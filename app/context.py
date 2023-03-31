from functools import cached_property
from dataclasses import dataclass

from fastapi import Depends
from starlette.requests import Request
from strawberry.types import Info as _Info
from strawberry.fastapi import BaseContext
from strawberry.types.info import RootValueType

from app.auth.user import get_current_user
from app.deps import get_user_service, get_todo_service
from app.repository.GetByUsername import GetByUsername
from app.services.TodoService import TodoService
from app.services.UserService import UserService


# @dataclass
# class Context(BaseContext):
#     @cached_property
#     async def user(self, user_service: UserService = Depends(get_user_service)) -> GetByUsername | None:
#         if not self.request:
#             return None
#
#         authorization = self.request.headers.get("Authorization", "")
#         print(authorization, "fokerko")
#
#         return await get_current_user(authorization, user_service)
#
#     @cached_property
#     async def todo_service(self, todo_service: TodoService = Depends(get_todo_service)):
#         return todo_service
#
#     @cached_property
#     async def user_service(self, user_service: UserService = Depends(get_user_service)):
#         return user_service

async def get_context(
        request: Request,
        todo_service: TodoService = Depends(get_todo_service),
        user_service: UserService = Depends(get_user_service),
):
    authorization = request.headers.get("Authorization", "")
    authorization = authorization.replace("Bearer ", "")
    print(authorization, "fokerko")

    return {
        "todo_service": todo_service,
        "user_service": user_service,
        "user": await get_current_user(authorization, user_service)
    }
