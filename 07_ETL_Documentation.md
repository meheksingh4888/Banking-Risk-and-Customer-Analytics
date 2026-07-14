# ETL Documentation

## Project

**Banking Risk Customer Analytics**

---

# Introduction

This project follows the ETL (Extract, Transform, Load) process to generate, clean, validate, and load banking data into PostgreSQL for reporting and analytics.

The ETL pipeline is developed using Python, Pandas, SQLAlchemy, and PostgreSQL.

---

# ETL Workflow

```
Raw Data
     │
     ▼
Python Data Generation
     │
     ▼
Data Cleaning
     │
     ▼
Data Validation
     │
     ▼
Transformation
     │
     ▼
PostgreSQL Loading
     │
     ▼
Verification
     │
     ▼
Power BI Dashboard
```

---

# Extract Phase

Data Sources

- Customers
- Accounts
- Transactions
- Loans
- Branches
- Merchants
- Account Types
- Loan Types

Generated using Python scripts.

Example:

- generate_customers.py
- generate_accounts.py
- generate_transactions.py
- generate_loans.py
- generate_merchants.py

---

# Transform Phase

Data Cleaning

Performed using Pandas.

Operations include:

- Removing duplicates
- Handling missing values
- Standardizing column names
- Formatting dates
- Data type conversion
- Removing invalid records

Example:

```python
df = df.drop_duplicates()

df["join_date"] = pd.to_datetime(df["join_date"])
```

---

# Data Validation

Validation checks performed:

## Customer Validation

- Duplicate Customer IDs
- Missing Email
- Missing Phone
- Credit Score Range
- Income Validation

---

## Account Validation

- Duplicate Accounts
- Negative Balance
- Missing Customer ID
- Invalid Account Type

---

## Transaction Validation

- Missing Transaction ID
- Invalid Account
- Invalid Merchant
- Negative Amount
- Invalid Status

---

## Loan Validation

- Missing Customer
- Invalid Loan Type
- EMI Validation
- Interest Rate Validation
- Default Flag Validation

---

## Merchant Validation

- Duplicate Merchant IDs
- Missing Merchant Name
- Invalid Category

---

# Load Phase

Data loaded into PostgreSQL using SQLAlchemy.

Example:

```python
df.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)
```

---

# Database Loading Order

1. Branches
2. Account Types
3. Loan Types
4. Customers
5. Merchants
6. Accounts
7. Loans
8. Transactions

This order maintains foreign key integrity.

---

# Validation Reports

Python scripts generate validation reports including:

- Total Records
- Missing Values
- Duplicate Records
- Invalid Data
- Summary Statistics

Example Output:

```
CUSTOMERS

Missing Values : 0

Duplicate IDs : 0

Invalid Email : 0

Validation Passed
```

---

# Logging

Log files generated:

- etl.log
- validation.log
- errors.log

Purpose:

- Track ETL execution
- Record validation issues
- Capture runtime errors

---

# Error Handling

The ETL pipeline handles:

- Missing files
- Database connection failures
- Duplicate primary keys
- Foreign key violations
- Data type mismatches
- Invalid values

Errors are logged for troubleshooting.

---

# Automation

The ETL process can be automated using:

- Python Scheduler
- Windows Task Scheduler
- Cron Jobs (Linux)

Execution Flow:

```
Generate Data
      ↓
Validate
      ↓
Load Database
      ↓
Run SQL Reports
      ↓
Refresh Power BI
```

---

# ETL Performance

Dataset Processed

- Customers: 20,000
- Accounts: 30,000
- Transactions: 500,000
- Loans: 10,000
- Merchants: 5,000
- Branches: 120

Optimizations

- Batch Inserts
- SQLAlchemy Engine
- Indexed Tables
- Efficient Data Types

---

# Technologies Used

- Python
- Pandas
- NumPy
- SQLAlchemy
- PostgreSQL
- Psycopg2

---

# Conclusion

The ETL pipeline ensures high-quality, validated, and consistent banking data is loaded into PostgreSQL. The processed data serves as the foundation for SQL reporting, Python analytics, and Power BI dashboards.


# Module 7 – Data Validation

## Objective

The purpose of this module is to validate the quality and integrity of the data after it has been loaded into PostgreSQL.

---

## Validation Checks Performed

### 1. Missing Values
Verified that the Customers, Accounts, and Transactions tables contain no NULL values in required columns.

**Result:** Passed

---

### 2. Duplicate Records
Checked for duplicate rows in all major tables.

**Result:** Passed

---

### 3. Foreign Key Validation
Verified that every transaction references a valid account.

**Result:** Passed

---

### 4. Negative Transaction Amounts
Checked that no transactions contain negative amounts.

**Result:** Passed

---

## Validation Summary

| Validation | Status |
|------------|--------|
| Missing Values | ✅ Passed |
| Duplicate Records | ✅ Passed |
| Foreign Key Integrity | ✅ Passed |
| Negative Amount Validation | ✅ Passed |

**Overall Status:** All validations passed successfully.