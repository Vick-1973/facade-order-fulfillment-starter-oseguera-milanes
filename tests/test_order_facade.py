from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order_fulfillment_facade import OrderFulfillmentFacade
from order_fulfillment.order_client import OrderClient
from order_fulfillment.order import Order


def test_client_places_order_using_facade():
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
        notification,
    )

    # Create a client that depends only on the Facade
    client = OrderClient(facade)

    # Create a sample order
    order = Order(
        order_id="ORD-001",
        sku="ITEM-123",
        amount=249.99,
        address="Guadalajara, Jalisco",
    )

    # Act: Place the order through the Facade
    result = client.place_order(order)

    # Assert: Verify the complete workflow
    assert result == [
        "inventory:reserved:ITEM-123",
        "payment:charged:249.99",
        "shipping:created:Guadalajara, Jalisco",
        "notification:sent:ORD-001",
    ]
