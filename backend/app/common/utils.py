import bcrypt

salt = bcrypt.gensalt()


def encrypt(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('UTF-8'), salt)


def matchPassword(request_password: str, user_password: str) -> bool:
    return bcrypt.checkpw(request_password.encode('UTF-8'), user_password.encode())
