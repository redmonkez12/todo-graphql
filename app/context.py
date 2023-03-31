from fastapi import Depends

from starlette.requests import  Request

from app.auth.user import get_current_user
from app.deps import get_user_service, get_todo_service
from app.services.TodoService import TodoService
from app.services.UserService import UserService


async def get_context(
        request: Request,
        todo_service: TodoService = Depends(get_todo_service),
        user_service: UserService = Depends(get_user_service),
):
    authorization = request.headers.get("Authorization", "")
    authorization = authorization.replace("Bearer ", "")

    async def get_lazy_user():
        result = await get_current_user(authorization, user_service)
        print(result)
        return result

    return {
        "todo_service": todo_service,
        "user_service": user_service,
        "get_user": get_lazy_user
    }
