from .inventory_service import InventoryService
from .notification_service import NotificationService
from .order import Order
from .payment_service import PaymentService
from .shipping_service import ShippingService


class OrderClient:
    def __init__(self, inventory: InventoryService, payment: PaymentService, shipping: ShippingService, notification: NotificationService):
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
        self.notification = notification

    def place_order(self, order: Order) -> list[str]:
        return [
            self.inventory.reserve(order),
            self.payment.charge(order),
            self.shipping.create_shipment(order),
            self.notification.send_confirmation(order),
        ]
