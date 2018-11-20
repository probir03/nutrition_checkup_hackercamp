from flask import Blueprint, request
from flask import render_template
from App.Response import *
from nutrition_calculator.Controllers.image_processing_controller import calculate_nutrition
import os
import app

health = Blueprint('health', __name__, template_folder='templates')
UPLOAD_FOLDER = os.path.basename('uploads')


@health.route('/')
def index():
	return render_template('home.html')

@health.route('/images/upload', methods=['POST'])
def statement_list():
    file = request.files['image']
    f = os.path.join(UPLOAD_FOLDER, file.filename)
    d = dict(request.form)
    print(d)
    data = {}
    for key, value in d.items():
        data[key] = value[0]
    idel_intake = 0
    if data:
        if data.get('gender').lower() == 'm':
            idel_intake = 10 * int(data.get('weight')) + 6.25 * int(data.get('height')) - 5 * int(data.get('age')) + 5
        else:
            idel_intake = 10 * int(data.get('weight')) + 6.25 * int(data.get('height')) - 5 * int(data.get('age')) - 161

    file.save(f)
    res = calculate_nutrition(f)
    return render_template('uploaded.html', data=res, idel=idel_intake)
    return respondWithItem(res)
