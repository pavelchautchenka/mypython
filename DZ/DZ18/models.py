from sqlalchemy import Column, Integer, String, VARCHAR, Text, select, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import uuid
from datetime import datetime


dsn = "sqlite:///hometsk18.db"
engine = create_engine(dsn, echo=True)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(VARCHAR(100))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now())


def create_table():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


drop_tables()
create_table()


def get_notes(uuid: str):
    query = select(Note).where(Note.uuid == uuid)

    return session.execute(query).scalar_one()


def create_notes(title: str, content: str):
    note = Note(title=title, content=content)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note
