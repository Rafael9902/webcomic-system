from ..models.user import User


class UserRepository:

    @staticmethod
    def get(id: str) -> dict:
        """ Query a user by username """
        user: dict = {}
        user = User.query.filter_by(id=id).first_or_404()
        user = {
            'user': user.first_name
        }
        return user
