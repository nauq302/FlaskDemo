from .FlaskApp import app
import flask 

from entity import Student
from model import StudentDAL
from datetime import datetime

@app.route("/insert", methods=["GET"])
def insert_get() -> str:
    return flask.render_template("insert.html")

        

@app.route("/insert", methods=["POST"])
def insert_post() -> str:
    request = flask.request

    StudentDAL.insert(
        name = request.form["name"],
        department = request.form["dept"],
        birthDate = datetime.strptime(request.form["dob"], "%Y-%m-%d").date()
    )


    return flask.redirect("home")