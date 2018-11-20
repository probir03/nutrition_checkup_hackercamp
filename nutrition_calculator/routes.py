from flask import Blueprint, request
from flask import render_template
from App.Response import *
from nutrition_calculator.Controllers.image_processing_controller import calculate_nutrition
import os
import app

health = Blueprint('health', __name__, template_folder='templates')
UPLOAD_FOLDER = os.path.basename('uploads')


@health.route('/foods/intakes', methods=['POST'])
def statement_list():
    file = request.files['image']
    f = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(f)
    res = calculate_nutrition(f)
    return respondWithItem(res)
