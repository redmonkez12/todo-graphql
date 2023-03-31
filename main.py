import strawberry
from fastapi import FastAPI
from strawberry.tools import merge_types
from strawberry.fastapi import GraphQLRouter

from app.context import get_context
from app.mutations.TodoMutation import TodoMutation
from app.mutations.UserMutation import UserMutation
from app.queries.TodoQuery import TodoQuery
from database import init_db


@strawberry.type
class User:
    name: str
    age: int


all_queries = merge_types("AllQueries", (TodoQuery,))
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
