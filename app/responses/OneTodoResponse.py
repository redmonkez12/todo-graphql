import strawberry

from app.errors.TodoDuplication import TodoDuplication
from app.responses.TodoResponse import TodoResponse

OneTodoResponse = strawberry.union(
    "OneTodoResponse", [TodoResponse, TodoDuplication]
)
