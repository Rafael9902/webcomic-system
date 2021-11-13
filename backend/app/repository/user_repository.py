import json

from flask import jsonify
from sqlalchemy.exc import IntegrityError

from ..models.user import User


class UserRepository:

    def get(self) -> dict:
        user: dict = {}
        user = User.get_by_id(self)

        user = {
            'id' : user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }

        return user

    def create(self):
        response: dict = {}

        try:

            validate_user: User = User.get_by_email(self['email'])

            if validate_user:
                response = {
                    "status": 400,
                    "message": "User with that email already exists"
                }
            else:
                user = User(
                    self['first_name'],
                    self['last_name'],
                    self['email'],
                    self['password']
                )

                user.save()

                response = {
                    "status": 200,
                    "message": "The user was created successfully",
                    "id": user.id
                }
        except Exception as e:
            user.rollback()

            response = {
                "status": 500,
                "message": "Server error"
            }

        return response

    def update(self):
        response: dict = {}

        try:
            validate_user: User = User.get_by_email(self['email'])

            if validate_user:
                response = {
                    "status": 400,
                    "message": "User with that email already exists"
                }
            else:
                user = User.get_by_id(self['id'])

                user.first_name = self['first_name']
                user.last_name = self['last_name']
                user.email = self['email']
                user.password = self['password']

                user.update()

                response = {
                    "status": 200,
                    "message": "The user was updated successfully",
                    "id": user.id
                }
        except Exception as e:
            response = {
                "status": 400,
                "message": "Failed to update the user"
            }

        return response
