import strawberry


@strawberry.input
class CreateUserRequest:
    first_name: str
    last_name: str
    email: str
    password: str
    username: str
    birthdate: str
