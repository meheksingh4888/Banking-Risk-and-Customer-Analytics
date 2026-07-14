import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

# Load transactions
df = pd.read_sql("SELECT * FROM transactions", engine)

# -----------------------------
# FRAUD RULE 1: HIGH VALUE
# -----------------------------
df["fraud_reason"] = None

df.loc[df["amount"] > 100000, "fraud_reason"] = "High Value Transaction"

# -----------------------------
# FRAUD RULE 2: FAILED TRANSACTIONS
# -----------------------------
df.loc[df["status"].str.lower() == "failed", "fraud_reason"] = "Failed Transaction"

# -----------------------------
# FRAUD RULE 3: MULTIPLE TXNS (VELOCITY CHECK)
# -----------------------------
df["txn_count"] = df.groupby(["account_id", "transaction_date"])["transaction_id"].transform("count")

df.loc[df["txn_count"] > 3, "fraud_reason"] = "Multiple Transactions Same Day"

# -----------------------------
# KEEP ONLY FRAUD CASES
# -----------------------------
fraud_df = df[df["fraud_reason"].notnull()]

# -----------------------------
# LOAD TO DB
# -----------------------------
fraud_df.to_sql(
    "fraud_alerts",
    engine,
    if_exists="append",
    index=False
)

print("🚨 Fraud alerts generated successfully")