from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# https://learn.microsoft.com/zh-cn/entra/identity-platform/v2-oauth2-auth-code-flow#protocol-details
class MsAuthorizationRequest(BaseModel):
    tenant: str
    client_id: str
    response_type: str = "code | code id_token"
    redirect_uri: str
    scope: str
    response_mode: Literal["query", "fragment", "form_post"]
    state: str

    model_config = ConfigDict(json_schema_extra={"example": {}})


_MS_TOKEN_BASE_REQUEST_EXAMPLE_ = {
    "tenant": "common",
    "client_id": "11112222-bbbb-3333-cccc-4444dddd5555",
    "scope": "https://graph.microsoft.com/mail.read",
    "code": "OAAABAAAAiL9Kn2Z27UubvWFPbm0gLWQJVzCTE9UkP3pSx1aXxUjq3n8b2JRLk4OxVXr...",
    "redirect_uri": "...",
    "grant_type": "authorization_code",
    "code_verifier": "ThisIsntRandomButItNeedsToBe43CharactersLong",
}


class MsTokenBaseRequest(BaseModel):
    tenant: str = Field("common", exclude=True)
    client_id: str
    scope: str
    code: str
    redirect_uri: str
    grant_type: Literal["authorization_code"] = "authorization_code"
    code_verifier: str | None = None

    model_config = ConfigDict(json_schema_extra={"example": {**_MS_TOKEN_BASE_REQUEST_EXAMPLE_}})


class MsTokenSecretRequest(MsTokenBaseRequest):
    client_secret: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                **_MS_TOKEN_BASE_REQUEST_EXAMPLE_,
                "client_secret": "sampleCredentia1s",
            }
        }
    )


class MsTokenAssertionRequest(MsTokenBaseRequest):
    client_assertion_type: Literal["urn:ietf:params:oauth:client-assertion-type:jwt-bearer"] = (
        "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    )
    client_assertion: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                **_MS_TOKEN_BASE_REQUEST_EXAMPLE_,
                "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                "client_assertion": "eyJhbGciOiJSUzI1NiIsIng1dCI6Imd4OHRHeXN5amNScUtqRlBuZDdSRnd2d1pJMCJ9.eyJ{a lot of characters here}M8U3bSUKKJDEg",
            }
        }
    )


MsTokenRequest = MsTokenSecretRequest | MsTokenAssertionRequest


class MsTokenResponse(BaseModel):
    token_type: str
    scope: str
    access_token: str
    expires_in: int
    refresh_token: str | None = None
    id_token: str | None = None


