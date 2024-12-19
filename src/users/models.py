from src.database import Base
from sqlalchemy import Column, Computed, Date, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False) 
    hashed_password = Column(String, nullable=False)