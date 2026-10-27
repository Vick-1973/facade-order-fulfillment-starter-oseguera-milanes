# Order Fulfillment Facade — Starter

Small class activity for the **Facade** pattern.

The client currently coordinates four valid subsystem services directly:

- Inventory
- Payment
- Shipping
- Notification

## Your task

1. Create `OrderFulfillmentFacade.place_order(order)`.
2. Move the common coordination sequence into the Facade.
3. Do **not** modify the subsystem service classes.
4. Keep subsystem responsibilities in their existing classes.
5. Add one focused test proving the client can place an order through the Facade.
6. Be ready to name one complexity cost introduced by the Facade.

Use explicit OO design and keep one main class per source file.

## Team workflow

Only one teammate creates the repository from this template. The team repository must be **public** and everyone works in the same repository.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
