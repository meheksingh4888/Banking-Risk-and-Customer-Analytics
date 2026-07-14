# SQL Documentation

## Project

**Banking Risk Customer Analytics**

---

# Overview

This project uses PostgreSQL as the backend database.

The SQL implementation covers:

- Database Design
- Constraints
- Views
- Materialized Views
- Functions
- Stored Procedures
- Triggers
- Transactions
- Indexes
- Query Optimization
- Analytical SQL

---

# Database Tables

## Master Tables

Customers

Accounts

Account Types

Transactions

Loan Types

Loans

Branches

Merchants

---

# Relationships

Customers → Accounts

Accounts → Transactions

Customers → Loans

Branches → Accounts

Merchants → Transactions

Loan Types → Loans

Account Types → Accounts

---

# SQL Modules

## Basic SQL

Topics Covered

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- GROUP BY
- HAVING
- Aggregate Functions

Examples

- Total Customers
- Total Accounts
- Average Balance
- Loan Amount
- Merchant Count

---

## Intermediate SQL

Topics Covered

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- CASE
- Subqueries
- Correlated Subqueries

Business Examples

Customer Accounts

Customer Loans

Branch Performance

Merchant Revenue

Risk Customers

---

## Advanced SQL

Topics Covered

- Multi-table JOIN
- Complex Aggregations
- Business KPIs
- Conditional Aggregation
- CASE Expressions

Business Reports

Executive Dashboard

Branch Dashboard

Risk Dashboard

Customer Dashboard

Loan Dashboard

Merchant Dashboard

---

## Window Functions

Implemented Functions

ROW_NUMBER()

RANK()

DENSE_RANK()

LAG()

LEAD()

SUM() OVER()

AVG() OVER()

Business Examples

Top Customers

Monthly Running Balance

Branch Ranking

Loan Ranking

Transaction Ranking

Moving Average

---

## Common Table Expressions (CTEs)

Topics

Simple CTE

Multiple CTE

Nested CTE

Business Examples

Risk Analysis

Customer Summary

Branch Performance

Loan Summary

Merchant Analysis

---

## Recursive CTE

Topics

Hierarchy

Recursive Queries

Running Levels

Business Example

Organizational Hierarchy

Recursive Tree Structure

---

# Database Views

Views Created

Customer Summary View

Account Summary View

Transaction Summary View

Loan Summary View

Branch Performance View

Merchant Performance View

Risk Summary View

Purpose

Simplify reporting queries.

---

# Materialized Views

Materialized Views

Monthly Transaction Summary

Branch Summary

Loan Portfolio Summary

Merchant Revenue Summary

Benefits

Fast reporting

Reduced query execution time

Dashboard optimization

---

# Functions

Functions Developed

Maximum Salary

Total Salary

Customer Risk Score

Loan EMI Calculator

Branch Deposit Summary

Purpose

Reusable business logic.

---

# Stored Procedures

Procedures Implemented

Insert Customer

Update Customer

Delete Customer

Loan Processing

Transaction Processing

Account Closing

Benefits

Centralized business rules.

---

# Database Triggers

Triggers Implemented

Audit Log

Automatic Timestamp

Balance Validation

Loan Status Update

Transaction Validation

Purpose

Maintain data integrity automatically.

---

# Transactions

Transaction Control Statements

BEGIN

COMMIT

ROLLBACK

SAVEPOINT

Business Examples

Fund Transfer

Loan Approval

Deposit

Withdrawal

---

# Indexes

Indexes Created

Customer ID

Account Number

Transaction Date

Merchant ID

Branch ID

Loan Status

Purpose

Improve query performance.

---

# Query Optimization

Techniques Used

EXPLAIN ANALYZE

Indexes

Proper JOIN strategy

Filtering before Aggregation

Avoiding unnecessary SELECT *

Materialized Views

Performance Improvements

Reduced execution time

Lower I/O cost

Better scalability

---

# SQL Business Reports

Reports Developed

Customer Analysis

Account Analysis

Transaction Analysis

Loan Analysis

Branch Analysis

Merchant Analysis

Risk Analysis

Executive Dashboard

---

# Conclusion

The SQL implementation covers everything from basic querying to advanced analytical SQL using PostgreSQL. The project demonstrates database design, optimization, reporting, and business intelligence techniques commonly used in enterprise banking systems.