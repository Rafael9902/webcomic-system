from ..models.comic import Comic
import app.common.utils as utils
from flask_jwt_extended import create_access_token
from ..utilities.comic_utility import ComicUtilities


class ComicRepository:
    def create(self):
        response: dict = {}
        message: str = ""
        comic: Comic

        try:
            if len(self) == 11:
                comic = ComicUtilities.saveComic(self)
                message = "The comic was created successfully"
            elif len(self) == 12:
                comic = ComicUtilities.updateComic(self)
                message = "The comic was updated successfully"

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
