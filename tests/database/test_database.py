"""Database Tests for OrangeHRM."""

import pytest
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.database
class TestDatabaseConnection:
    """Test database connectivity."""

    def test_database_connection(self, db_connection):
        """Test database connection is established."""
        assert db_connection is not None
        assert db_connection.conn is not None
        logger.info("✓ Database connection test passed")

    def test_database_parameters(self, db_connection):
        """Test database parameters are correctly set."""
        assert db_connection.host is not None
        assert db_connection.user is not None
        assert db_connection.database is not None
        logger.info("✓ Database parameters test passed")

    def test_simple_query(self, db_connection):
        """Test executing a simple SELECT query."""
        query = "SELECT 1 AS test"
        result = db_connection.fetch_one(query)
        
        assert result is not None
        assert result[0] == 1
        logger.info("✓ Simple query test passed")

    def test_fetch_multiple_rows(self, db_connection):
        """Test fetching multiple rows."""
        query = "SELECT 1 UNION SELECT 2"
        results = db_connection.fetch_query(query)
        
        assert results is not None
        assert len(results) > 0
        logger.info("✓ Fetch multiple rows test passed")
