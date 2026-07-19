import pandas as pd
from pathlib import Path

# Path of the raw data file
RAW_DATA_PATH = Path("data/raw/Retail_Store_Sales.csv")

# Check if the file exist

def load_data():
    """
    Load the raw data into a pandas DataFrame

    """
    if not RAW_DATA_PATH.exists():
        print(f'File not found: {RAW_DATA_PATH}')
        return None

    print(f'File found: {RAW_DATA_PATH}')
    df = pd.read_csv(RAW_DATA_PATH)

    print('Data loaded successfully.')
    return df


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


def main():
    """
    Load and inspect the data

    """
    df = load_data()

    if df is not None:
        inspect_data(df)

if __name__ == '__main__':
    main()