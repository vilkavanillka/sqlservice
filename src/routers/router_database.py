from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi_users import FastAPIUsers

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth import auth_backend, get_current_user
from src.auth.models import User
from src.database import get_async_session
from src.auth.manager import get_user_manager

from src.config import DB_HOST, DB_PORT, DB_PASS, DB_USER, DB_NAME
from src.models.models import connection
import psycopg2

router = APIRouter(
    prefix="/database",
    tags=["database"],
)

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self, dbname: str, user_id: int):
        new_database = f"{dbname}_{user_id}"
        self.connection = new_database

database_connection = DatabaseConnection()

@router.post("/create_db_server") # создание БД(наверное)
async def create_db_server(new_database: str, session: AsyncSession = Depends(get_async_session),
                           user: int = Depends(get_current_user), token: Annotated[str, Header()]=None):
    if not user:
        raise HTTPException(status_code=401, detail="You need to be logged in to create a server")

    conn = psycopg2.connect(
        dbname = DB_NAME,
        user = DB_USER,
        password = DB_PASS,
        host = DB_HOST,
        port = DB_PORT
    )

    new_database_concat = "_".join([new_database, str(user)]) # костыль, если два юзера одинаково назовут бд

    try:
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("CREATE DATABASE " + new_database_concat)
        conn.close()  # Закрываем соединение

    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "details": "Такая БД уже существует"
        })

    stmt = insert(connection).values(id = user, database =new_database_concat)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success",
            "details": "Создана база данных " + new_database
            }

@router.post("/connect_to_db/")
async def connect_to_db(dbname: str, user: int = Depends(get_current_user),
                        token: Annotated[str, Header()]=None):
    try:
        database_connection.connect(dbname, user)
        return {"status": "success",
                "details": "Вы подключены к базе данных " + database_connection.connection}
    except Exception:
        raise HTTPException(status_code=489, detail={
            "status": "error",
            "details": "Такой базы данных не существует",
        })