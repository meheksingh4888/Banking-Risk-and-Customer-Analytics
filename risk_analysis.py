import pandas as pd
from python.Config.database import engine


# ==============================
# LOAD CUSTOMER DATA
# ==============================

customers = pd.read_sql("""
SELECT
    customer_id,
    annual_income,
    credit_score
FROM customers
""", engine)


# ==============================
# LOAD LOAN DATA
# Aggregate loans customer wise
# ==============================

loans = pd.read_sql("""
SELECT
    customer_id,
    SUM(loan_amount) AS total_loan_amount,
    COUNT(loan_id) AS loan_count,
    SUM(CASE 
            WHEN default_flag = TRUE 
            THEN 1 
            ELSE 0 
        END) AS default_count
FROM loans
GROUP BY customer_id
""", engine)


# ==============================
# LOAD ACCOUNT DATA
# Aggregate balance customer wise
# ==============================

accounts = pd.read_sql("""
SELECT
    customer_id,
    SUM(balance) AS total_balance
FROM accounts
GROUP BY customer_id
""", engine)


# ==============================
# CREATE CUSTOMER RISK DATASET
# ==============================

risk = (
    customers
    .merge(loans, on="customer_id", how="left")
    .merge(accounts, on="customer_id", how="left")
)


# Handle missing values

risk["total_loan_amount"] = (
    risk["total_loan_amount"]
    .fillna(0)
)

risk["loan_count"] = (
    risk["loan_count"]
    .fillna(0)
)

risk["default_count"] = (
    risk["default_count"]
    .fillna(0)
)

risk["total_balance"] = (
    risk["total_balance"]
    .fillna(0)
)


# ==============================
# RISK SCORE CALCULATION
# ==============================

risk["risk_score"] = 0


# Credit Score Risk

risk.loc[
    risk["credit_score"] < 500,
    "risk_score"
] += 40


risk.loc[
    (risk["credit_score"] >= 500) &
    (risk["credit_score"] < 700),
    "risk_score"
] += 20



# Default Risk

risk.loc[
    risk["default_count"] > 0,
    "risk_score"
] += 40



# High Loan Risk

risk.loc[
    risk["total_loan_amount"] > 3000000,
    "risk_score"
] += 20



# Loan vs Income Risk

risk.loc[
    risk["total_loan_amount"] >
    (risk["annual_income"] * 5),
    "risk_score"
] += 20



# ==============================
# RISK CATEGORY
# ==============================

def assign_risk(score):

    if score <= 30:
        return "Low Risk"

    elif score <= 60:
        return "Medium Risk"

    else:
        return "High Risk"



risk["risk_category"] = (
    risk["risk_score"]
    .apply(assign_risk)
)



# ==============================
# REPORT
# ==============================

print("=" * 60)
print("CUSTOMER RISK ANALYSIS REPORT")
print("=" * 60)


print("\nTotal Customers")
print(
    risk["customer_id"].nunique()
)


print("\nRisk Category Distribution")

print(
    risk["risk_category"]
    .value_counts()
)



print("\nAverage Risk Score")

print(
    round(
        risk["risk_score"].mean(),
        2
    )
)



print("\nHigh Risk Customers")


print(
    risk[
        risk["risk_category"] == "High Risk"
    ]
    [
        [
            "customer_id",
            "credit_score",
            "annual_income",
            "total_loan_amount",
            "default_count",
            "risk_score"
        ]
    ]
    .head(20)
)



print("\nFinal Risk Dataset")

print(
    risk[
        [
            "customer_id",
            "credit_score",
            "total_loan_amount",
            "default_count",
            "risk_score",
            "risk_category"
        ]
    ]
    .head(20)
)