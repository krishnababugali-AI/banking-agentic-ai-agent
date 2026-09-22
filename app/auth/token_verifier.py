import time

import httpx
import jwt

from cryptography import x509
from cryptography.hazmat.primitives import serialization


PROJECT_ID = "banking-agentic-ai-agent"

ISSUER = "https://" + "securetoken.google.com/" + PROJECT_ID

GOOGLE_CERTS_URL = (
    "https://"
    + "www.googleapis.com"
    + "/robot/v1/metadata/x509/"
    + "securetoken@system.gserviceaccount.com"
)


async def verify_identity_token(id_token: str) -> dict:
    # Read JWT header.
    header = jwt.get_unverified_header(id_token)

    if header.get("alg") != "RS256":
        raise ValueError("Invalid token algorithm")

    kid = header.get("kid")

    if not kid:
        raise ValueError("Token is missing kid")

    # Fetch Google's signing certificates.
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(GOOGLE_CERTS_URL)
        response.raise_for_status()
        certificates = response.json()

    certificate_pem = certificates.get(kid)

    if certificate_pem is None:
        raise ValueError("Unknown token signing key")

    # Convert Google's X.509 certificate into an RSA public key.
    certificate = x509.load_pem_x509_certificate(
        certificate_pem.encode("utf-8")
    )

    public_key = certificate.public_key()

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    # Verify JWT signature and standard claims.
    claims = jwt.decode(
        id_token,
        public_key_pem,
        algorithms=["RS256"],
        audience=PROJECT_ID,
        issuer=ISSUER,
        options={
            "require": ["exp", "iat", "aud", "iss", "sub", "auth_time"],
        },
    )

    # Additional Identity Platform checks.
    now = int(time.time())

    subject = claims.get("sub")
    issued_at = claims.get("iat")
    auth_time = claims.get("auth_time")

    if not isinstance(subject, str) or not subject:
        raise ValueError("Invalid token subject")

    if len(subject) > 128:
        raise ValueError("Invalid token subject")

    if not isinstance(issued_at, int) or issued_at > now:
        raise ValueError("Invalid issued-at time")

    if not isinstance(auth_time, int) or auth_time > now:
        raise ValueError("Invalid authentication time")

    return claims