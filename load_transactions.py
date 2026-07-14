import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

df = pd.read_csv(
    r"C:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\DATASETS\RAW\transactions.csv"
)

# clean columns
df.columns = df.columns.str.strip().str.lower()

# -------------------------
# ADD TRANSACTION TYPE NAME
# -------------------------
transaction_map = {
    1: "Deposit",
    2: "Withdrawal",
    3: "Transfer",
    5: "UPI Payment",
    6: "Debit Card",
    7: "Credit Card",
    8: "NEFT",
    9: "RTGS",
    10: "IMPS",
    11: "ATM Withdrawal",
    12: "Cash Deposit",
    13: "POS Purchase"
}

df["transaction_type"] = df["transaction_type_id"].map(transaction_map)

# FK CHECK
valid_accounts = pd.read_sql("SELECT account_id FROM accounts", engine)
df = df[df["account_id"].isin(valid_accounts["account_id"])]

# DUPLICATE PREVENTION
existing = pd.read_sql("SELECT reference_number FROM transactions", engine)
df = df[~df["reference_number"].isin(existing["reference_number"])]

# LOAD
df.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False,
    chunksize=500
)

print("✅ Transactions loaded successfully")