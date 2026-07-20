import pandas as pd

# Imports for file, logger, and validator.
from src.utils.file_utils import ensure_directory_exists
from src.config.config import RAW_DATA_PATH, BRONZE_DATA_PATH
from src.utils.logger import logger
from src.utils.validator import validate_dataframe

# Check if the file exist


def load_data() -> pd.DataFrame | None:
    """
    Load the retail sales data from the raw layer.

    Returns:
        pd.DataFrame: Loaded DataFrame if the file exists, None otherwise.

    """
    if not RAW_DATA_PATH.exists():
        logger.error(f"File not found: {RAW_DATA_PATH}")
        return None

    logger.info(f"Raw data file found: {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)

    logger.info(" Raw data loaded successfully.")
    return df


# Inspect the data


def inspect_data(df: pd.DataFrame) -> None:
    """
    Inspect the loaded data

    """
    print("\nData:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDataset Summary:")
    df.info()


# Save Data to Bronze Layer


def save_bronze_data(df: pd.DataFrame) -> None:
    """
    Save the raw retail sales data to the Bronze layer.

    Args:
        df (pd.DataFrame): DataFrame containing the raw retail sales data.

    """

    ensure_directory_exists(BRONZE_DATA_PATH.parent)
    df.to_csv(BRONZE_DATA_PATH, index=False)

    logger.info("Bronze data saved successfully.")


def main():
    logger.info("=" * 60)

    try:
        logger.info("Starting Bronze Pipeline...")

        df = load_data()

        if df is None:
            return

        if not validate_dataframe(df):
            return

        inspect_data(df)
        save_bronze_data(df)

        logger.info("Bronze Pipeline finished.")

    except Exception as e:
        logger.exception(f"Bronze Pipeline failed: {e}")

    finally:
        logger.info("=" * 60)


if __name__ == "__main__":
    main()
