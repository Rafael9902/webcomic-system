from app.db import db, BaseModelMixin


class Comic(db.Model, BaseModelMixin):
    id = db.Column(db.String(50), nullable=False)
    month = db.Column(db.String(2), nullable=False)
    num = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    link = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(50), nullable=False)
    news = db.Column(db.String(50))
    safe_title = db.Column(db.String(50), nullable=False)
    transcript = db.Column(db.String(100), nullable=False)
    alt = db.Column(db.String(50), nullable=False)
    img = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    day = db.Column(db.String(50), nullable=False)

    def __init__(self, month, link, year, news, safe_title, transcript, alt, img, title, day):
        self.month = month
        self.link = link
        self.year = year
        self.news = news
        self.safe_title = safe_title
        self.transcript = transcript
        self.alt = alt
        self.img = img
        self.title = title
        self.day = day
