from typing import Any, Union
from myauth import authenticate_header, authenticate_query_param

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info

from app.services.UserService import UserService


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        request: Union[Request, WebSocket] = info.context["request"]
        user_service: UserService = info.context["user_service"]

        if "Authorization" in request.headers:
            return authenticate_header(request)

        if "auth" in request.query_params:
            return authenticate_query_params(request)

        return False
