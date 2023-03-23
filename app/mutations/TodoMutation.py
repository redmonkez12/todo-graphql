import strawberry
from strawberry.types import Info

from app.request.TodoRequest import TodoRequest
from app.request.UpdateTodoRequest import UpdateTodoRequest
from app.responses.TodoResponse import TodoResponse
from app.services.TodoService import TodoService


@strawberry.type
class TodoMutation:

    @strawberry.mutation
    async def create_todo(self, info: Info, label: str) -> TodoResponse:
        todo_service: TodoService = info.context["todo_service"]

        return await todo_service.create_todo(TodoRequest(label=label))

    @strawberry.mutation
    async def update_todo(self, info: Info, todo: UpdateTodoRequest) -> TodoResponse:
        todo_service: TodoService = info.context["todo_service"]
        result = await todo_service.update_todo(todo)
        return result

    @strawberry.mutation
    async def delete_todo(self, info: Info, todo_id: int) -> None:
        todo_service: TodoService = info.context["todo_service"]
        await todo_service.delete_todo(todo_id)
