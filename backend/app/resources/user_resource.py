from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Api, Resource
from ..repository.user_repository import UserRepository

user_api = Blueprint('user_api', __name__)
api = Api(user_api)


class UserResource(Resource):
    @jwt_required
    def get(self):
        current_user_id = get_jwt_identity()
        user = UserRepository.get(current_user_id)

        return user

    def post(self):
        request_json = request.get_json(silent=True)
        user = UserRepository.create(request_json)

        return user


class UserResourceList(Resource):
    def get(self, id: int):
        user = UserRepository.get(id)

        return user


class UserResourceLogin(Resource):
    def post(self):
        request_json = request.get_json(silent=True)
        authenticated = UserRepository.login(request_json)

        return authenticated


class UserResourceLogout(Resource):
    def post(self):
        logout = UserRepository.logout()

        return logout


api.add_resource(UserResource, '/user', endpoint='user')
api.add_resource(UserResourceList, '/user/<int:id>', endpoint='user_list')
api.add_resource(UserResourceLogin, '/user/login', endpoint='user_login')
api.add_resource(UserResourceLogin, '/user/logout', endpoint='user_logout')
