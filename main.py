import strawberry
from fastapi import FastAPI, Depends
from strawberry.tools import merge_types
from strawberry.fastapi import GraphQLRouter

from app.deps import get_todo_service, get_user_service
from app.mutations.TodoMutation import TodoMutation
from app.mutations.UserMutation import UserMutation
from app.queries.TodoQuery import TodoQuery
from app.services.TodoService import TodoService
from app.services.UserService import UserService
from database import init_db


async def get_context(
        todo_service: TodoService = Depends(get_todo_service),
        user_service: UserService = Depends(get_user_service),
):
    return {
        "todo_service": todo_service,
        "user_service": user_service,
    }


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


all_queries = merge_types("AllQueries", (Query, TodoQuery))
all_mutations = merge_types("AllMutations", (TodoMutation, UserMutation))

schema = strawberry.Schema(query=all_queries, mutation=all_mutations)

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app.include_router(graphql_app, prefix="/graphql")
