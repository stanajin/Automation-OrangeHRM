"""Configuration management for the test suite."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for test settings."""

    # Browser settings
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium")
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/")

    # Database settings
    MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "orangehrm")

    # API settings
    API_BASE_URL = os.getenv("API_BASE_URL", "https://opensource-demo.orangehrm.com/api")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 30))

    # Test data
    DEFAULT_USERNAME = "Admin"
    DEFAULT_PASSWORD = "admin123"
