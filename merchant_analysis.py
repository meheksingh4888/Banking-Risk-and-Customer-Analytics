import pandas as pd
from python.Config.database import engine

merchants = pd.read_sql("""
SELECT *
FROM merchants
""", engine)

transactions = pd.read_sql("""
SELECT
    merchant_id,
    amount,
    status,
    transaction_type,
    channel
FROM transactions
""", engine)

merchant_txn = merchants.merge(
    transactions,
    on="merchant_id",
    how="left"
)

print("=" * 60)
print("MERCHANT ANALYSIS REPORT")
print("=" * 60)

print("\nTotal Merchants:")
print(len(merchants))

print("\nMerchant Categories")
print(merchants["merchant_category"].value_counts())

print("\nTop 10 Merchants by Transactions")
print(
    merchant_txn.groupby("merchant_name")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Merchants by Revenue")
print(
    merchant_txn.groupby("merchant_name")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTransaction Status")
print(merchant_txn["status"].value_counts())

print("\nTransaction Channels")
print(merchant_txn["channel"].value_counts())

print("\nTop Merchant Cities")
print(merchants["city"].value_counts().head(10))

print("\nSummary Statistics")
print(merchants.describe(include="all"))