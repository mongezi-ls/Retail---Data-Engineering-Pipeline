from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
BRONZE_DATA_DIR = DATA_DIR / "bronze"

RAW_DATA_PATH = RAW_DATA_DIR / "retail_store_sales.csv"
BRONZE_DATA_PATH = BRONZE_DATA_DIR / "bronze_sales.csv"

LOG_DIR = PROJECT_ROOT / "logs"
