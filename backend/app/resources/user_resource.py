from flask import request, Blueprint
from flask_restful import Api, Resource

from ..schemas.user_schema import UserSchema
from ..models.user import User
from ..repository.user_repository import UserRepository

user_api = Blueprint('user_api', __name__)

api = Api(user_api)


class UserResource(Resource):
    def get(self, id: str):
        id = str(id)
        user = UserRepository.get(id)
        return user, 200


