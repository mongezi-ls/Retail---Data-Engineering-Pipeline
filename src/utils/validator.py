from src.utils.logger import logger


def validate_dataframe(df):
    """Validate the loaded DataFrame."""

    if df.empty:
        logger.error("The DataFrame is empty.")
        return False

    logger.info("DataFrame validation passed.")

    return True
