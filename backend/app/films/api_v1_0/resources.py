from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import FilmSchema
from ...models.user import User
from ...models.comic import Comic
from ...common.error_handling import ObjectNotFound

films_v1_0_bp = Blueprint('films_v1_0_bp', __name__)

film_schema = FilmSchema()

api = Api(films_v1_0_bp)


def get(film_id):
    film = User.get_by_id(film_id)
    if film is None:
        raise ObjectNotFound('La película no existe')
    resp = film_schema.dump(film)
    return resp


class FilmResource(Resource):
    def get(self, film_id):
        film = User.get_by_id(film_id)
        resp = film_schema.dump(film)
        return resp


# api.add_resource(FilmListResource, '/api/v1.0/films/', endpoint='film_list_resource')
api.add_resource(FilmResource, '/api/v1.0/films/<int:film_id>', endpoint='film_resource')
