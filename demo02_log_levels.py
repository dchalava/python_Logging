import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("CommerceHub")

def process_order(order_id, quantity):
    available_stock = 10
    logger.info("Order received: %s", order_id)
    logger.debug("Available: %s, Requested: %s",
                 available_stock, quantity)
    if quantity > available_stock:
        logger.error("Order %s rejected: Insufficient stock", order_id)
        return
    remaining = available_stock - quantity
    if remaining < 5:
        logger.warning("Low stock: %s items remaining", remaining)
    logger.info("Order %s created successfully", order_id)

process_order(101, 3)
process_order(102, 8)
process_order(103, 15)
logger.critical("Simulated database unavailable")
