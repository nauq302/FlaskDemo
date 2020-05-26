from .FlaskApp import app
import flask 

from entity import Student
from model import StudentDAL

@app.route("/delete", methods=["GET"])
def delete_get():
    id = int(flask.request.args.get("id"))
    student = StudentDAL.get(id)

    return flask.render_template("delete.html", student = student)


@app.route("/delete", methods=["POST"])
def delete_post():
    id = int(flask.request.form["id"])
    StudentDAL.remove(id)

    return flask.redirect("home")