import strawberry
import asyncpg

from sqlmodel import Session, select, asc, desc, delete, update
from sqlalchemy import exc

from app.exceptions.TodoDuplicationException import TodoDuplicationException
from app.models.Todo import Todo
from enum import Enum

from app.repository.GetByUsername import GetByUsername
from app.request.TodoRequest import TodoRequest
from app.request.UpdateTodoRequest import UpdateTodoRequest


@strawberry.enum
class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"


class TodoService:
    def __init__(self, session: Session):
        self.session = session

    async def create_todo(self, data: TodoRequest, user: GetByUsername):
        try:
            new_todo = Todo(label=data.label, user_id=user.user_id)

            self.session.add(new_todo)
            await self.session.commit()

            return new_todo
        except (exc.IntegrityError, asyncpg.exceptions.UniqueViolationError):
            raise TodoDuplicationException(f"Todo [{data.label}] already exists")

    async def get_todo(self, todo_id: int):
        query = (
            select(Todo)
            .where(Todo.todo_id == todo_id)
        )

        result = await self.session.execute(query)
        return result.one()

    async def get_todos(self, page: int, limit: int, order_by: str, sort_direction):
        query = (
            select(Todo)
            .offset(page * limit)
            .limit(limit)
        )

        if order_by == "todoId":
            query = query.order_by(asc(Todo.todo_id) if sort_direction == SortOrder.ASC else desc(Todo.todo_id))

        if order_by == "label":
            query = query.order_by(asc(Todo.label) if sort_direction == SortOrder.ASC else desc(Todo.label))

        data = await self.session.execute(query)
        return data.scalars().all()

    async def update_todo(self, new_todo: UpdateTodoRequest):
        query = (
            update(Todo)
            .values(label=new_todo.label)
            .where(Todo.todo_id == new_todo.id)
            .returning(Todo.todo_id, Todo.label)
        )

        result = await self.session.execute(query)
        await self.session.commit()
        return result.one()

    async def delete_todo(self, todo_id: int):
        query = (
            delete(Todo)
            .where(Todo.todo_id == todo_id)
        )

        result = await self.session.execute(query)
        await self.session.commit()
        return result.one()
