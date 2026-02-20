"""Admin page class for various objects"""

from playwright.async_api import Page
import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class AdminPage(BasePage):
    """Page Object for OrangeHRM Admin Page."""

    # Locators - Update with actual selectors from your OrangeHRM admin page
    ADMIN_USER_TITLE = "//h6[contains(text(), 'Admin')]"
    SYSTEM_USER_TITLE = "//h6[contains(text(), 'System Users')]"
    USERNAME_INPUT = "//input[@placeholder='Username']"
    EMPLOYEE_NAME_INPUT = "//input[@placeholder='Employee Name']"
    STATUS_DROPDOWN = "//select[@name='status']"
    SEARCH_BUTTON = "//button[contains(text(), 'Search')]"

    async def is_admin_page_loaded(self) -> bool:
        """Check if admin page is loaded."""
        return await self.is_element_visible(self.ADMIN_USER_TITLE)

    async def search_user(self, username: str):
        """Search for a user by username."""
        await self.fill(self.USERNAME_INPUT, username)
        await self.click(self.SEARCH_BUTTON)
        await self.page.wait_for_load_state("networkidle")
        logger.info(f"Searched for user: {username}")