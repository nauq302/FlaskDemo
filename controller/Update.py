from .FlaskApp import app
import flask 

from entity import Student
from model import StudentDAL
from datetime import datetime

@app.route("/update", methods = ["GET"])
def update_get():
    id = int(flask.request.args.get("id"))
    student = StudentDAL.get(id)

    return flask.render_template("update.html", student = student)


@app.route("/update", methods = ["POST"])
def update_post():
    request = flask.request

    student = Student.Student(
        id = int(request.form["id"]),
        name = request.form["name"],
        department = request.form["dept"],
        birthDate = datetime.strptime(request.form["dob"], "%Y-%m-%d").date()
    )

    StudentDAL.update(student)

    return flask.redirect("home")