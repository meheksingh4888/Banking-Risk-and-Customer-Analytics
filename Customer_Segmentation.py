import pandas as pd
from python.Config.database import engine

customers = pd.read_sql("""
SELECT
    customer_id,
    first_name,
    last_name,
    annual_income,
    credit_score
FROM customers
""", engine)

# -----------------------------
# Income Segmentation
# -----------------------------
customers["income_segment"] = pd.cut(
    customers["annual_income"],
    bins=[0,500000,1000000,2000000,5000000],
    labels=[
        "Low Income",
        "Middle Income",
        "Upper Middle",
        "High Income"
    ]
)

# -----------------------------
# Credit Score Segmentation
# -----------------------------
customers["credit_segment"] = pd.cut(
    customers["credit_score"],
    bins=[300,580,670,740,800,900],
    labels=[
        "Poor",
        "Fair",
        "Good",
        "Very Good",
        "Excellent"
    ],
    include_lowest=True
)

print("="*60)
print("CUSTOMER SEGMENTATION REPORT")
print("="*60)

print("\nTotal Customers")
print(len(customers))

print("\nIncome Segments")
print(customers["income_segment"].value_counts())

print("\nCredit Score Segments")
print(customers["credit_segment"].value_counts())

print("\nAverage Income by Credit Segment")
print(
    customers.groupby("credit_segment")["annual_income"].mean()
)

print("\nTop 20 High Income Customers")
print(
    customers[
        [
            "customer_id",
            "first_name",
            "last_name",
            "annual_income",
            "credit_score"
        ]
    ]
    .sort_values("annual_income",ascending=False)
    .head(20)
)

print("\nSummary Statistics")
print(customers.describe(include="all"))