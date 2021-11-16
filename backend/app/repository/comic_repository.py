from flask import jsonify
from sqlalchemy import or_

from ..models.comic import Comic
import app.common.utils as utils

from ..utilities.comic_utility import ComicUtilities


class ComicRepository:
    def get(self):
        response: dict = {}
        comic = Comic.get_by_id(self)

        if not comic:
            response = {
                "status": 400,
                "message": "Comic with that id doesn't exists"
            }
        else:
            response = {
                "id": comic.id,
                "month": comic.month,
                "num": comic.num,
                "link": comic.link,
                "year": comic.year,
                "news": comic.news,
                "safe_title": comic.safe_title,
                "transcript": comic.transcript,
                "alt": comic.alt,
                "img": comic.img,
                "title": comic.title,
                "day": comic.day,
            }

        return response


    def create(self):
        response: dict = {}
        message: str = ""

        try:
            if "id" not in self:
                comic = ComicUtilities.saveComic(self)
                message = "The comic was created successfully"
            else:
                comic = ComicUtilities.updateComic(self)
                message = message = "The comic was updated successfully"

            response = {
                "status": 200,
                "message": message,
                "id": comic.id
            }
        except Exception as e:
            print(e)
            response = {
                "status": 500,
                "message": "Server error"
            }

        return response

    def filter(self):
        response: list = []
        comics = Comic.query.filter(or_(Comic.safe_title.ilike('%'+self+'%'),Comic.transcript.ilike('%'+self+'%'))).all()

        for i in range(len(comics)):
            comic = utils.object_as_dict(comics[i])
            response.append(comic)

        return response

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
                    "message": "Server error",
                    "error": e
                }
        else:
            response = {
                "status": 400,
                "message": "Comic with that id doesn't exists"
            }

        return response
