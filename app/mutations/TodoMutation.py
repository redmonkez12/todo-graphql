import strawberry
from strawberry.types import Info

from app.errors.TodoDuplication import TodoDuplication
from app.errors.TodoNotFound import TodoNotFound
from app.request.TodoRequest import TodoRequest
from app.request.UpdateTodoRequest import UpdateTodoRequest
from app.responses.OneTodoResponse import OneTodoResponse
from app.services.TodoService import TodoService


@strawberry.type
class TodoMutation:

    @strawberry.mutation
    async def create_todo(self, info: Info, label: str) -> OneTodoResponse:
        try:
            todo_service: TodoService = info.context["todo_service"]
            return await todo_service.create_todo(TodoRequest(label=label))
        except Exception as e:
            print(e)
            return TodoDuplication(label=label, message=f"Todo [{label}] already exists")

    @strawberry.mutation
    async def update_todo(self, info: Info, todo: UpdateTodoRequest) -> OneTodoResponse:
        try:
            todo_service: TodoService = info.context["todo_service"]
            result = await todo_service.update_todo(todo)
            return result
        except Exception:
            return TodoNotFound(id=id, message=f"Todo [{id}] not found")

    @strawberry.mutation
    async def delete_todo(self, info: Info, todo_id: int) -> None:
        todo_service: TodoService = info.context["todo_service"]
        await todo_service.delete_todo(todo_id)
