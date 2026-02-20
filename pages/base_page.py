"""Base Page class with common page methods."""

from playwright.async_api import Page, Locator
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class with common methods for all pages."""

    def __init__(self, page: Page):
        """Initialize base page with Playwright page object."""
        self.page = page

    async def navigate_to(self, url: str):
        """Navigate to a specific URL."""
        await self.page.goto(url)
        logger.info(f"Navigated to {url}")

    async def click(self, locator: str):
        """Click on an element."""
        await self.page.click(locator)
        logger.info(f"Clicked on {locator}")

    async def fill(self, locator: str, text: str):
        """Fill in text input."""
        await self.page.fill(locator, text)
        logger.info(f"Filled {locator} with {text}")

    async def get_text(self, locator: str) -> str:
        """Get text from an element."""
        text = await self.page.text_content(locator)
        logger.info(f"Got text from {locator}: {text}")
        return text

    async def wait_for_element(self, locator: str, timeout: int = 5000):
        """Wait for element to be visible."""
        await self.page.wait_for_selector(locator, timeout=timeout)
        logger.info(f"Element {locator} is visible")

    async def is_element_visible(self, locator: str) -> bool:
        """Check if element is visible."""
        try:
            await self.wait_for_element(locator, timeout=2000)
            return True
        except:
            return False

    async def take_screenshot(self, filename: str):
        """Take screenshot of the page."""
        await self.page.screenshot(path=f"reports/screenshots/{filename}.png")
        logger.info(f"Screenshot saved as {filename}")

    async def get_page_title(self) -> str:
        """Get page title."""
        title = await self.page.title()
        logger.info(f"Page title: {title}")
        return title

    async def get_page_url(self) -> str:
        """Get current page URL."""
        url = self.page.url
        logger.info(f"Current URL: {url}")
        return url
