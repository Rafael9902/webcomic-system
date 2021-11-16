from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Api, Resource
from ..repository.comic_repository import ComicRepository

comic_api = Blueprint('comic_api', __name__)
api = Api(comic_api)


class ComicResource(Resource):
    def post(self):
        request_json = request.get_json(silent=True)
        comic = ComicRepository.create(request_json)
        return comic, 200


api.add_resource(ComicResource, '/comic', endpoint='comic')
