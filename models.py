from flask import Flask, json, jsonify
from datetime import datetime, timedelta
from __init__ import db
from sqlalchemy import text, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import ARRAY, array
from helpers import datetime_to_epoch
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.associationproxy import association_proxy


def expires_at():
    return datetime.utcnow() + timedelta(days=7)


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.String)
    height = db.Column(db.String, nullable=True)
    gendar = db.Column(db.String, nullable=True)
    activity = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def transform(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': int(self.age),
            'weight': float(self.weight),
            'height': float(self.height),
            'gendar': self.gendar,
            'activity': self.activity,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class UserToken(db.Model):
    __tablename__ = 'user_tokens'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(u'users.id', ondelete=u'CASCADE'), nullable=False)
    token = db.Column(db.String(100), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False,  default=expires_at)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    user = relationship(u'User')

    def transform(self):
        return {
            'id': self.id,
            'token': self.token,
            'expiresAt': datetime_to_epoch(self.expires_at),
            'user': self.user.transform()
        }


class intake(db.Model):
    __tablename__ = 'Intakes'

    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.ForeignKey(u'users.id', ondelete=u'CASCADE'), nullable=False)
    image_name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.String)

    user = relationship(u'User')

    def transform(self):
        return {
            'id': self.id,
            'image_name': self.image_name,
            'calories': self.calories,
            'user': self.user.transform()
        }


class Food(db.Model):
    __tablename__ = 'Foods'

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.String(100), nullable=False)

    def transform(self):
        return {
            'id': self.id,
            'name': self.name,
            'calories': self.calories,
        }
