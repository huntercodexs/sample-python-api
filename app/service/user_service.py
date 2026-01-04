from app.config.settings import settings
from app.integration.order_client import OrderClient
from app.repository.user_repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()
        self.order_client = OrderClient(settings.order_service_url)

    def create_user(self, user):
        self.create_user_and_order("100", "2")
        return self.repository.create(user)

    def list_users(self):
        return self.repository.find_all()

    def get_user(self, user_id):
        return self.repository.find_by_id(user_id)

    def update_user(self, user_id, data):
        self.repository.update(user_id, data)

    def delete_user(self, user_id):
        self.repository.delete(user_id)

    def create_user_and_order(self, price: str, quantity: str):
        # business logic here

        print(">>>creating user and order for tests")

        try:
            self.order_client.create_order(
                price=price,
                quantity=quantity
            )
        except Exception as e:
            print(e)
