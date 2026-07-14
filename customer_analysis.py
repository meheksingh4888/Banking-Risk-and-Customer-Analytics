import pandas as pd
from python.Config.database import engine

# Read customers table
customers = pd.read_sql("SELECT * FROM customers", engine)

print("=" * 60)
print("CUSTOMER ANALYSIS REPORT")
print("=" * 60)

# Total Customers
print(f"\nTotal Customers: {len(customers)}")

# Gender Distribution
print("\nGender Distribution")
print(customers["gender"].value_counts())

# State-wise Customers
print("\nTop 10 States")
print(customers["state"].value_counts().head(10))

# City-wise Customers
print("\nTop 10 Cities")
print(customers["city"].value_counts().head(10))

# Average Income
print("\nAverage Annual Income")
print(f"₹ {customers['annual_income'].mean():,.2f}")

# Highest Income
print("\nHighest Annual Income")
print(f"₹ {customers['annual_income'].max():,.2f}")

# Lowest Income
print("\nLowest Annual Income")
print(f"₹ {customers['annual_income'].min():,.2f}")

# Credit Score Statistics
print("\nAverage Credit Score")
print(round(customers["credit_score"].mean(), 2))

print("\nHighest Credit Score")
print(customers["credit_score"].max())

print("\nLowest Credit Score")
print(customers["credit_score"].min())

# Top 10 Customers by Income
print("\nTop 10 Customers by Income")
top_income = customers[
    ["customer_id", "first_name", "last_name", "annual_income"]
].sort_values(
    by="annual_income",
    ascending=False
).head(10)

print(top_income)

# Summary Statistics
print("\nSummary Statistics")
print(customers.describe())