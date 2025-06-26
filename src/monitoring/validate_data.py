import sys
import pandas as pd

df = pd.read_parquet("output/spotify_daily_top.parquet")

if df.isnull().any().any():
    print("❌ Null values found in the dataset!")
    sys.exit(1)
else:
    print("✅ Data validation passed.")
