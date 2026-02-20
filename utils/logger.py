"""Logger configuration for the test suite."""

import logging
import os
from datetime import datetime
from pathlib import Path


def _cleanup_old_logs(log_dir: str, max_logs: int = 5):
    """Remove old log files, keeping only the most recent ones."""
    log_path = Path(log_dir)
    log_files = sorted(log_path.glob("test_*.log"), key=lambda f: f.stat().st_mtime)
    
    # Delete oldest logs if we exceed the limit
    if len(log_files) >= max_logs:
        for old_log in log_files[:-max_logs + 1]:  # Keep space for the new log
            try:
                old_log.unlink()
            except Exception as e:
                print(f"Warning: Could not delete old log {old_log}: {e}")


def get_logger(name: str):
    """Configure and return logger instance."""
    
    # Create logs directory if it doesn't exist
    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Cleanup old logs, keeping only the last 5
    _cleanup_old_logs(log_dir, max_logs=5)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create formatters
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler
    log_file = os.path.join(log_dir, f"test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
