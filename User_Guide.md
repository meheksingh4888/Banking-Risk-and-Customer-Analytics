# Banking Risk Customer Analytics

## User Guide

---

# Introduction

The Banking Risk Customer Analytics project is an end-to-end Data Analytics solution developed using PostgreSQL, Python, SQL, and Power BI.

The project analyzes customers, accounts, transactions, loans, branches, merchants, and fraud risk to generate business insights and executive dashboards.

---

# Technology Stack

- PostgreSQL
- SQL
- Python
- Pandas
- NumPy
- SQLAlchemy
- Power BI
- Git
- VS Code

---

# Folder Structure

```
Banking-Risk-Customer-Analytics/

database/
datasets/
python/
sql_queries/
dashboards/
presentation/
docs/
screenshots/
README.md
requirements.txt
```

---

# Project Workflow

1. Generate Banking Dataset
2. Load Data into PostgreSQL
3. Validate Data
4. Perform SQL Analysis
5. Perform Python EDA
6. Risk Analysis
7. Dashboard Data Preparation
8. Power BI Dashboard
9. Executive Summary
10. Documentation

---

# Running the Project

## Step 1

Clone the repository

```
git clone <repository-url>
```

---

## Step 2

Install Python packages

```
pip install -r requirements.txt
```

---

## Step 3

Configure PostgreSQL database credentials.

Update

```
python/Config/database.py
```

with your PostgreSQL username, password, host, and database name.

---

## Step 4

Load the database

Run

```
python python/ETL/load_data.py
```

---

## Step 5

Run Python Analysis

```
python -m python.Analysis.customer_analysis

python -m python.Analysis.account_analysis

python -m python.Analysis.transaction_analysis

python -m python.Analysis.loan_analysis

python -m python.Analysis.branch_analysis

python -m python.Analysis.merchant_analysis

python -m python.Analysis.risk_analysis

python -m python.Analysis.Executive_Summary
```

---

## Step 6

Open Power BI Dashboard

```
powerbi/Banking_Risk_Customer_Analytics.pbix
```

Refresh the data source.

---

# Dashboard Pages

- Executive Dashboard
- Customer Analysis
- Account Analysis
- Transaction Analysis
- Loan Analysis
- Fraud Analysis
- Branch Analysis
- Risk Analysis

---

# Key KPIs

- Total Customers
- Total Accounts
- Total Deposits
- Loan Portfolio
- Transaction Volume
- Failed Transactions
- Average Credit Score
- Loan Default Rate
- Branch Performance
- Merchant Performance

---

# Business Insights

The project provides:

- Customer Segmentation
- Credit Risk Analysis
- Loan Performance
- Fraud Detection
- Branch Performance
- Merchant Analysis
- Transaction Trends
- Executive Reporting

---

# Author

Mehek Singh