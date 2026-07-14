import pandas as pd

from python.Config.database import engine


print("="*70)
print("POWER BI DASHBOARD DATA GENERATION")
print("="*70)


# ==========================
# KPI DATA
# ==========================

kpi = pd.read_sql(
"""
SELECT
(SELECT COUNT(*) FROM customers) AS total_customers,
(SELECT COUNT(*) FROM accounts) AS total_accounts,
(SELECT COUNT(*) FROM transactions) AS total_transactions,
(SELECT SUM(amount) FROM transactions) AS transaction_volume,
(SELECT COUNT(*) FROM loans) AS total_loans,
(SELECT SUM(loan_amount) FROM loans) AS loan_portfolio
""",
engine
)


kpi.to_csv(
"datasets/processed/dashboard_kpi.csv",
index=False
)


# ==========================
# CUSTOMER DATA
# ==========================

customer_state = pd.read_sql(
"""
SELECT
state,
COUNT(*) customer_count
FROM customers
GROUP BY state
ORDER BY customer_count DESC
""",
engine
)


customer_state.to_csv(
"datasets/processed/customer_state.csv",
index=False
)



# ==========================
# TRANSACTION CHANNEL
# ==========================

channel = pd.read_sql(
"""
SELECT
channel,
COUNT(*) transaction_count,
SUM(amount) total_amount
FROM transactions
GROUP BY channel
ORDER BY transaction_count DESC
""",
engine
)


channel.to_csv(
"datasets/processed/transaction_channel.csv",
index=False
)



# ==========================
# FRAUD DATA
# ==========================

fraud = pd.read_sql(
"""
SELECT
status,
COUNT(*) count
FROM transactions
GROUP BY status
""",
engine
)


fraud.to_csv(
"datasets/processed/fraud_summary.csv",
index=False
)



# ==========================
# LOAN DATA
# ==========================

loan = pd.read_sql(
"""
SELECT
loan_type_id,
COUNT(*) loan_count,
SUM(loan_amount) total_amount
FROM loans
GROUP BY loan_type_id
""",
engine
)


loan.to_csv(
"datasets/processed/loan_summary.csv",
index=False
)



print("\nDashboard files generated successfully")
print("="*70)