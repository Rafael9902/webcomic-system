from app.models.comic import Comic


class ComicUtilities:
    def saveComic(self):
        comic = Comic(
            self['month'],
            self['num'],
            self['link'],
            self['year'],
            self['news'],
            self['safe_title'],
            self['transcript'],
            self['alt'],
            self['img'],
            self['title'],
            self['day'],
        )

        comic.save()

        return comic

    def updateComic(self):
        comic = Comic.get_by_id(self['id'])

        if comic:
            comic.month = self['month'],
            comic.num = self['num'],
            comic.link = self['link'],
            comic.year = self['year'],
            comic.news = self['news'],
            comic.safe_title = self['safe_title'],
            comic.transcript = self['transcript'],
            comic.alt = self['alt'],
            comic.img = self['img'],
            comic.title = self['title'],
            comic.day = self['day']

            comic.update()

            return comic
