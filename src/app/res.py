from collections.abc import Mapping

# core/error_code.py
from enum import IntEnum
from typing import Any, TypedDict

from fastapi.responses import JSONResponse


class ResponseDict(TypedDict):
    code: int
    msg: str
    data: Any | None


class APPResponse(JSONResponse):
    media_type = "application/json"

    def __init__(
        self,
        content: str,
        status_code: int = 200,
        headers: Mapping[str, str] | None = None,
        media_type: str | None = None,
    ) -> None:
        super().__init__(content, status_code, headers, media_type)


class ErrorCode(IntEnum):
    PARAM_INVALID = 10001
    MISSING_PARAM = 10002
    UNAUTHORIZED = 20001
    FORBIDDEN = 20002
    USER_NOT_FOUND = 30001
    SYSTEM_ERROR = 50000


# 错误码 -> 默认提示
ERROR_MESSAGES = {
    ErrorCode.PARAM_INVALID: "参数校验失败",
    ErrorCode.MISSING_PARAM: "缺少必要参数",
    ErrorCode.UNAUTHORIZED: "未登录或登录已过期",
    ErrorCode.FORBIDDEN: "无权限访问",
    ErrorCode.USER_NOT_FOUND: "用户不存在",
    ErrorCode.SYSTEM_ERROR: "系统繁忙，请稍后重试",
}
