import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

df = pd.read_csv(
    r"C:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\DATASETS\RAW\merchants.csv"
)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Add merchant_id column
df.insert(0, "merchant_id", range(1, len(df) + 1))

# Remove duplicates
df = df.drop_duplicates(subset=["merchant_id"])

# Check existing merchants
existing = pd.read_sql(
    "SELECT merchant_id FROM merchants",
    engine
)

df = df[~df["merchant_id"].isin(existing["merchant_id"])]

# Load
df.to_sql(
    "merchants",
    engine,
    if_exists="append",
    index=False,
    chunksize=500
)

print(f"✅ Loaded {len(df)} merchants")