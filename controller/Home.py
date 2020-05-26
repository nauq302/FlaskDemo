from .FlaskApp import app
import flask 

from entity import Student
from model import StudentDAL

@app.route("/home")
def home() -> str:
    students = StudentDAL.getAll()
    return flask.render_template('home.html', students = students)
