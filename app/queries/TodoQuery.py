import strawberry
from strawberry.types import Info

from app.responses.TodoResponse import TodoResponse
from app.services.TodoService import TodoService


@strawberry.type
class TodoQuery:
    @strawberry.field
    async def todos(self, info: Info) -> list[TodoResponse]:
        todo_service: TodoService = info.context["todo_service"]

        return await todo_service.get_todos(0, 10)
