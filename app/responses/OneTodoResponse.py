import strawberry

from app.errors.TodoNotFound import TodoNotFound
from app.responses.TodoResponse import TodoResponse

OneTodoResponse = strawberry.union(
    "GetTodoResponse", [TodoResponse, TodoNotFound]
)
