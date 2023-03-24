import strawberry
from strawberry.types import Info

from app.request.CreateUserRequest import CreateUserRequest
from app.services.UserService import UserService


@strawberry.type
class UserMutation:

    @strawberry.mutation
    async def create_user(self, info: Info, data: CreateUserRequest):
        user_service: UserService = info.context["user_service"]

        new_user = await user_service.create_user(data)
        return new_user
