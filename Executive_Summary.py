import pandas as pd
from python.Config.database import engine

customers = pd.read_sql("SELECT * FROM customers", engine)
accounts = pd.read_sql("SELECT * FROM accounts", engine)
transactions = pd.read_sql("SELECT * FROM transactions", engine)
loans = pd.read_sql("SELECT * FROM loans", engine)
branches = pd.read_sql("SELECT * FROM branches", engine)
merchants = pd.read_sql("SELECT * FROM merchants", engine)

print("=" * 70)
print("BANKING RISK CUSTOMER ANALYTICS")
print("EXECUTIVE SUMMARY")
print("=" * 70)

print("\nCUSTOMERS")
print(f"Total Customers            : {len(customers):,}")

print("\nACCOUNTS")
print(f"Total Accounts             : {len(accounts):,}")
print(f"Total Deposits             : ₹ {accounts['balance'].sum():,.2f}")

print("\nTRANSACTIONS")
print(f"Total Transactions         : {len(transactions):,}")
print(f"Transaction Amount         : ₹ {transactions['amount'].sum():,.2f}")

print("\nLOANS")
print(f"Total Loans                : {len(loans):,}")
print(f"Loan Portfolio             : ₹ {loans['loan_amount'].sum():,.2f}")

print("\nBRANCHES")
print(f"Total Branches             : {len(branches):,}")

print("\nMERCHANTS")
print(f"Total Merchants            : {len(merchants):,}")

print("\nFRAUD")
print(f"Failed Transactions        : {(transactions['status']=='Failed').sum():,}")
print(f"International Transactions : {transactions['is_international'].sum():,}")

print("\nCUSTOMER RISK")
print(f"Average Credit Score       : {customers['credit_score'].mean():.2f}")
print(f"Loan Defaults              : {loans['default_flag'].sum():,}")

print("\nTOP 5 STATES")

print(customers["state"].value_counts().head())

print("\nTOP 5 TRANSACTION CHANNELS")

print(transactions["channel"].value_counts().head())

print("\nTOP 5 ACCOUNT TYPES")

print(accounts["account_type_id"].value_counts().head())

print("\nTOP 5 LOAN TYPES")

print(loans["loan_type_id"].value_counts().head())

print("\n" + "=" * 70)
print("REPORT GENERATED SUCCESSFULLY")
print("=" * 70)