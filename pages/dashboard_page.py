"""Dashboard Page Object for OrangeHRM."""

from playwright.async_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class DashboardPage(BasePage):
    """Page Object for OrangeHRM Dashboard Page."""

    # Locators
    DASHBOARD_TITLE = "h6.oxd-topbar-header-breadcrumb-module:has-text('Dashboard')"
    USER_PROFILE_DROPDOWN = "//img[@class='oxd-userdropdown-img']"
    LOGOUT_BUTTON = "//a[@href='/web/index.php/auth/logout']"
    QUICK_LAUNCH_MENU = "//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']"
    WELCOME_MESSAGE = "//h6[contains(text(), 'Welcome')]"

    async def is_dashboard_loaded(self) -> bool:
        """Check if dashboard is loaded."""
        return await self.is_element_visible(self.DASHBOARD_TITLE)

    async def click_user_profile(self):
        """Click on user profile dropdown."""
        await self.click(self.USER_PROFILE_DROPDOWN)
        logger.info("Clicked user profile dropdown")

    async def click_logout(self):
        """Click on logout button."""
        await self.click(self.LOGOUT_BUTTON)
        logger.info("Clicked logout button")

    async def logout(self):
        """Perform logout action."""
        await self.click_user_profile()
        await self.click_logout()
        logger.info("Logged out")

    async def get_welcome_message(self) -> str:
        """Get welcome message."""
        welcome = await self.get_text(self.WELCOME_MESSAGE)
        return welcome

    async def get_page_title(self) -> str:
        """Get dashboard page title."""
        return await super().get_page_title()
