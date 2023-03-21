import strawberry
from strawberry.types import Info

from app.request.TodoRequest import TodoRequest
from app.responses.TodoResponse import TodoResponse
from app.services.TodoService import TodoService


@strawberry.type
class TodoMutation:
    @strawberry.mutation
    async def create_todo(self, info: Info, label: str) -> TodoResponse:
        todo_service: TodoService = info.context["todo_service"]

        return await todo_service.create_todo(TodoRequest(label=label))
