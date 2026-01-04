from client_order.api.default_api import DefaultApi
from client_order.api_client import ApiClient
from client_order.configuration import Configuration
from client_order.models.order import Order


class OrderClient:

    def __init__(self, base_url: str):
        config = Configuration(
            host=base_url
        )
        self.api = DefaultApi(ApiClient(configuration=config))

    def create_order(self, price: str, quantity: str) -> None:
        order = Order(
            price=price,
            quantity=quantity
        )
        self.api.create_order(order)