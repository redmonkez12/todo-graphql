import strawberry
from strawberry.types import Info

from app.auth.token import create_access_token
from app.errors.ErrorResponse import ErrorResponse
from app.exceptions.UserNotAuthorizedException import UserNotAuthorizedException
from app.exceptions.UserNotFoundException import UserNotFoundException
from app.repository.GetByUsername import GetByUsername
from app.request.ChangePasswordRequest import ChangePasswordRequest
from app.request.LoginRequest import LoginRequest
from app.request.UserCreateRequest import CreateUserRequest
from app.responses.ChangePasswordResponse import ChangeResultResponse, ChangePasswordResponse
from app.responses.UserLoginResponse import LoginResultResponse, UserLoginResponse
from app.services.UserService import UserService, CreateUserModel


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, info: Info, data: CreateUserRequest) -> CreateUserModel:
        user_service: UserService = info.context["user_service"]

        new_user = await user_service.create_user(data)
        return new_user

    @strawberry.field
    async def login(self, info: Info, data: LoginRequest) -> LoginResultResponse:
        try:
            user_service: UserService = info.context["user_service"]
            user = await user_service.login(data)

            access_token = create_access_token(
                data={"sub": user.username}
            )

            return UserLoginResponse(access_token=access_token, token_type="bearer")
        except Exception as e:
            return ErrorResponse()

    @strawberry.mutation
    async def change_password(self, info: Info, data: ChangePasswordRequest) -> ChangeResultResponse:
        try:
            user_service: UserService = info.context["user_service"]
            get_user = info.context["get_user"]
            user: GetByUsername = await get_user()
            await user_service.change_password(user, data)

            return ChangePasswordResponse(message="Password changed")
        except UserNotAuthorizedException as e:
            return ErrorResponse(message=str(e), code="INVALID_CREDENTIALS")
        except UserNotFoundException as e:
            return ErrorResponse(message=str(e), code="USER_NOT_FOUND")
        except Exception as e:
            print(e)
            return ErrorResponse()
