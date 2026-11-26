import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars

structlog.configure(processors=[
    structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level,
    structlog.processors.TimeStamper(fmt="iso"),
    structlog.processors.JSONRenderer()
])
logger = structlog.get_logger()

def check_stock():
    logger.info("stock_checked")

def process_payment():
    logger.info("payment_completed")

def save_order():
    logger.info("order_saved")

def process_order(request_id, order_id):
    clear_contextvars()
    bind_contextvars(request_id=request_id, order_id=order_id)
    try:
        logger.info("order_received")
        check_stock()
        process_payment()
        save_order()
        logger.info("order_completed")
    finally:
        clear_contextvars()

process_order("REQ-101", 1001)
process_order("REQ-102", 1002)
process_order("REQ-103", 1003)
