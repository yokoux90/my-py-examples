from typing import Annotated
from fastapi import Depends
from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, Session, create_engine

from model import Event, Job


connect_string: str = "mysql+pymysql://root:example@localhost:3306/celery"
engine: Engine = create_engine(connect_string)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine, tables=[Job.__table__, Event.__table__])


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
