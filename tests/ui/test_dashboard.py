"""UI Tests for OrangeHRM Dashboard functionality."""

import pytest
from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.ui
@pytest.mark.asyncio
class TestDashboard:
    """Test dashboard functionality using Page Object Model."""

    async def test_dashboard_loads_after_login(self, authenticated_dashboard):
        """Test that dashboard loads successfully after login."""
        is_loaded = await authenticated_dashboard.is_dashboard_loaded()
        assert is_loaded
        logger.info("✓ Dashboard loads after login test passed")

    async def test_logout_functionality(self, authenticated_page, authenticated_dashboard):
        """Test logout functionality."""
        await authenticated_dashboard.logout()
        
        # Verify redirect to login page
        await authenticated_page.wait_for_load_state("networkidle")
        assert "/login" in authenticated_page.url
        logger.info("✓ Logout test passed")

    async def test_dashboard_page_title(self, authenticated_dashboard):
        """Test dashboard page title."""
        title = await authenticated_dashboard.get_page_title()
        
        assert "Dashboard" in title or "OrangeHRM" in title
        logger.info(f"✓ Dashboard page title test passed - Title: {title}")

    async def test_dashboard_url(self, authenticated_page, authenticated_dashboard):
        """Test dashboard URL."""
        url = await authenticated_dashboard.get_page_url()
        
        assert "dashboard" in url.lower()
        logger.info(f"✓ Dashboard URL test passed - URL: {url}")
