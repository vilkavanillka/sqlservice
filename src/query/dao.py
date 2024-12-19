from src.dao.base import BaseDAO
from src.query.models import Query


class QueryDAO(BaseDAO):
    """Класс для работы с БД. Наследуется от базового класса"""
    model = Query