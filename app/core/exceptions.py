import logging

from fastapi import Request
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


async def global_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:

    request_id = getattr(
        request.state,
        "request_id",
        "unknown",
    )

    logger.exception(
        "request_id=%s unhandled_exception=%s",
        request_id,
        type(exc).__name__,
    )

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "request_id": request_id,
        },
    )