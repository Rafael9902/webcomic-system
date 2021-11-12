from marshmallow import fields
from app.ext import ma


class UserSchema(ma.Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String()
    last_name = fields.Integer()
    email = fields.Integer()
    password = fields.String()
