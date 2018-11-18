from flask import Flask, render_template, redirect, flash, url_for, session
from models import Intake, Food
from Exceptions.ExceptionHandler import FeedrException
from categorization.nutritionRepository import NutritionRepository, FoodRepository
from models import Food
import datetime
import models
import helpers

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def process_image(file_path):

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    # file_path = os.path.join(
    #     os.path.dirname(__file__),
    #     'burger.jpg')

    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels


def calculate_nutrition(file_path):
    repo = NutritionRepository()
    food_repo = FoodRepository()
    labels = process_image(file_path)
    total_cal = 0
    for label in labels:
        food = search_food(Food, {'name': label})
        if food:
            total_cal += food.get('calories')
    input_data = {
        'id': helpers.generate_unique_code().__str__(),
        'image_name': file_path,
        'calories': calories
    }
    res = repo.store(Intake, input_data)
    return res
