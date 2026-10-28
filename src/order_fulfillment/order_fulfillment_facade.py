from .inventory_service import InventoryService
from .payment_service import PaymentService
from .shipping_service import ShippingService
from .notification_service import NotificationService
from .order import Order


class OrderFulfillmentFacade:
    def __init__(
        self,
        inventory: InventoryService,
        payment: PaymentService,
        shipping: ShippingService,
        notification: NotificationService,
    ):
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
        self.notification = notification

    def place_order(self, order: Order) -> list[str]:
        # Step 1: Reserve inventory
        # Step 2: Charge payment
        # Step 3: Create shipment
        # Step 4: Send confirmation
        return [
            self.inventory.reserve(order),
            self.payment.charge(order),
            self.shipping.create_shipment(order),
            self.notification.send_confirmation(order),
        ]
