
from flask import Flask, Response, request
from sqlalchemy import exc
from models import create_table, drop_tables
from crud import get_notes, create_notes


app = Flask(__name__)

drop_tables()
create_table()


@app.route("/", methods=['GET'])
def get_create_note():
    return (
        "<h1> Create Note </h1>"
        '<form action="/" method="post">' 
        '   <p> Title: <input type="text" name="title"> </p>'     
        '   <p> Content: <input type="text" name="content"> </p>' 
        '   <p> <input type="submit"> </p>'
        '</form>'
    )


@app.route("/", methods=['POST'] )
def register_note():
    user_data = request.form

    note = create_notes(title=user_data["title"], content=user_data["content"])

    return f"""
    <h1>Your note successfully created !</h1>
    <p>ID: {note.uuid}</p>"""


@app.route("/<uuid>",methods=['GET'])
def note_view(uuid: str):
    try:
        note = get_notes(uuid)

    except exc.NoResultFound:
        return Response("Note not founded", status=404)

    return f"""
        <h1>your note under id {note.uuid} </h1>
        <p>Title: {note.title} </p>
        <p>Content: {note.content}</p>
        <p>Created at: {note.created_at} </p>
        
    """


if __name__ == "__main__":
    app.run(debug=True)
