import strawberry
from strawberry.types import Info

from app.errors.TodoNotFound import TodoNotFound
from app.responses.OneTodoResponse import OneTodoResponse
from app.responses.TodoResponse import TodoResponse
from app.services.TodoService import TodoService, SortOrder


@strawberry.type
class TodoQuery:
    @strawberry.field
    async def todos(self, info: Info,
                    limit: int, page: int,
                    order_by: str,
                    sort_direction: SortOrder = SortOrder.ASC
                    ) -> list[TodoResponse]:
        todo_service: TodoService = info.context["todo_service"]

        return await todo_service.get_todos(limit, page, order_by, sort_direction)

    @strawberry.field
    async def todo(self, info: Info, todo_id: int) -> OneTodoResponse:
        try:
            todo_service: TodoService = info.context["todo_service"]
            return await todo_service.get_todo(todo_id)
        except Exception:
            return TodoNotFound(id=id, message=f"Todo [{todo_id}] not found")
