from src.database import Base
from sqlalchemy import Column, Date, Integer, ForeignKey, Text


class Query(Base):

    __tablename__ = "query"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    query = Column(Text, nullable=False)
    time = Column(Date, nullable=False)