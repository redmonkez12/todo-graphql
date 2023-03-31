import strawberry


@strawberry.type
class GetByUsername:
    user_id: int
    username: str
    email: str
    password: str
