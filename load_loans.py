import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

df = pd.read_csv(
    r"C:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\DATASETS\RAW\loans.csv"
)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Add loan_id column
df.insert(0, "loan_id", range(1, len(df) + 1))

# Remove duplicates
df = df.drop_duplicates(subset=["loan_id"])

# Check existing loans
existing = pd.read_sql(
    "SELECT loan_id FROM loans",
    engine
)

df = df[~df["loan_id"].isin(existing["loan_id"])]

# Load
df.to_sql(
    "loans",
    engine,
    if_exists="append",
    index=False,
    chunksize=500
)

print(f"✅ Loaded {len(df)} loans")