import logging
import os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/application.log"),
    ]
)
logger = logging.getLogger("CommerceHub")
logger.info("Application started")
logger.info("Order 101 received")
logger.warning("Product stock is low")
logger.error("Payment processing failed")
logger.info("Application completed")
