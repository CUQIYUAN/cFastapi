from typing import Mapping, TypedDict

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse


class MsExceptionResponse(TypedDict):
    error: str
    error_description: str
    error_codes: list[str]
    timestamp: str
    trace_id: str
    correlation_id: str


class MsException(Exception):
    def __init__(
        self,
        status_code: int,
        content: MsExceptionResponse,
        media_type: str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        self.status_code = status_code
        self.content = content
        self.media_type = media_type
        self.headers = headers


def exception(app: FastAPI) -> None:
    @app.exception_handler(MsException)
    async def _1(_: Request, exc: MsException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.content,
            headers=exc.headers,
            media_type=exc.media_type,
        )
