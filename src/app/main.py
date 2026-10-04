from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

from .routers import ms_router, validate_router
from .routers.ms.exception import exception

app = FastAPI(
    title="cFastapi",
    # summary,
    # description,
    version="0.1.0",
    contact={
        "name": "CUQIYUAN",
        "url": "http://github.com/CUQIYUAN",
        "email": "3489143596@qq.com",
    },
    # license_info
    # //
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    redirect_slashes=False,
)

app.include_router(ms_router)
app.include_router(validate_router)

# // exception
exception(app)
