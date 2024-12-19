from fastapi import APIRouter, Depends, Response
from src.exceptions import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from src.users.auth import authenticate_user, create_access_token, get_password_hash
from src.users.dependencies import get_current_user
from src.users.models import Users
from src.users.schemas import SUserLogin
from src.users.dao import UsersDAO
from typing import List
from src.query.schemas import SQuery

router = APIRouter(
    prefix="/query",
    tags=["Query"]
)


@router.post("/")
async def do_query(query_text: SQuery, current_user: Users = Depends(get_current_user)):
    pass



@router.get("/")
async def get_history(current_user: Users = Depends(get_current_user)):
    pass

