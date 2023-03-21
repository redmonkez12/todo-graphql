from pydantic import BaseModel


class TodoRequest(BaseModel):
    label: str
