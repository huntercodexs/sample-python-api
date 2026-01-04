from server.apis.default_api import BaseDefaultApi
from app.service.user_service import UserService
from server.models.user import User


class UserApiImpl(BaseDefaultApi):

    def __init__(self):
        self.service = UserService()

    async def create_user(
        self,
        user: User,
    ) -> None:
        self.service.create_user(user)

    def get_users(self):
        return self.service.list_users()