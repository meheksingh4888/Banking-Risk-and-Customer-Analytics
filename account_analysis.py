import pandas as pd
from python.Config.database import engine

# Read accounts table
accounts = pd.read_sql("SELECT * FROM accounts", engine)

print("=" * 60)
print("ACCOUNT ANALYSIS REPORT")
print("=" * 60)

# Total Accounts
print(f"\nTotal Accounts: {len(accounts)}")

# Account Type Distribution
print("\nAccount Type Distribution")
print(accounts["account_type_id"].value_counts())

# Total Balance
print("\nTotal Bank Balance")
print(f"₹ {accounts['balance'].sum():,.2f}")

# Average Balance
print("\nAverage Balance")
print(f"₹ {accounts['balance'].mean():,.2f}")

# Highest Balance
print("\nHighest Balance")
print(f"₹ {accounts['balance'].max():,.2f}")

# Lowest Balance
print("\nLowest Balance")
print(f"₹ {accounts['balance'].min():,.2f}")

# Top 10 Accounts by Balance
print("\nTop 10 Accounts by Balance")

top_accounts = (
    accounts[
        ["account_id", "customer_id", "account_type_id", "balance"]
    ]
    .sort_values(by="balance", ascending=False)
    .head(10)
)

print(top_accounts)

# Dormant Accounts
print("\nDormant Accounts")

accounts["last_transaction_date"] = pd.to_datetime(
    accounts["last_transaction_date"]
)

dormant = accounts[
    accounts["last_transaction_date"] < "2025-01-01"
]

print("Dormant Accounts:", len(dormant))
print("Active Accounts:", len(accounts) - len(dormant))

# Branch-wise Accounts
print("\nTop 10 Branchs by Accounts")

print(
    accounts["branch_id"]
    .value_counts()
    .head(10)
)

# Summary Statistics
print("\nSummary Statistics")

print(accounts.describe())