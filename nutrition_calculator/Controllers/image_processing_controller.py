from flask import Flask, render_template, redirect, flash, url_for, session
from models import Intake, Food
from nutrition_calculator.nutritionRepository import NutritionRepository, FoodRepository
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
    response = client.web_detection(image=image)
    annotations = response.web_detection

    # if annotations.web_entities:
    #     for entity in annotations.web_entities:
    #         print('\n\tScore      : {}'.format(entity.score))
    #         print(u'\tDescription: {}'.format(entity.description))
    return annotations.web_entities


def calculate_nutrition(file_path):
    repo = NutritionRepository()
    food_repo = FoodRepository()
    labels = process_image(file_path)
    total_cal = 0
    for label in labels:
        print(label.description)
        if label.description:
            food = food_repo.search_food(Food, label.description.lower())
            if food:
                print(food.name, label.description.lower())
                total_cal += int(food.calories)
    input_data = {
        'id': helpers.generate_unique_code().__str__(),
        'image_name': file_path,
        'calories': total_cal
    }
    res = repo.store(Intake, input_data)
    return res
