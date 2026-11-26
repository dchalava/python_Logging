import structlog

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger()

def process_order(order_id, quantity):
    available_stock = 10
    logger.info("order_received", order_id=order_id,
                quantity=quantity, sku="KB-101")
    if quantity > available_stock:
        logger.error("order_rejected", order_id=order_id,
                     reason="Insufficient stock",
                     available=available_stock, requested=quantity)
        return
    remaining = available_stock - quantity
    logger.info("order_created", order_id=order_id,
                remaining_stock=remaining)

process_order(101, 3)
process_order(102, 15)
