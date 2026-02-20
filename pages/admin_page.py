"""Admin page class for various objects"""

from playwright.async_api import Page
import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class AdminPage(BasePage):
    """Page Object for OrangeHRM Admin Page."""

    # Locators - From inspector findings
    ADMIN_USER_TITLE = "h6.oxd-topbar-header-breadcrumb-module"
    SYSTEM_USER_TITLE = "//h6[contains(text(), 'System Users')]"
    #USERNAME_INPUT = "[role='textbox'] >> nth=1"  # 2nd textbox on admin page
    EMPLOYEE_NAME_INPUT = "[role='textbox'] >> nth=0"  # 1st textbox
    STATUS_DROPDOWN = "//select[@name='status']"
    SEARCH_BUTTON = "button:has-text('Search')"  # Button with "Search" text
    # In admin_page.py
    USERNAME_INPUT = 'input[role="textbox"]'  # CSS selector
    

    async def is_admin_page_loaded(self) -> bool:
        """Check if admin page is loaded."""
        return await self.is_element_visible(self.ADMIN_USER_TITLE)

    async def search_user(self, username: str):
        """Search for a user by username."""
        # Use get_by_role for nth selector support
        textbox = self.page.get_by_role("textbox").nth(1)
        await textbox.click()
        await textbox.fill(username)
        
        # Click search button
        await self.page.get_by_role("button", name="Search").click()
        await self.page.wait_for_load_state("networkidle")
        logger.info(f"Searched for user: {username}")