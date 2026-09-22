import logging

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.security_context import SecurityContext
from app.auth.token_verifier import verify_identity_token


logger = logging.getLogger(__name__)

bearer_scheme = HTTPBearer(auto_error=False)


async def get_security_context(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> SecurityContext:

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authorization token",
        )

    try:
        claims = await verify_identity_token(
            credentials.credentials
        )

    except Exception as exc:
        logger.warning(
            "Identity token verification failed: %s",
            type(exc).__name__,
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token",
        ) from exc

    uid = claims["sub"]

    return SecurityContext(
        user_id=uid,
        customer_id="CUST-1001",
        roles=["customer"],
        scopes=["transactions:read"],
    )