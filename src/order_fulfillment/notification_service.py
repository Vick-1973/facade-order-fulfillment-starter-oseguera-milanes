from .order import Order


class NotificationService:
    def send_confirmation(self, order: Order) -> str:
        return f"notification:sent:{order.order_id}"
