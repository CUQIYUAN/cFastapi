from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .ms.router import router as ms_router

api = APIRouter()

api.include_router(ms_router)


@api.get("/{path:path}", include_in_schema=False)
async def read_root(path: str) -> JSONResponse:
    return JSONResponse(status_code=404, content={"msg": "Not Found"})
