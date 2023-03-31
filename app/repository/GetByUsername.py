from pydantic import BaseModel


class GetByUsername(BaseModel):
    user_id: int
    username: str
    email: str
    password: str
