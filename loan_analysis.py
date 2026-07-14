import pandas as pd
from python.Config.database import engine

loans = pd.read_sql("""
SELECT *
FROM loans
""", engine)

print("=" * 60)
print("LOAN ANALYSIS REPORT")
print("=" * 60)

print("\nTotal Loans:")
print(len(loans))

print("\nTotal Loan Amount:")
print(f"₹ {loans['loan_amount'].sum():,.2f}")

print("\nAverage Loan Amount:")
print(f"₹ {loans['loan_amount'].mean():,.2f}")

print("\nLoan Type Distribution")
print(loans["loan_type_id"].value_counts())

print("\nAverage Interest Rate")
print(f"{loans['interest_rate'].mean():.2f}%")

print("\nAverage EMI")
print(f"₹ {loans['emi_amount'].mean():,.2f}")

print("\nLoan Tenure Distribution")
print(loans["tenure_months"].value_counts().sort_index())

print("\nDefault Customers")
print(loans["default_flag"].value_counts())

print("\nTop 10 Highest Loans")
print(
    loans[
        [
            "loan_id",
            "customer_id",
            "loan_type_id",
            "loan_amount",
            "interest_rate",
            "emi_amount"
        ]
    ]
    .sort_values("loan_amount", ascending=False)
    .head(10)
)

print("\nSummary Statistics")
print(loans.describe(include="all"))