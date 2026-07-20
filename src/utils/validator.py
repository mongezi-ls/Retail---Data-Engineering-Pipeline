import pandas as pd
from src.utils.logger import logger
from src.config.config import EXPECTED_COLUMNS


def validate_dataframe(df: pd.DataFrame) -> bool:
    """Validate the loaded DataFrame."""

    if df.empty:
        logger.error("The DataFrame is empty.")
        return False

    missing_columns = [
        column for column in EXPECTED_COLUMNS if column not in df.columns
    ]

    if missing_columns:
        logger.error(f"Missing columns: {missing_columns}")
        return False

    duplicate_count = df["Transaction ID"].duplicated().sum()

    if duplicate_count > 0:
        logger.warning(f"Found {duplicate_count} duplicate Transaction ID(s).")

    logger.info("DataFrame validation passed.")
    return True
