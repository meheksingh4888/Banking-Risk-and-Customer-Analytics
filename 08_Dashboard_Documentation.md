# Power BI Dashboard Documentation

## Project

**Banking Risk Customer Analytics Dashboard**

---

# Introduction

The Banking Risk Customer Analytics Dashboard is developed using Microsoft Power BI to provide real-time business insights into customers, accounts, transactions, loans, branches, merchants, and financial risk.

The dashboard helps executives, managers, and analysts monitor banking operations through interactive visualizations and KPIs.

---

# Dashboard Objectives

- Monitor banking performance
- Analyze customer behavior
- Identify financial risks
- Track branch performance
- Monitor transaction activities
- Analyze loan portfolio
- Support data-driven decision making

---

# Data Source

Database:

PostgreSQL

Database Name:

Banking_Risk_Customer_Analytics

Connection:

Power BI PostgreSQL Connector

---

# Dashboard Pages

## 1. Executive Dashboard

KPIs

- Total Customers
- Total Accounts
- Total Deposits
- Total Loans
- Total Transactions
- Failed Transactions
- Average Credit Score
- Loan Defaults

Charts

- Customer Distribution
- Monthly Transactions
- Loan Portfolio
- Branch Performance

---

## 2. Customer Dashboard

Visualizations

- Gender Distribution
- Customer by State
- Customer by City
- Income Distribution
- Credit Score Analysis
- Customer Status

KPIs

- Total Customers
- Average Income
- Average Credit Score

---

## 3. Account Dashboard

Visualizations

- Account Type Distribution
- Account Balance Distribution
- Dormant Accounts
- Branch-wise Accounts

KPIs

- Total Accounts
- Total Deposits
- Average Balance

---

## 4. Transaction Dashboard

Visualizations

- Monthly Transactions
- Transaction Channels
- Transaction Status
- Device Analysis
- International Transactions

KPIs

- Total Transactions
- Transaction Amount
- Failed Transactions

---

## 5. Loan Dashboard

Visualizations

- Loan Type Distribution
- Loan Status
- EMI Analysis
- Interest Rate Analysis
- Default Customers

KPIs

- Total Loans
- Loan Portfolio
- Average Interest Rate

---

## 6. Branch Dashboard

Visualizations

- Branch Ranking
- Branch Deposits
- Customer Count
- Loan Distribution

KPIs

- Total Branches
- Branch Deposits
- Branch Loans

---

## 7. Merchant Dashboard

Visualizations

- Merchant Categories
- Merchant Revenue
- Merchant Transactions
- Top Merchants

KPIs

- Total Merchants
- Total Revenue

---

## 8. Risk Dashboard

Visualizations

- High Risk Customers
- Loan Defaults
- Failed Transactions
- International Transactions
- Fraud Analysis

KPIs

- Fraud Rate
- Default Rate
- Risk Customers

---

# Power BI Features Used

- KPI Cards
- Bar Charts
- Column Charts
- Line Charts
- Pie Charts
- Donut Charts
- Matrix Tables
- Maps
- Slicers
- Drill Through
- Tooltips
- Bookmarks
- Navigation Buttons

---

# Filters

The dashboard supports filtering by:

- State
- City
- Branch
- Account Type
- Loan Type
- Loan Status
- Transaction Status
- Merchant Category
- Year
- Month

---

# DAX Measures

Examples

Total Customers

```
Total Customers = COUNT(customers[customer_id])
```

Total Deposits

```
Total Deposits = SUM(accounts[balance])
```

Average Credit Score

```
Average Credit Score = AVERAGE(customers[credit_score])
```

Loan Portfolio

```
Loan Portfolio = SUM(loans[loan_amount])
```

Failed Transactions

```
Failed Transactions =
CALCULATE(
COUNT(transactions[transaction_id]),
transactions[status]="Failed"
)
```

---

# Business Insights

The dashboard enables users to:

- Monitor branch performance
- Identify high-value customers
- Track loan defaults
- Analyze transaction trends
- Monitor fraud indicators
- Evaluate customer risk
- Compare branch profitability
- Analyze merchant performance

---

# Performance Optimization

Techniques Used

- Star Schema
- Data Modeling
- Relationships
- DAX Measures
- Query Optimization
- Aggregations
- Slicers
- Drill Through

---

# Benefits

- Interactive Reporting
- Real-Time Analysis
- Faster Decision Making
- Better Risk Monitoring
- Executive-Level Reporting
- Improved Customer Analytics

---

# Conclusion

The Power BI dashboard transforms raw banking data into interactive business intelligence reports. It enables executives, analysts, and managers to monitor performance, identify risks, and make informed decisions using data-driven insights.