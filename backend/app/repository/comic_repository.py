from sqlalchemy import or_

from ..models.comic import Comic
import app.common.utils as utils
from flask_jwt_extended import create_access_token, jwt_required

from ..utilities.comic_utility import ComicUtilities


class ComicRepository:
    @jwt_required
    def create(self):
        response: dict = {}
        message: str = ""
        comic: Comic

        try:
            if "id" not in self:
                comic = ComicUtilities.saveComic(self)
                message = "The comic was created successfully"
            else:
                comic = ComicUtilities.updateComic(self)
                message = "The comic was updated successfully"

            response = {
                "status": 200,
                "message": message,
                "id": comic.id
            }
        except Exception as e:
            response = {
                "status": 500,
                "message": "Server error"
            }

        return response

    def filter(self):
        response: list = []
        comics = Comic.query.filter(or_(Comic.safe_title.ilike('%'+self+'%'),Comic.transcript.ilike('%'+self+'%'))).all()

        print("comics", comics)

        for i in range(len(comics)):
            comic = utils.object_as_dict(comics[i])
            response.append(comic)

        return response

    @jwt_required
    def delete(self):
        response: dict = {}
        comic = Comic.get_by_id(self)

        if comic:
            try:
                comic.delete()

                response = {
                    "status": 200,
                    "message": "The comic was deleted successfully",
                    "id": self
                }
            except Exception as e:
                response = {
                    "status": 500,
                    "message": "Server error"
                }
        else:
            response = {
                "status": 400,
                "message": "Comic with that id doesn't exists"
            }

        return response
