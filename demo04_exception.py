import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)
logger = logging.getLogger("CommerceHub")

def calculate_unit_price(total_amount, quantity):
    return total_amount / quantity

def process_order():
    try:
        logger.info("Calculating unit price")
        price = calculate_unit_price(1000, 0)
        logger.info("Unit price: %s", price)
    except ZeroDivisionError:
        logger.exception("Price calculation failed")
        raise

process_order()
logger.info("Application continues")
