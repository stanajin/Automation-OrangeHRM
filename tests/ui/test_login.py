"""UI Tests for OrangeHRM Login functionality."""

import pytest
from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.ui
@pytest.mark.asyncio
class TestLogin:
    """Test login functionality using Page Object Model."""

    async def test_successful_login(self, page, login_page):
        """Test successful login with valid credentials."""
        await page.goto(Config.BASE_URL)
        await login_page.login(Config.DEFAULT_USERNAME, Config.DEFAULT_PASSWORD)
        
        # Verify redirect to dashboard
        await page.wait_for_load_state("networkidle")
        assert "/dashboard/index" in page.url
        logger.info("✓ Successful login test passed")

    async def test_login_page_displayed(self, page, login_page):
        """Test that login page is displayed correctly."""
        await page.goto(Config.BASE_URL)
        is_displayed = await login_page.is_login_page_displayed()
        
        assert is_displayed
        logger.info("✓ Login page displayed test passed")

    async def test_invalid_credentials(self, page, login_page):
        """Test login with invalid credentials."""
        await page.goto(Config.BASE_URL)
        await login_page.login("InvalidUser", "InvalidPassword")
        
        # Verify error message appears
        await page.wait_for_load_state("networkidle")
        error_message = await login_page.get_error_message()
        
        assert error_message is not None
        assert "Invalid" in error_message or "credentials" in error_message.lower()
        logger.info("✓ Invalid credentials test passed")

    async def test_empty_username(self, page, login_page):
        """Test login with empty username."""
        await page.goto(Config.BASE_URL)
        await login_page.enter_password(Config.DEFAULT_PASSWORD)
        await login_page.click_login()
        
        # Verify still on login page
        assert "/login" in page.url
        logger.info("✓ Empty username test passed")
