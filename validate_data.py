import pandas as pd
from sqlalchemy import create_engine

# ============================================
# DATABASE CONNECTION
# ============================================

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

print("=" * 60)
print("        BANKING DATA VALIDATION REPORT")
print("=" * 60)

# ============================================
# TABLES TO VALIDATE
# ============================================

tables = [
    "customers",
    "accounts",
    "transactions"
]

duplicate_found = False

# ============================================
# 1. MISSING VALUES CHECK
# ============================================

print("\n1. MISSING VALUES CHECK")

for table in tables:

    df = pd.read_sql(f"SELECT * FROM {table}", engine)

    print(f"\n{table.upper()}")

    print(df.isnull().sum())

# ============================================
# 2. DUPLICATE RECORDS CHECK
# ============================================

print("\n2. DUPLICATE RECORDS CHECK")

for table in tables:

    df = pd.read_sql(f"SELECT * FROM {table}", engine)

    duplicates = df.duplicated().sum()

    print(f"{table}: {duplicates}")

    if duplicates > 0:
        duplicate_found = True

# ============================================
# 3. FOREIGN KEY VALIDATION
# ============================================

print("\n3. FOREIGN KEY VALIDATION")

accounts = pd.read_sql(
    "SELECT account_id FROM accounts",
    engine
)

transactions = pd.read_sql(
    "SELECT account_id FROM transactions",
    engine
)

invalid_fk = transactions[
    ~transactions["account_id"].isin(accounts["account_id"])
]

print(f"Invalid Account References : {len(invalid_fk)}")

# ============================================
# 4. NEGATIVE TRANSACTION AMOUNTS
# ============================================

print("\n4. NEGATIVE TRANSACTION CHECK")

tx = pd.read_sql(
    "SELECT amount FROM transactions",
    engine
)

negative = tx[tx["amount"] < 0]

print(f"Negative Amount Transactions : {len(negative)}")

# ============================================
# 5. FINAL SUMMARY
# ============================================

print("\n" + "=" * 60)
print("VALIDATION SUMMARY")
print("=" * 60)

if (
    len(invalid_fk) == 0
    and len(negative) == 0
    and duplicate_found is False
):

    print("✅ ALL VALIDATIONS PASSED")

else:

    print("❌ VALIDATION FAILED")
    print("Please check the errors shown above.")

print("=" * 60)
print("VALIDATION COMPLETED")
print("=" * 60)