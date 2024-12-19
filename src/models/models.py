from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean
from sqlalchemy.orm import declarative_base

from src.database import metadata


connection = Table(
    "connection",
    metadata,
    Column("id", Integer, nullable = False),
    Column("database", String, nullable = False),
)

query = Table(
    "query",
    metadata,
    Column("id", Integer, nullable=False),
    Column("queryname", String, nullable = False),
    Column("time", String, nullable = False),
)


