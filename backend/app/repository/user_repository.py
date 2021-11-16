from flask import jsonify

from ..models.user import User
import app.common.utils as utils
from flask_jwt_extended import create_access_token

from ..utilities.user_utility import UserUtilities


class UserRepository:

    def get(self) -> dict:
        response: dict = {}
        user = User.get_by_id(self)

        if not user:
            response = {
                "status": 400,
                "message": "User with that id doesn't exists"
            }
        else:
            response = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }

        return response

    def create(self):
        response: dict = {}
        message: str = ""

        try:
            if "id" not in self:
                validate_user: User = User.get_by_email(self['email'])

                if validate_user:
                    response = {
                        "status": 400,
                        "message": "User with that email already exists"
                    }
                else:
                    user = UserUtilities.createUser(self)
                    message = "The user was created successfully"
            else:
                user = UserUtilities.updateUser(self)
                message = message = "The user was updated successfully"

            response = {
                "status": 200,
                "message": message,
                "id": user.id
            }

        except Exception as e:
            print(e)
            response = {
                "status": 500,
                "message": "Server error"
            }

        return response

    def login(self):
        response: dict = {}

        try:
            user = User.get_by_email(self['email'])

            if not user or not utils.matchPassword(self['password'], user.password):
                response = {
                    "status": 401,
                    "message": "Please check your credentials"
                }
            else:
                access_token: str = create_access_token(identity=user.id)

                response = {
                    "status": 200,
                    "message": "User logged in successfully",
                    "token": access_token
                }
        except Exception as e:
            response = {
                "status": 500,
                "message": "Server error",
                "error": e
            }

        return response

    def logout(self):
        return {
            "status": "200",
            "message": "User logged out successfully"
        }
