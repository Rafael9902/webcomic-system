from flask import request, Blueprint, jsonify
from flask_restful import Api, Resource
from ..repository.user_repository import UserRepository
from ..models.user import User

user_api = Blueprint('user_api', __name__)
api = Api(user_api)


class UserResource(Resource):
    def get(self, id: int):
        try:
            user = UserRepository.get(id)
            return user
        except Exception as e:
            return {
                "status": 500,
                "message": "Server error"
            }


class UserResourceList(Resource):
    def get(self):
        user = UserRepository.getAll(self)
        return user, 200

    def put(self):
        request_json = request.get_json(silent=True)
        user = UserRepository.update(request_json)
        return user, 200

    def post(self):
        request_json = request.get_json(silent=True)

        try:
            user = UserRepository.create(request_json)
            return user, 200
        except Exception as e:
            return {
                "status": 500,
                "message": "Server error"
            }


api.add_resource(UserResourceList, '/user', endpoint='user')
api.add_resource(UserResource, '/user/<int:id>', endpoint='user_get')
