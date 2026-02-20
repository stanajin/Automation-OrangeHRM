"""Database utility for MySQL connections."""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()
logger = get_logger(__name__)


class DatabaseConnection:
    """Database connection handler for MySQL."""

    def __init__(self):
        """Initialize database connection parameters from environment."""
        self.host = os.getenv("MYSQL_HOST", "127.0.0.1")
        self.port = int(os.getenv("MYSQL_PORT", 3306))
        self.user = os.getenv("MYSQL_USER", "root")
        self.password = os.getenv("MYSQL_PASSWORD", "")
        self.database = os.getenv("MYSQL_DATABASE", "orangehrm")
        self.conn = None

    def connect(self):
        """Establish database connection."""
        try:
            logger.info(
                f"Attempting MySQL connection to {self.host}:{self.port}/{self.database}"
            )
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                connection_timeout=5,
            )
            logger.info(f"Connected to MySQL: {self.host}:{self.port}/{self.database}")
            return self.conn
        except Error as e:
            logger.error(f"Error connecting to MySQL: {e}")
            return None

    def disconnect(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Disconnected from MySQL")

    def execute_query(self, query: str):
        """Execute a modification query (INSERT/UPDATE/DELETE)."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            logger.info(f"Query executed successfully: {query[:50]}...")
            cursor.close()
        except Error as e:
            logger.error(f"Error executing query: {e}")
            self.conn.rollback()

    def fetch_query(self, query: str):
        """Execute a SELECT query and return results."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            logger.info(f"Query fetched successfully: {query[:50]}...")
            cursor.close()
            return results
        except Error as e:
            logger.error(f"Error fetching query: {e}")
            return None

    def fetch_one(self, query: str):
        """Execute a SELECT query and return first result."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            logger.info(f"Query fetched one record: {query[:50]}...")
            cursor.close()
            return result
        except Error as e:
            logger.error(f"Error fetching query: {e}")
            return None
