from app.services.TodoService import TodoService
from app.services.UserTodoService import UserTodoService
from database import async_session


async def get_todo_service():
    async with async_session() as session:
        async with session.begin():
            yield TodoService(session)


async def get_user_todo_service():
    async with async_session() as session:
        async with session.begin():
            yield UserTodoService(session)
