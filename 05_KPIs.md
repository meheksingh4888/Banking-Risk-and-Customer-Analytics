# Key Performance Indicators (KPIs)

## Project

**Banking Risk Customer Analytics**

---

# Introduction

Key Performance Indicators (KPIs) help management monitor the bank's performance, customer behavior, financial health, operational efficiency, and business risks.

The following KPIs are implemented using SQL, Python, and Power BI.

---

# Customer KPIs

### Total Customers

Definition:
Total number of registered customers.

Formula:
COUNT(customer_id)

---

### Active Customers

Definition:
Customers whose status is Active.

Formula:
COUNT(customer_id WHERE customer_status='Active')

---

### Average Credit Score

Definition:
Average credit score of all customers.

Formula:
AVG(credit_score)

---

### High Risk Customers

Definition:
Customers with low credit scores and loan defaults.

Business Purpose:
Identify customers likely to default on future loans.

---

# Account KPIs

### Total Accounts

Definition:
Total number of bank accounts.

Formula:
COUNT(account_id)

---

### Total Deposits

Definition:
Total balance across all customer accounts.

Formula:
SUM(balance)

---

### Average Account Balance

Formula:
AVG(balance)

---

### Dormant Accounts

Definition:
Accounts with no recent transaction activity.

Business Purpose:
Identify inactive customers for re-engagement campaigns.

---

### Account Type Distribution

Measures:

- Savings Accounts
- Current Accounts
- Salary Accounts
- Fixed Deposit Accounts

---

# Transaction KPIs

### Total Transactions

Formula:
COUNT(transaction_id)

---

### Total Transaction Amount

Formula:
SUM(amount)

---

### Average Transaction Amount

Formula:
AVG(amount)

---

### Successful Transactions

Formula:
COUNT(status='Success')

---

### Failed Transactions

Formula:
COUNT(status='Failed')

---

### Pending Transactions

Formula:
COUNT(status='Pending')

---

### International Transactions

Formula:
COUNT(is_international=True)

---

### Monthly Transaction Trend

Business Purpose:
Track transaction growth over time.

---

### Channel Performance

Includes:

- UPI
- ATM
- POS
- RTGS
- NEFT
- IMPS
- Mobile Banking
- Internet Banking
- Branch

---

# Loan KPIs

### Loan Portfolio

Formula:
SUM(loan_amount)

---

### Average Loan Amount

Formula:
AVG(loan_amount)

---

### Average Interest Rate

Formula:
AVG(interest_rate)

---

### Loan Status Distribution

Includes:

- Active
- Closed
- Defaulted

---

### Default Customers

Formula:
COUNT(default_flag=True)

---

### Outstanding Loan Amount

Formula:
SUM(outstanding_balance)

---

### Remaining Loan Balance

Formula:
SUM(remaining_balance)

---

# Branch KPIs

### Total Branches

Formula:
COUNT(branch_id)

---

### Branch-wise Customers

Business Purpose:
Measure customer distribution across branches.

---

### Branch Deposits

Formula:
SUM(balance)

---

### Branch Loan Portfolio

Formula:
SUM(loan_amount)

---

### Branch Performance Ranking

Business Purpose:
Rank branches based on deposits, customers, and loans.

---

# Merchant KPIs

### Total Merchants

Formula:
COUNT(merchant_id)

---

### Merchant Revenue

Formula:
SUM(transaction amount)

---

### Merchant Category Distribution

Examples:

- Pharmacy
- Restaurant
- Fuel
- Shopping
- Electronics
- Utilities
- Hospital

---

### Top Performing Merchants

Business Purpose:
Identify merchants generating the highest transaction volume and revenue.

---

# Fraud & Risk KPIs

### Fraud Transactions

Definition:
Transactions marked as Failed.

---

### Fraud Rate

Formula:

(Failed Transactions / Total Transactions) × 100

---

### High Risk Customers

Criteria:

- Credit Score < 500
- Defaulted Loan

---

### International Transaction Rate

Formula:

(International Transactions / Total Transactions) × 100

---

# Executive Dashboard KPIs

The Power BI Executive Dashboard displays:

- Total Customers
- Total Accounts
- Total Deposits
- Total Loans
- Total Transactions
- Failed Transactions
- International Transactions
- Average Credit Score
- Loan Defaults
- Top States
- Branch Performance
- Monthly Transaction Trend

---

# Conclusion

These KPIs provide a comprehensive view of banking operations, customer risk, financial performance, and branch efficiency. They support data-driven decision-making for executives, risk managers, and business analysts.
Customer KPIs
Total Customers
Active Customers
Dormant Customers
High-Value Customers
Customer Lifetime Value
Average Credit Score
Account KPIs
Total Accounts
Average Account Balance
Deposit Growth
Withdrawal Growth
Loan KPIs
Total Loans
Outstanding Loan Amount
Default Rate
Loan Approval Rate
Transaction KPIs
Total Transactions
Monthly Transaction Growth
Average Transaction Amount
Peak Transaction Volume
Fraud KPIs
Fraud Cases
Fraud Amount
High-Risk Locations
Fraud Detection Rate
Branch KPIs
Branch Revenue
Branch Deposits
Branch Loan Amount
Customer Count
Average Balance
Step 7: Business Questions

These are the questions our SQL queries and dashboards must answer.

Customer Analytics
Who are the top 100 customers by balance?
Which customers are most profitable?
Which customers are inactive?
Which customers are likely to default?
Branch Analytics
Which branches perform best?
Which branches have the highest deposits?
Which branches have the highest loan defaults?
Loan Analytics
Which loan type has the highest default rate?
Which loan type generates the highest revenue?
Fraud Analytics
Which cities have the most fraud?
Which devices are associated with fraud?
Which merchants have the highest fraud count?
Transaction Analytics
How do monthly transactions change over time?
What are the busiest transaction hours?
What is the average transaction amount by branch?