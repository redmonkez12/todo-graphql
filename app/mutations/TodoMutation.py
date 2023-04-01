import strawberry
from strawberry.types import Info
from sqlalchemy.exc import NoResultFound

from app.errors.ErrorResponse import ErrorResponse
from app.errors.TodoDuplication import TodoDuplication
from app.errors.TodoNotFound import TodoNotFound
from app.exceptions.TodoDuplicationException import TodoDuplicationException
from app.repository.GetByUsername import GetByUsername
from app.request.TodoRequest import TodoRequest
from app.request.UpdateTodoRequest import UpdateTodoRequest
from app.responses.DeleteTodoResponse import DeleteTodoResponse
from app.responses.OneTodoResponse import OneTodoResponse
from app.services.TodoService import TodoService


@strawberry.type
class TodoMutation:

    @strawberry.mutation
    async def create_todo(self, info: Info, label: str) -> OneTodoResponse:
        try:
            todo_service: TodoService = info.context["todo_service"]
            get_user = info.context["get_user"]
            user: GetByUsername = await get_user()

            return await todo_service.create_todo(TodoRequest(label=label), user)
        except TodoDuplicationException as e:
            return TodoDuplication(label=label, message=str(e))
        except Exception:
            return ErrorResponse()

    @strawberry.mutation
    async def update_todo(self, info: Info, todo: UpdateTodoRequest) -> OneTodoResponse:
        try:
            todo_service: TodoService = info.context["todo_service"]
            result = await todo_service.update_todo(todo)
            return result
        except NoResultFound:
            return TodoNotFound(id=todo.id, message=f"Todo [{todo.id}] not found")
        except Exception:
            return ErrorResponse()

    @strawberry.mutation
    async def delete_todo(self, info: Info, todo_id: int) -> DeleteTodoResponse:
        try:
            todo_service: TodoService = info.context["todo_service"]
            await todo_service.delete_todo(todo_id)
        except NoResultFound:
            return TodoNotFound(id=todo_id, message=f"Todo [{todo_id}] not found")
        except Exception:
            return ErrorResponse()
