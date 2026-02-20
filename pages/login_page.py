"""Login Page Object for OrangeHRM."""

from playwright.async_api import Page
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    """Page Object for OrangeHRM Login Page."""

    # Locators
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content--error"  # CSS selector (more flexible)
    PAGE_TITLE = "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']"

    async def enter_username(self, username: str):
        """Enter username."""
        await self.fill(self.USERNAME_INPUT, username)
        logger.info(f"Entered username: {username}")

    async def enter_password(self, password: str):
        """Enter password."""
        await self.fill(self.PASSWORD_INPUT, password)
        logger.info(f"Entered password")

    async def click_login(self):
        """Click login button."""
        await self.click(self.LOGIN_BUTTON)
        logger.info("Clicked login button")

    async def login(self, username: str, password: str):
        """Perform login action."""
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login()
        # Wait for navigation to complete after login
        await self.page.wait_for_load_state("networkidle")
        logger.info(f"Login performed for user: {username}")

    async def get_error_message(self) -> str:
        """Get error message if login fails."""
        error_text = await self.get_text(self.ERROR_MESSAGE)
        return error_text

    async def is_login_page_displayed(self) -> bool:
        """Check if login page is displayed."""
        return await self.is_element_visible(self.PAGE_TITLE)
