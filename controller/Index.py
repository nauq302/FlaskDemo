from .FlaskApp import app
import flask 

@app.route("/")
def index() -> str:
    return flask.render_template('index.html')