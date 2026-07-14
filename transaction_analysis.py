import pandas as pd
from python.Config.database import engine

transactions = pd.read_sql("""
SELECT *
FROM transactions
""", engine)

print("=" * 60)
print("TRANSACTION ANALYSIS REPORT")
print("=" * 60)

print("\nTotal Transactions:")
print(len(transactions))

print("\nTotal Transaction Amount:")
print(f"₹ {transactions['amount'].sum():,.2f}")

print("\nAverage Transaction Amount:")
print(f"₹ {transactions['amount'].mean():,.2f}")

print("\nTransaction Status")
print(transactions["status"].value_counts())

print("\nTransaction Channels")
print(transactions["channel"].value_counts())

print("\nDevice Types")
print(transactions["device_type"].value_counts())

print("\nInternational Transactions")
print(transactions["is_international"].value_counts())

print("\nTop 10 Transaction Cities")
print(transactions["transaction_city"].value_counts().head(10))

print("\nTop 10 Largest Transactions")
print(
    transactions[
        ["transaction_id", "account_id", "amount", "transaction_type", "status"]
    ]
    .sort_values("amount", ascending=False)
    .head(10)
)

print("\nSummary Statistics")
print(transactions.describe(include="all"))