"""
This module is used to populate database with initial data
"""
import logging

from app.db.init_db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    """
    This function runs db initialization
    :return:
    """
    init_db()


def main() -> None:
    """
    This function runs init function in module
    :return:
    """
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
