import bcrypt
from sqlalchemy import inspect

salt = bcrypt.gensalt()


def encrypt(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('UTF-8'), salt)


def matchPassword(request_password: str, user_password: str) -> bool:
    return bcrypt.checkpw(request_password.encode('UTF-8'), user_password.encode())


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
