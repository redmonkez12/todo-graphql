import strawberry

from app.errors.ErrorResponse import ErrorResponse
from app.errors.TodoNotFound import TodoNotFound
from app.responses.EmptyResponse import EmptyResponse

DeleteTodoResponse = strawberry.union(
    "DeleteTodoResponse", (EmptyResponse, ErrorResponse, TodoNotFound),
)