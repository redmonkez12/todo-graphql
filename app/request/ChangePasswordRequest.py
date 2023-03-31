import strawberry


@strawberry.input
class ChangePasswordRequest:
    old_password: str
    new_password: str
