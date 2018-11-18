from flask import Flask, session, redirect, request
from Exceptions.ExceptionHandler import FoodException
from Auth.AuthRepository import UserTokenRepository
from models import User
import jwt


def api_login_required(func):
    def wraps(*args, **kwargs):
        if request.headers.has_key('access-token'):
            repo = UserTokenRepository()
            token = request.headers['access-token']
            tokenObj = repo.check_valid_token(UserToken, token)
            if hasattr(tokenObj, 'token'):
                return func(*args, **kwargs)
        raise FoodException('Unauthorized request', 401)
    wraps.func_name = func.func_name
    return wraps


def validate_jwt_token(func):
    def wraps(*args, **kwargs):
        if request.headers.has_key('app-token'):
            token = request.headers['app-token']
            payload = jwt.decode(token, 'feed_engine', algorithm='HS256')
            app = AppRepository().get_by_slug(App, payload['app_name'])
            if app:
                request.__setattr__('app', app.transform())
                return func(*args, **kwargs)
        raise FoodException('Unauthorized request', 401)
    wraps.func_name = func.func_name
    return wraps
