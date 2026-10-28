from .order import Order
from .order_fulfillment_facade import OrderFulfillmentFacade


class OrderClient:
    def __init__(self, facade: OrderFulfillmentFacade):
        self.facade = facade

    def place_order(self, order: Order) -> list[str]:
        return self.facade.place_order(order)

