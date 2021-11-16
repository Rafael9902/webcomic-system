from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id: int):
        return cls.query.get(id)

    @classmethod
    def get_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_num(cls, num: str):
        return cls.query.filter_by(num=num).first()

    @classmethod
    def filter_by(cls, query: str):
        return cls.query.filter(query)