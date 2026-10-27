from .order import Order


class PaymentService:
    def charge(self, order: Order) -> str:
        return f"payment:charged:{order.amount:.2f}"
