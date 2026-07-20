from pathlib import Path

from src.utils.logger import logger


def ensure_directory_exists(directory: Path):
    """Create the directory if it does not already exist."""

    directory.mkdir(parents=True, exist_ok=True)

    logger.info(f"Verified directory exists: {directory}")
