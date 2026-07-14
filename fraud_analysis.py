import pandas as pd
from python.Config.database import engine

transactions = pd.read_sql("""
SELECT
    transaction_id,
    account_id,
    merchant_id,
    amount,
    status,
    is_international,
    channel,
    transaction_type,
    transaction_date
FROM transactions
""", engine)

print("=" * 60)
print("FRAUD ANALYSIS REPORT")
print("=" * 60)

print("\nTotal Transactions:")
print(len(transactions))

print("\nFailed Transactions:")
failed = transactions[transactions["status"] == "Failed"]
print(len(failed))

print("\nFailure Percentage:")
print(f"{len(failed) / len(transactions) * 100:.2f}%")

print("\nInternational Transactions:")
international = transactions[transactions["is_international"] == True]
print(len(international))

print("\nInternational Transaction Percentage:")
print(f"{len(international) / len(transactions) * 100:.2f}%")

print("\nTop 10 Accounts with Failed Transactions")
print(
    failed.groupby("account_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Merchants with Failed Transactions")
print(
    failed.groupby("merchant_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Channels with Failed Transactions")
print(
    failed["channel"]
    .value_counts()
)

print("\nTop Transaction Types with Failed Transactions")
print(
    failed["transaction_type"]
    .value_counts()
)

print("\nTop 10 Highest Failed Transactions")
print(
    failed[
        [
            "transaction_id",
            "account_id",
            "merchant_id",
            "amount",
            "channel"
        ]
    ]
    .sort_values("amount", ascending=False)
    .head(10)
)

print("\nSummary Statistics")
print(transactions.describe(include="all"))