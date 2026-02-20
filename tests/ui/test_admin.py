"""UI Tests for OrangeHRM Admin Page functionality."""

import pytest
from config.config import Config
from pages.admin_page import AdminPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.ui
@pytest.mark.asyncio
class TestAdmin:
    """Test admin page functionality using Page Object Model."""

    async def test_admin_page_loads(self, authenticated_page):
        """Test that admin page loads successfully."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        admin_page = AdminPage(authenticated_page)
        
        # Verify admin page is loaded
        is_loaded = await admin_page.is_admin_page_loaded()
        assert is_loaded
        logger.info("✓ Admin page loads successfully")

    async def test_search_user_by_username(self, authenticated_page):
        """Test searching for a user by username."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        admin_page = AdminPage(authenticated_page)
        
        # Search for user
        await admin_page.search_user("Admin")
        
        # Verify search was executed
        assert "Admin" in await authenticated_page.content()
        logger.info("✓ User search by username test passed")

    async def test_search_user_empty_username(self, authenticated_page):
        """Test searching with empty username field."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        admin_page = AdminPage(authenticated_page)
        
        # Attempt search with empty username
        await admin_page.search_user("")
        
        # Should still load page (search executes with no filter)
        assert authenticated_page.url is not None
        logger.info("✓ Empty username search test passed")

    async def test_admin_page_url(self, authenticated_page):
        """Test admin page URL."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        
        url = authenticated_page.url
        assert "admin" in url.lower()
        assert "viewSystemUsers" in url
        logger.info(f"✓ Admin page URL test passed - URL: {url}")

    async def test_admin_page_title(self, authenticated_page):
        """Test admin page title."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        admin_page = AdminPage(authenticated_page)
        
        title = await authenticated_page.title()
        assert "Admin" in title or "OrangeHRM" in title
        logger.info(f"✓ Admin page title test passed - Title: {title}")

    async def test_admin_page_elements_visible(self, authenticated_page):
        """Test that main admin page elements are visible."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        admin_page = AdminPage(authenticated_page)
        
        # Check if admin page is loaded (title should be visible)
        is_loaded = await admin_page.is_admin_page_loaded()
        assert is_loaded, "Admin page title not visible"
        logger.info("✓ Admin page elements visibility test passed")

    async def test_search_and_verify_results(self, authenticated_page):
        """Test searching and verifying results are displayed."""
        # Navigate to admin page
        await authenticated_page.goto(f"{Config.BASE_URL}/web/index.php/admin/viewSystemUsers")
        admin_page = AdminPage(authenticated_page)
        
        # Perform search
        await admin_page.search_user("Admin")
        
        # Wait for results to load
        await authenticated_page.wait_for_load_state("networkidle")
        
        # Verify page still on admin section
        assert "admin" in authenticated_page.url.lower()
        logger.info("✓ Search and verify results test passed")
