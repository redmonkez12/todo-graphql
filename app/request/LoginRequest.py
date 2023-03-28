import strawberry


@strawberry.input
class LoginRequest:
    username: str
    password: str
