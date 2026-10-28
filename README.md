# Order Fulfillment Facade

## Description

This project implements the Facade Design Pattern to simplify the order fulfillment process.

Originally, OrderClient directly coordinated four subsystem services: Inventory, Payment, Shipping, and Notification.

The goal is to move this coordination into a single Facade without modifying the existing subsystem services.

## Design Pattern: Facade

The Facade Pattern provides a simplified interface to a subsystem composed of multiple collaborating classes.

Instead of requiring the client to know every subsystem service, the client interacts with one task-oriented interface.

### Pattern Structure

The implementation contains the following components:

- **Client:** OrderClient
- **Facade:** OrderFulfillmentFacade
- **Subsystem 1:** InventoryService
- **Subsystem 2:** PaymentService
- **Subsystem 3:** ShippingService
- **Subsystem 4:** NotificationService

### Before Implementing Facade

Originally, OrderClient depended directly on four services:

1. InventoryService
2. PaymentService
3. ShippingService
4. NotificationService

The client was responsible for executing the entire order fulfillment sequence.

This introduced unnecessary coupling between the client and the subsystem.

### After Implementing Facade

OrderClient now depends only on OrderFulfillmentFacade.

The Facade coordinates all four services through one method:

    place_order(order)

The client no longer needs to know which services participate or the order in which they execute.

## Problem

The original client directly coordinated multiple services to complete an order.

The original workflow was:

1. Reserve inventory.
2. Charge payment.
3. Create shipment.
4. Send confirmation.

This approach created several problems:

- The client depended on multiple subsystem services.
- The client needed to know the correct execution order.
- Changes to the coordination sequence could affect the client.
- The client had more responsibilities than necessary.

## Solution

We implemented OrderFulfillmentFacade to centralize the common coordination sequence.

The Facade receives the four existing subsystem services through its constructor.

It exposes the following method:

    place_order(order)

This method performs the following operations:

    inventory.reserve(order)
    payment.charge(order)
    shipping.create_shipment(order)
    notification.send_confirmation(order)

Each service keeps its original responsibility.

The Facade only coordinates the execution sequence.

### Updated Client

OrderClient now receives only the Facade:

    class OrderClient:
        def __init__(self, facade):
            self.facade = facade

        def place_order(self, order):
            return self.facade.place_order(order)

This reduces coupling and keeps the client focused on requesting order fulfillment.

## Project Structure

    src/
      order_fulfillment/
        __init__.py
        order.py
        order_client.py
        order_fulfillment_facade.py
        inventory_service.py
        payment_service.py
        shipping_service.py
        notification_service.py

    tests/
      test_existing_order_flow.py
      test_order_facade.py

    README.md
    requirements.txt
    pyproject.toml

## Installation

### 1. Clone the Repository

Clone your GitHub repository:

    git clone https://github.com/YOUR-USERNAME/facade-order-fulfillment-activity.git

Navigate to the project folder:

    cd facade-order-fulfillment-activity

Replace YOUR-USERNAME with your actual GitHub username and adjust the repository name if necessary.

### 2. Create a Virtual Environment

Run:

    python -m venv .venv

### 3. Activate the Virtual Environment

On Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

On macOS/Linux:

    source .venv/bin/activate

### 4. Install Dependencies

Run:

    python -m pip install -r requirements.txt

## Running Tests

The project includes two tests to verify the Facade implementation.

### Test 1: Existing Order Flow

Run:

    python -m pytest tests/test_existing_order_flow.py -v

This test verifies that the original order fulfillment behavior is preserved after introducing the Facade.

### Test 2: Facade Integration Test

Run:

    python -m pytest tests/test_order_facade.py -v

This test verifies that OrderClient can place an order through OrderFulfillmentFacade.

### Run All Tests

Execute:

    python -m pytest -q

Expected result when both tests pass:

    2 passed

Both tests should pass without modifying the original subsystem service classes.

## Test Explanation

The tests follow the Arrange, Act, Assert testing structure.

### Test 1: Existing Order Flow

**File:** tests/test_existing_order_flow.py

The original test was updated to use OrderFulfillmentFacade instead of passing four individual services directly to OrderClient.

#### Arrange

Create the subsystem services:

    inventory = InventoryService()
    payment = PaymentService()
    shipping = ShippingService()
    notification = NotificationService()

Create the Facade:

    facade = OrderFulfillmentFacade(
        inventory,
        payment,
        shipping,
        notification
    )

Create the client:

    client = OrderClient(facade)

Create the order:

    order = Order("O-1", "SKU-9", 125.0, "Guadalajara")

#### Act

Place the order through the Facade:

    steps = client.place_order(order)

#### Assert

Verify the expected results:

    inventory:reserved:SKU-9
    payment:charged:125.00
    shipping:created:Guadalajara
    notification:sent:O-1

This test confirms that the original workflow remains functional after the refactoring.

### Test 2: Facade Integration Test

**File:** tests/test_order_facade.py

This new test verifies that OrderClient can place an order through the Facade.

#### Test Order

- Order ID: ORD-001
- SKU: ITEM-123
- Amount: 249.99
- Address: Guadalajara, Jalisco

#### Expected Results

    inventory:reserved:ITEM-123
    payment:charged:249.99
    shipping:created:Guadalajara, Jalisco
    notification:sent:ORD-001

The test verifies that:

1. The Facade receives the required subsystem services.
2. OrderClient depends only on the Facade.
3. The order is placed through the Facade.
4. All four subsystem operations are executed.
5. The returned results preserve the correct execution order.

## Design Explanation

### What is the Facade?

OrderFulfillmentFacade is a simplified entry point that coordinates the existing subsystem services.

It allows OrderClient to place an order through a single method instead of interacting directly with multiple services.

### What knowledge was removed from the client?

OrderClient no longer needs to know:

- Which subsystem services participate.
- Which methods belong to each service.
- The correct execution order.
- How the services collaborate to fulfill an order.

This knowledge is now centralized inside OrderFulfillmentFacade.

### What responsibilities remain inside the services?

Each subsystem maintains its original responsibility.

**InventoryService**

Responsible for reserving inventory.

**PaymentService**

Responsible for processing payments.

**ShippingService**

Responsible for creating shipments.

**NotificationService**

Responsible for sending order confirmations.

The Facade does not implement these responsibilities.

It only coordinates the services.

### Why use composition?

The Facade contains references to the existing subsystem services.

This allows it to delegate operations without modifying their implementations.

Composition also keeps the subsystem services independent from the Facade.

### Why is this a Facade and not an Adapter?

An Adapter solves interface incompatibility by translating one interface into another.

A Facade simplifies interactions with an existing subsystem.

In this project, the subsystem services already provide compatible operations.

The problem is that OrderClient needs to coordinate too many services directly.

Therefore, the Facade Pattern is the appropriate solution.

### What complexity cost does the Facade introduce?

The Facade introduces an additional class and abstraction that developers must understand and maintain.

If the order fulfillment workflow changes, the coordination logic inside OrderFulfillmentFacade may also require modifications and additional testing.

Another potential risk is that the Facade could become a God Object if it starts implementing responsibilities that belong to individual subsystem services.

However, the added abstraction is justified because it reduces client coupling and simplifies the order fulfillment process.

### What would make the Facade a God Object?

The Facade would become a God Object if it started implementing inventory management, payment processing, shipping calculations, and notification logic directly.

To avoid this problem, the Facade should only coordinate existing services.

## Benefits of the Implementation

The implementation provides several benefits:

1. **Reduced Coupling:** OrderClient depends on one Facade instead of four services.

2. **Separation of Concerns:** Each subsystem service keeps its original responsibility.

3. **Improved Maintainability:** The coordination sequence is centralized in one class.

4. **Simplified Client:** OrderClient only needs to call place_order(order).

5. **Code Reusability:** Existing subsystem services can continue being used independently.

6. **Better Testability:** The order fulfillment workflow can be tested through a single entry point.

## Changes Made

The following changes were implemented:

### New Files

**order_fulfillment_facade.py**

Introduces OrderFulfillmentFacade and its place_order(order) method.

**test_order_facade.py**

Adds a focused test proving that OrderClient can place an order through the Facade.

### Modified Files

**order_client.py**

Removes direct dependencies on InventoryService, PaymentService, ShippingService, and NotificationService.

The client now depends only on OrderFulfillmentFacade.

**test_existing_order_flow.py**

Updates the original test to instantiate the Facade before creating OrderClient.

The test continues verifying that the original workflow produces the expected results.

### Unchanged Files

The following subsystem classes remain unchanged:

- inventory_service.py
- payment_service.py
- shipping_service.py
- notification_service.py
- order.py

## Requirements Checklist

- [x] OrderFulfillmentFacade implemented
- [x] place_order(order) implemented
- [x] Coordination moved into the Facade
- [x] OrderClient depends on the Facade
- [x] Original subsystem services remain unchanged
- [x] Subsystem responsibilities preserved
- [x] Original test updated
- [x] Focused Facade test added
- [x] Design explanation included
- [x] Complexity cost explained

## Conclusion

The Facade Design Pattern successfully simplifies the order fulfillment process by introducing a single entry point for coordinating multiple subsystem services.

OrderClient now interacts with OrderFulfillmentFacade instead of directly managing Inventory, Payment, Shipping, and Notification services.

The original subsystem responsibilities remain unchanged, while the common coordination sequence is centralized inside the Facade.

The updated original test and the new focused test verify that the order fulfillment workflow remains functional through the simplified client interface.

This implementation demonstrates how the Facade Pattern reduces coupling, improves separation of concerns, and simplifies client interactions without replacing existing subsystem functionality.z