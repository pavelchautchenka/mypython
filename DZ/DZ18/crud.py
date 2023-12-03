from sqlalchemy import select
from models import Note, session


def get_notes(uuid: str):
    query = select(Note).where(Note.uuid == uuid)

    return session.execute(query).scalar_one()


def create_notes(title: str, content: str):
    note = Note(title=title, content=content)
    session.add(note)
    session.commit()
    session.refresh(note)
    return note