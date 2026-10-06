from fastapi import FastAPI, Request, Response

from .api import api
from .api.ms.exception import exception
from .config import API_PREFIX

app = FastAPI(
    title="cFastapi",
    version="v0.1.0",
    # summary="",
    # description = Readme.read_text(encoding="utf-8"),
    contact={
        "name": "CUQIYUAN",
        "url": "http://github.com/CUQIYUAN",
        "email": "3489143596@qq.com",
    },
    # license_info={"name": "", "identifier": "", "url": ""},
    # //
    openapi_url=f"{API_PREFIX}/openapi.json",
    docs_url=f"{API_PREFIX}/docs",
    redoc_url=f"{API_PREFIX}/redoc",
    redirect_slashes=False,
    # // exception
)

# // router
app.include_router(api, prefix=API_PREFIX)


@app.get("/{path:path}", response_class=Response, include_in_schema=False)
async def frontend(path: str, request: Request) -> Response:
    env = request.scope["env"]
    asset_url = f"https://assets.local/{path}"
    resp = await env.ASSETS.fetch(asset_url)
    body = await resp.bytes()
    return Response(content=body, status_code=resp.status, headers=resp.headers)


# // exception
exception(app)
