from flask import Flask, render_template, redirect, flash, url_for, session
from models import User, UserToken
from Auth.AuthRepository import AuthRepository, UserTokenRepository
import helpers
import datetime
import models
from Auth.AuthValidator import create_user_rule


def create_user(data):
    create_user_rule(data)
    repo = AuthRepository()
    inputs = {
        'id': helpers.generate_unique_code().__str__(),
        'email': data['email'],
        'age': str(data['age']),
        'weight': str(data['weight']),
        'height': str(data['height']),
        'activity': data['activity'],
        'gendar': data['gendar'],
        'password': helpers.hash_password(data['password']),
        'name': data['name'],
    }
    user = repo.store(User, inputs)
    return user


def legacy_login_api(data):
    repo = AuthRepository()
    tokenRepo = UserTokenRepository()
    userObj = repo.filter_attribute(User, {'email': data['email']})
    if hasattr(userObj, 'email'):
        isValid = helpers.validate_hash_password(data['password'], userObj.password)
        if isValid:
            token = helpers.access_token()
            return tokenRepo.store(UserToken,
                                   {
                                       'token': token,
                                       'user_id': userObj.id
                                   })


def logout(token):
    tokenRepo = UserTokenRepository()
    return tokenRepo.deleteToken(UserToken, token)
