import pandas as pd
from pathlib import Path

# Imports for file, logger, and validator.

from src.config.config import RAW_DATA_PATH, BRONZE_DATA_PATH
from src.utils.logger import logger
from src.utils.validator import validate_dataframe

# Check if the file exist


def load_data():
    """
    Load the raw data into a pandas DataFrame

    """
    if not RAW_DATA_PATH.exists():
        logger.error(f"File not found: {RAW_DATA_PATH}")
        return None

    logger.info(f"Raw data file found: {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)

    logger.info(" Raw data loaded successfully.")
    return df


# Inspect the data


def inspect_data(df):
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


def save_bronze_data(df):
    """Save the raw data to the Bronze layer."""

    df.to_csv(BRONZE_DATA_PATH, index=False)

    logger.info("Bronze data saved successfully.")


def main():
    logger.info("=" * 60)

    try:
        logger.info("Starting Bronze Pipeline...")

        df = load_data()

        if df is not None:

            if validate_dataframe(df):

                inspect_data(df)
                save_bronze_data(df)

                logger.info("Bronze Pipeline finished.")

    except Exception as e:
        logger.exception(f"Bronze Pipeline failed: {e}")

    finally:
        logger.info("=" * 60)


if __name__ == "__main__":
    main()
