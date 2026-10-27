from .order import Order


class InventoryService:
    def reserve(self, order: Order) -> str:
        return f"inventory:reserved:{order.sku}"
