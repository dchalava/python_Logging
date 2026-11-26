def process_order(order_id, quantity):
    available_stock = 10
    print("Order received:", order_id)
    print("Checking stock")
    if quantity > available_stock:
        print("Insufficient stock")
        return
    remaining = available_stock - quantity
    print("Order created successfully")
    print("Remaining stock:", remaining)

process_order(101, 3)
process_order(102, 5)
