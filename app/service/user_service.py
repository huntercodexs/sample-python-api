from app.repository.user_repository import UserRepository

class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, user):
        return self.repository.create(user)

    def list_users(self):
        return self.repository.find_all()

    def get_user(self, user_id):
        return self.repository.find_by_id(user_id)

    def update_user(self, user_id, data):
        self.repository.update(user_id, data)

    def delete_user(self, user_id):
        self.repository.delete(user_id)
