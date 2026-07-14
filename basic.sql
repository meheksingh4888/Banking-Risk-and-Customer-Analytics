-- ==========================================
-- BASIC SELECT QUERIES
-- ==========================================

-- View all customers
SELECT *
FROM customers;

-- View all accounts
SELECT *
FROM accounts;

-- View all transactions
SELECT *
FROM transactions;

-- View all branches
SELECT *
FROM branches;

-- View first 20 customers
SELECT *
FROM customers
LIMIT 20;

-- Customer names only
SELECT
first_name,
last_name
FROM customers;

-- Customer city and state
SELECT
customer_id,
city,
state
FROM customers;

-- Accounts with balances
SELECT
account_number,
balance
FROM accounts;

-- Transactions
SELECT
transaction_date,
amount,
transaction_type
FROM transactions;

-- Merchant IDs
SELECT DISTINCT merchant_id
FROM transactions;


Step 1: Customer Analysis


1. Total Customers

SELECT COUNT(*) AS total_customers
FROM customers;

2. Male vs Female Customers
SELECT
    gender,
    COUNT(*) AS total_customers
FROM customers
GROUP BY gender
ORDER BY total_customers DESC;

3. Customers by State
SELECT
    state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY state
ORDER BY total_customers DESC;

4. Top 10 Cities by Customers
SELECT
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC
LIMIT 10;

5. Average Credit Score
SELECT
    ROUND(AVG(credit_score),2) AS average_credit_score
FROM customers;

6. Highest Credit Score
SELECT
    first_name,
    last_name,
    credit_score
FROM customers
ORDER BY credit_score DESC
LIMIT 10;

7. Income Distribution
SELECT
    CASE
        WHEN annual_income < 300000 THEN 'Low'
        WHEN annual_income BETWEEN 300000 AND 700000 THEN 'Middle'
        ELSE 'High'
    END AS income_group,
    COUNT(*) AS customers
FROM customers
GROUP BY income_group;

8. Average Income by State
SELECT
    state,
    ROUND(AVG(annual_income),2) AS avg_income
FROM customers
GROUP BY state
ORDER BY avg_income DESC;

9. New Customers per Year
SELECT
    EXTRACT(YEAR FROM join_date) AS join_year,
    COUNT(*) AS customers
FROM customers
GROUP BY join_year
ORDER BY join_year;

10. Top 20 High Income Customers
SELECT
    customer_id,
    first_name,
    last_name,
    annual_income
FROM customers
ORDER BY annual_income DESC
LIMIT 20;

Revenue
Deposits
Loan Distribution
Customer Count
Branch Rankings


📄 02_account_analysis.sql

1. Total Accounts
SELECT COUNT(*) AS total_accounts
FROM accounts;

2. Savings vs Current Accounts
SELECT
    account_type,
    COUNT(*) AS total_accounts
FROM accounts
GROUP BY account_type
ORDER BY total_accounts DESC;

3. Active vs Inactive Accounts
SELECT
    account_status,
    COUNT(*) AS total_accounts
FROM accounts
GROUP BY account_status;

4. Dormant Accounts
SELECT
    account_id,
    customer_id,
    account_type,
    balance
FROM accounts
WHERE account_status='Dormant';

5. Total Balance by Account Type
SELECT
    account_type,
    SUM(balance) AS total_balance
FROM accounts
GROUP BY account_type;

6. Average Balance
SELECT
    ROUND(AVG(balance),2) AS average_balance
FROM accounts;

7. Top 20 Richest Accounts
SELECT
    account_id,
    customer_id,
    balance
FROM accounts
ORDER BY balance DESC
LIMIT 20;

8. Negative Balance Detection
SELECT *
FROM accounts
WHERE balance < 0;

9. Branch-wise Accounts
SELECT
    b.branch_name,
    COUNT(a.account_id) AS total_accounts
FROM accounts a
JOIN branches b
ON a.branch_id=b.branch_id
GROUP BY b.branch_name
ORDER BY total_accounts DESC;

10. Average Balance per Branch
SELECT
    b.branch_name,
    ROUND(AVG(a.balance),2) AS avg_balance
FROM accounts a
JOIN branches b
ON a.branch_id=b.branch_id
GROUP BY b.branch_name
ORDER BY avg_balance DESC;


📄 03_transaction_analysis.sql
1. Total Transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;

2. Total Transaction Amount
SELECT
SUM(amount) AS total_amount
FROM transactions;

3. Transaction Type Analysis
SELECT
transaction_type,
COUNT(*) AS total_transactions,
SUM(amount) AS total_amount
FROM transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;

4. Monthly Transactions
SELECT
DATE_TRUNC('month',transaction_date) AS month,
COUNT(*) AS transactions,
SUM(amount) AS amount
FROM transactions
GROUP BY month
ORDER BY month;

5. Failed Transactions
SELECT
status,
COUNT(*) AS total
FROM transactions
GROUP BY status;

6. International Transactions
SELECT
COUNT(*) AS international_transactions
FROM transactions
WHERE is_international=TRUE;

7. Channel Analysis
SELECT
channel,
COUNT(*) AS total_transactions,
SUM(amount) AS total_amount
FROM transactions
GROUP BY channel
ORDER BY total_amount DESC;

8. Device Analysis
SELECT
device_type,
COUNT(*) AS total_transactions
FROM transactions
GROUP BY device_type
ORDER BY total_transactions DESC;

9. Top 20 Merchants
SELECT
m.merchant_name,
COUNT(*) AS transactions,
SUM(t.amount) AS revenue
FROM transactions t
JOIN merchants m
ON t.merchant_id=m.merchant_id
GROUP BY m.merchant_name
ORDER BY revenue DESC
LIMIT 20;

10. Top Transaction Cities
SELECT
transaction_city,
COUNT(*) AS total_transactions
FROM transactions
GROUP BY transaction_city
ORDER BY total_transactions DESC;


📄 04_loan_analysis.sql
1. Loan Portfolio
SELECT
SUM(loan_amount) AS total_loan_portfolio
FROM loans;

2. Loan Status
SELECT
loan_status,
COUNT(*) AS total_loans
FROM loans
GROUP BY loan_status;

3. Average Loan Amount
SELECT
ROUND(AVG(loan_amount),2) AS average_loan
FROM loans;

4. Loan Type Distribution
SELECT
loan_type,
COUNT(*) AS total_loans
FROM loans
GROUP BY loan_type
ORDER BY total_loans DESC;

5. EMI Analysis
SELECT
ROUND(AVG(emi_amount),2) AS average_emi
FROM loans;

6. Highest EMI Loans
SELECT
loan_id,
customer_id,
emi_amount
FROM loans
ORDER BY emi_amount DESC
LIMIT 20;

7. Interest Rate Analysis
SELECT
loan_type,
ROUND(AVG(interest_rate),2) AS avg_interest
FROM loans
GROUP BY loan_type;

8. High Risk Customers
SELECT
customer_id,
loan_amount,
interest_rate
FROM loans
WHERE interest_rate >
(
SELECT AVG(interest_rate)
FROM loans
);

9. Total Outstanding Loan Amount
SELECT
SUM(outstanding_balance) AS outstanding_amount
FROM loans;

10. Top 20 Largest Loans
SELECT
loan_id,
customer_id,
loan_amount
FROM loans
ORDER BY loan_amount DESC
LIMIT 20;

📄 05_branch_analysis.sql
1. Total Branches
SELECT COUNT(*) AS total_branches
FROM branches;

2. Customers per Branch
SELECT
b.branch_name,
COUNT(DISTINCT a.customer_id) AS customers
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name
ORDER BY customers DESC;

3. Accounts per Branch
SELECT
b.branch_name,
COUNT(a.account_id) AS accounts
FROM branches b
LEFT JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name;

4. Branch Deposits
SELECT
b.branch_name,
SUM(a.balance) AS total_deposits
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name
ORDER BY total_deposits DESC;

5. Branch Loan Portfolio
SELECT
b.branch_name,
SUM(l.loan_amount) AS total_loans
FROM branches b
JOIN loans l
ON b.branch_id=l.branch_id
GROUP BY b.branch_name
ORDER BY total_loans DESC;

6. Average Account Balance
SELECT
b.branch_name,
ROUND(AVG(a.balance),2) AS average_balance
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name
ORDER BY average_balance DESC;

7. Top Performing Branches
SELECT
b.branch_name,
SUM(a.balance) AS deposits,
COUNT(DISTINCT a.customer_id) AS customers
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name
ORDER BY deposits DESC;

8. Transactions per Branch
SELECT
b.branch_name,
COUNT(t.transaction_id) AS transactions
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
JOIN transactions t
ON a.account_id=t.account_id
GROUP BY b.branch_name
ORDER BY transactions DESC;

9. Revenue by Branch (Transaction Volume)
SELECT
b.branch_name,
SUM(t.amount) AS transaction_volume
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
JOIN transactions t
ON a.account_id=t.account_id
GROUP BY b.branch_name
ORDER BY transaction_volume DESC;

10. Branch Ranking
SELECT
b.branch_name,
SUM(a.balance) AS total_deposits
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name
ORDER BY total_deposits DESC;