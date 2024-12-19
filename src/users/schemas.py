from pydantic import BaseModel, EmailStr, Field


class SUserRegister(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 знаков")
    

class SUserLogin(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта")
    password: str = Field(..., min_length=8, max_length=50, description="Пароль, от 8 до 50 знаков")

# class SUsers(BaseModel):
#     id: int = Field(..., description="ID пользователя")
#     firstname: str = Field(..., description="Имя пользователя")
#     lastname: str = Field(..., description="Фамилия пользователя")