"""API client utility for making HTTP requests."""

import requests
from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class APIClient:
    """Reusable API client for making HTTP requests."""

    def __init__(self, base_url: str = None):
        """Initialize API client with base URL."""
        self.base_url = base_url or Config.API_BASE_URL
        self.timeout = Config.API_TIMEOUT
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def set_header(self, key: str, value: str):
        """Set custom header."""
        self.headers[key] = value
        logger.info(f"Set header: {key}")

    def set_authorization(self, token: str):
        """Set authorization token."""
        self.set_header("Authorization", f"Bearer {token}")

    def get(self, endpoint: str, params: dict = None):
        """Make GET request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(
                url, headers=self.headers, params=params, timeout=self.timeout
            )
            logger.info(f"GET {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as e:
            logger.error(f"GET request failed: {e}")
            return None

    def post(self, endpoint: str, data: dict = None, json: dict = None):
        """Make POST request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(
                url,
                headers=self.headers,
                data=data,
                json=json,
                timeout=self.timeout,
            )
            logger.info(f"POST {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as e:
            logger.error(f"POST request failed: {e}")
            return None

    def put(self, endpoint: str, data: dict = None, json: dict = None):
        """Make PUT request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(
                url,
                headers=self.headers,
                data=data,
                json=json,
                timeout=self.timeout,
            )
            logger.info(f"PUT {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as e:
            logger.error(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint: str):
        """Make DELETE request."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"DELETE {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as e:
            logger.error(f"DELETE request failed: {e}")
            return None
