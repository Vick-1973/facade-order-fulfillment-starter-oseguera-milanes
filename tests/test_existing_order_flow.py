from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order import Order
from order_fulfillment.order_client import OrderClient
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService


def test_existing_client_coordinates_all_services():
    client = OrderClient(InventoryService(), PaymentService(), ShippingService(), NotificationService())
    order = Order("O-1", "SKU-9", 125.0, "Guadalajara")
    steps = client.place_order(order)
    assert len(steps) == 4
    assert steps[0] == "inventory:reserved:SKU-9"
    assert steps[-1] == "notification:sent:O-1"
