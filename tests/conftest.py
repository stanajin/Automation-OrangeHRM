"""Pytest configuration and fixtures."""

import pytest
from playwright.async_api import async_playwright
from config.config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.logger import get_logger
from utils.database import DatabaseConnection
from utils.api_client import APIClient

logger = get_logger(__name__)


@pytest.fixture(scope="function")
async def browser():
    """Fixture to provide Playwright browser instance."""
    async with async_playwright() as p:
        browser = await p[Config.BROWSER_TYPE].launch(headless=Config.HEADLESS)
        yield browser
        await browser.close()


@pytest.fixture(scope="function")
async def page(browser):
    """Fixture to provide Playwright page instance."""
    page = await browser.new_page()
    yield page
    await page.close()


@pytest.fixture(scope="function")
async def login_page(page):
    """Fixture to provide LoginPage instance."""
    return LoginPage(page)


@pytest.fixture(scope="function")
async def dashboard_page(page):
    """Fixture to provide DashboardPage instance."""
    return DashboardPage(page)


@pytest.fixture(scope="function")
async def authenticated_page(page):
    """Fixture to provide authenticated page (logged in)."""
    login_page = LoginPage(page)
    await page.goto(Config.BASE_URL)
    await login_page.login(Config.DEFAULT_USERNAME, Config.DEFAULT_PASSWORD)
    yield page


@pytest.fixture(scope="function")
async def authenticated_dashboard(authenticated_page):
    """Fixture to provide authenticated dashboard page."""
    return DashboardPage(authenticated_page)


@pytest.fixture(scope="function")
def db_connection():
    """Fixture to provide database connection."""
    db = DatabaseConnection()
    db.connect()
    yield db
    db.disconnect()


@pytest.fixture(scope="function")
def api_client():
    """Fixture to provide API client."""
    return APIClient()


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment before all tests."""
    logger.info("Setting up test environment...")
    logger.info(f"Base URL: {Config.BASE_URL}")
    logger.info(f"Headless mode: {Config.HEADLESS}")
    logger.info(f"Browser: {Config.BROWSER_TYPE}")


@pytest.fixture(scope="function", autouse=True)
def test_logger(request):
    """Fixture to log test start and end."""
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Completed test: {request.node.name}")
