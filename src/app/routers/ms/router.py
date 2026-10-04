from typing import Annotated

from fastapi import APIRouter, Body, HTTPException
from httpx import AsyncClient

from .exception import MsException
from .models import MsAuthorizationRequest, MsTokenRequest, MsTokenResponse

router = APIRouter(prefix="/ms")

TokenRequestModel = Annotated[
    MsTokenRequest,
    Body(
        media_type="application/json",
        title="Token请求",
        description="""
""",
    ),
]


@router.post(
    "/token",
    # //
    status_code=200,
    response_model=MsTokenResponse,
    response_model_exclude_unset=True,
    response_model_exclude_none=True,
    # //
)
async def token(data: TokenRequestModel) -> MsTokenResponse:
    async with AsyncClient() as client:
        res = await client.post(
            f"https://login.microsoftonline.com/{data.tenant}/oauth2/v2.0/token",
            json=data.model_dump(),
            timeout=20.0,
        )

        if res.status_code == 200:
            return MsTokenResponse.model_validate(res.json())
        else:
            raise MsException(status_code=res.status_code, content=res.json())
