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

        return comic

    def get(self):
        tag: str = request.args.get("tag")
        comics = ComicRepository.filter(tag)

        return comics


class ComicResourceList(Resource):
    def delete(self, id: int):
        comic = ComicRepository.delete(id)
        return comic


api.add_resource(ComicResource, '/comic', endpoint='comic')
api.add_resource(ComicResourceList, '/comic/<int:id>', endpoint='comic_delete')
