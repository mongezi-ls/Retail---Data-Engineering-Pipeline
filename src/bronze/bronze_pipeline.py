import pandas as pd
from pathlib import Path

# Path of the raw data file
RAW_DATA_PATH = Path("data/raw/Retail_Store_Sales.csv")

# Check if the file exist
if RAW_DATA_PATH.exists():
    print(f'File found: {RAW_DATA_PATH}')
    """
    Load the raw data into a pandas DataFrame

    """
    df = pd.read_csv(RAW_DATA_PATH)
    print('Data loaded successfully.')

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
    print(df.info())

else:
    print(f'File not found: {RAW_DATA_PATH}')
    exit(1)