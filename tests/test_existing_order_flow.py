from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order import Order
from order_fulfillment.order_client import OrderClient
from order_fulfillment.order_fulfillment_facade import OrderFulfillmentFacade
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService


def test_existing_client_places_order_through_facade():
    # Arrange: Create the subsystem services
    inventory = InventoryService()
    payment = PaymentService()
    shipping = ShippingService()
    notification = NotificationService()

    # Create the Facade
    facade = OrderFulfillmentFacade(
        inventory,
        payment,
        shipping,
        notification
    )

    # The client only depends on the Facade
    client = OrderClient(facade)

    # Create an order
    order = Order("O-1", "SKU-9", 125.0, "Guadalajara")

    # Act: Place the order through the Facade
    steps = client.place_order(order)

    # Assert: Verify the original workflow
    assert len(steps) == 4
    assert steps[0] == "inventory:reserved:SKU-9"
    assert steps[1] == "payment:charged:125.00"
    assert steps[2] == "shipping:created:Guadalajara"
    assert steps[3] == "notification:sent:O-1"

