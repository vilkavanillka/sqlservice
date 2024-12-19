from src.users.dao import UsersDAO
from src.exceptions import IncorrectEmailOrPasswordException
from src.config import settings
from pydantic import EmailStr
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    ''' Генерирует хэшированный пароль '''
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    """Проверяет пароль на валидность"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """Создает токен"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encode_jwt


async def authenticate_user(email: EmailStr, password: str):
    ''' Аутенфицирует пользователя, возвращает либо его, либо ошибку '''
    user = await UsersDAO.find_one_or_none(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        raise IncorrectEmailOrPasswordException
    return user