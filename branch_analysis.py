import pandas as pd
from python.Config.database import engine

branches = pd.read_sql("""
SELECT *
FROM branches
""", engine)

accounts = pd.read_sql("""
SELECT branch_id, balance
FROM accounts
""", engine)

customers = pd.read_sql("""
SELECT DISTINCT
    customer_id,
    branch_id
FROM accounts
""", engine)

loans = pd.read_sql("""
SELECT customer_id, loan_amount
FROM loans
""", engine)

# Merge customers with loans
customer_loans = customers.merge(
    loans,
    on="customer_id",
    how="left"
)

print("=" * 60)
print("BRANCH ANALYSIS REPORT")
print("=" * 60)

print("\nTotal Branches:")
print(len(branches))

print("\nBranch-wise Accounts")
print(accounts["branch_id"].value_counts().head(10))

print("\nTop 10 Branches by Deposits")
print(
    accounts.groupby("branch_id")["balance"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Branches by Average Balance")
print(
    accounts.groupby("branch_id")["balance"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Branches by Customer Count")
print(
    customers["branch_id"]
    .value_counts()
    .head(10)
)

print("\nTop 10 Branches by Loan Amount")
print(
    customer_loans.groupby("branch_id")["loan_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nBranch Summary")
print(branches.describe(include="all"))