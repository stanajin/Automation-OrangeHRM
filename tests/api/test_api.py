"""API Tests for OrangeHRM."""

import pytest
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.api
class TestAPIEndpoints:
    """Test API endpoints."""

    def test_api_connection(self, api_client):
        """Test API client can be instantiated."""
        assert api_client is not None
        assert api_client.base_url is not None
        logger.info("✓ API connection test passed")

    def test_api_headers_setup(self, api_client):
        """Test API headers are properly set."""
        assert "Content-Type" in api_client.headers
        assert "Accept" in api_client.headers
        logger.info("✓ API headers setup test passed")

    def test_set_custom_header(self, api_client):
        """Test setting custom header."""
        api_client.set_header("X-Custom", "test-value")
        assert api_client.headers["X-Custom"] == "test-value"
        logger.info("✓ Set custom header test passed")

    def test_set_authorization(self, api_client):
        """Test setting authorization token."""
        token = "test-token-123"
        api_client.set_authorization(token)
        assert api_client.headers["Authorization"] == f"Bearer {token}"
        logger.info("✓ Set authorization test passed")
