import datetime
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy import text
from src.query.dao import QueryDAO
from src.users.dependencies import get_current_user
from src.users.models import Users
from src.query.schemas import SQuery
from src.database import async_session_maker
from sqlalchemy import exc

router = APIRouter(
    prefix="/query",
    tags=["Query"]
)

create_table = """

CREATE TABLE product_category (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE product (
  id INT PRIMARY KEY,
  category_id INT,
  name VARCHAR(100)
);

INSERT INTO product_category VALUES (1, 'Food');
INSERT INTO product_category VALUES (2, 'Gadget');

INSERT INTO product VALUES (1, 1, 'Milk');
INSERT INTO product VALUES (2, 1, 'Pineapples');
INSERT INTO product VALUES (3, 2, 'Apple iPhone 15');"""

@router.post("/", description=f"Введите запрос, например {create_table}")
async def do_query(query_text: str = Body(...), current_user: Users = Depends(get_current_user)):
    
    try:
        async with async_session_maker() as session:
            query = text(query_text)
            result = await session.execute(query)  
            await session.commit()       
            await QueryDAO.add(user_id=current_user.id, query=query_text, time=datetime.datetime.now())
            if "CREATE" in query_text.upper():
                 return {"status": "success", "data": "запрос не вернул никаких данных"}
            else:
                 # Получаем все строки и столбцы
                rows = result.fetchall()
                # Получаем имена столбцов
                column_names = result.keys()
                # Преобразуем результаты в список словарей
                data = [dict(zip(column_names, row)) for row in rows]
                return {"status": "success", "data": data}
    except exc.SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))
            
                
            

    
        
    




@router.get("/")
async def get_history(current_user: Users = Depends(get_current_user)):
    return {}

