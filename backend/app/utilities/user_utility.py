from app.common import utils
from app.models.user import User


class UserUtilities:
    def createUser(self):
        password: str = str(utils.encrypt(self['password']))
        password = password[1:].replace("'", "")

        user = User(
            self['first_name'],
            self['last_name'],
            self['email'],
            password
        )

        user.save()

        return user

    def updateUser(self):
        user = User.get_by_id(self['id'])
        password: str = str(utils.encrypt(self['password']))
        password = password[1:].replace("'", "")

        user.first_name = self['first_name']
        user.last_name = self['last_name']
        user.email = self['email']
        user.password = password

        user.update()

        return user
