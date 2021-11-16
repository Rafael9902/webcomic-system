import json

from sqlalchemy import Sequence

from app.db import db, BaseModelMixin

USER_ID_SEQ = Sequence('user_id_seq')


class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, USER_ID_SEQ, primary_key=True, autoincrement=True,
                   server_default=USER_ID_SEQ.next_value())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
