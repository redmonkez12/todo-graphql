from pydantic import BaseModel
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

from app.auth.token import SECRET_KEY, ALGORITHM
from app.exceptions.UserNotAuthorizedException import UserNotAuthorizedException
from app.repository.GetByUsername import GetByUsername
from app.services.UserService import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    username: str | None = None


async def get_current_user(
        token: str,
        user_service: UserService
) -> GetByUsername:
    credentials_exception = UserNotAuthorizedException("Could not validate credentials")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = await user_service.get_by_username(token_data.username)
    if user is None:
        raise credentials_exception

    return user
