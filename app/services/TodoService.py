import strawberry

from sqlmodel import Session, select, asc, desc

from app.models.Todo import Todo
from app.request.TodoRequest import TodoRequest
from enum import Enum


@strawberry.enum
class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"


class TodoService:
    def __init__(self, session: Session):
        self.session = session

    async def create_todo(self, data: TodoRequest):
        new_todo = Todo(label=data.label)

        self.session.add(new_todo)
        await self.session.commit()

        return new_todo

    async def get_todo(self, todo_id: int):
        query = (
            select(Todo)
            .where(Todo.id == todo_id)
        )

        result = await self.session.execute(query)
        return result.one()

    async def get_todos(self, page: int, limit: int, order_by: str, sort_direction):
        query = (
            select(Todo)
            .offset(page * limit)
            .limit(limit)
        )

        if order_by == "id":
            query = query.order_by(asc(Todo.id) if sort_direction == SortOrder.ASC else desc(Todo.id))

        if order_by == "label":
            query = query.order_by(asc(Todo.label) if sort_direction == SortOrder.ASC else desc(Todo.label))

        data = await self.session.execute(query)
        return data.scalars().all()

    # async def update_todo(self, new_todo: UpdateTodoRequest):
    #     query = (
    #         update(Todo)
    #         .values(label=new_todo.label)
    #         .where(Todo.todo_id == new_todo.todo_id)
    #     )
    #
    #     await self.session.execute(query)
    #     await self.session.commit()
    #
    # async def delete_todo(self, todo_id: int):
    #     query = (
    #         delete(Todo)
    #         .where(Todo.todo_id == todo_id)
    #     )
    #
    #     await self.session.execute(query)
    #     await self.session.commit()