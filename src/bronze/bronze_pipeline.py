import pandas as pd
import time

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


# Statistics


def log_pipeline_statistics(df: pd.DataFrame) -> None:
    """
    Log summary statistics for the Bronze pipeline.

    Args:
        df (pd.DataFrame): The processed DataFrame.
    """
    logger.info(f"Total rows processed: {df.shape[0]}")
    logger.info(f"Total columns processed: {df.shape[1]}")
    logger.info(f"Bronze output path: {BRONZE_DATA_PATH}")


def main():
    logger.info("=" * 60)
    start_time = time.perf_counter()

    try:
        logger.info("Starting Bronze Pipeline...")

        df = load_data()

        if df is None:
            return

        if not validate_dataframe(df):
            return

        inspect_data(df)
        save_bronze_data(df)
        log_pipeline_statistics(df)

        logger.info("Bronze Pipeline finished.")

    except Exception as e:
        logger.exception(f"Bronze Pipeline failed: {e}")

    finally:
        end_time = time.perf_counter()
        execute_time = end_time - start_time

        logger.info(f"Bronze Pipeline execution time: {execute_time:.2f} seconds")
        logger.info("=" * 60)


if __name__ == "__main__":
    main()
