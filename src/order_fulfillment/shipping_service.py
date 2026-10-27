from .order import Order


class ShippingService:
    def create_shipment(self, order: Order) -> str:
        return f"shipping:created:{order.address}"
