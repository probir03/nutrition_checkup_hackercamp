from flask import Flask, Blueprint, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from Exceptions. ExceptionHandler import FoodException

app = Flask(__name__, static_folder="static")
CORS(app)
app.config.from_pyfile('env.py')
db = SQLAlchemy(app)

from Http.routes import base
from nutrition_calculator.routes import health
from Auth.routes import auth

app.register_blueprint(base)
app.register_blueprint(auth)
app.register_blueprint(health)

# custome handler


@app.errorhandler(FoodException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
