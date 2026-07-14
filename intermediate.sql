📂 sql_queries/intermediate/

Create these files:

sql_queries/
│
├── intermediate/
│   ├── 01_customer_account_analysis.sql
│   ├── 02_customer_loan_analysis.sql
│   ├── 03_transaction_analysis.sql
│   ├── 04_branch_performance.sql
│   ├── 05_fraud_analysis.sql
│   ├── 06_subqueries.sql
│   ├── 07_case_having.sql
│   └── 08_correlated_subqueries.sql
📄 01_customer_account_analysis.sql

1. Customers with their account details
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    a.account_id,
    a.account_type,
    a.balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id;

2. Customers having multiple accounts
SELECT
    customer_id,
    COUNT(*) AS total_accounts
FROM accounts
GROUP BY customer_id
HAVING COUNT(*) > 1
ORDER BY total_accounts DESC;

3. Top 20 customers by total balance
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_balance DESC
LIMIT 20;

4. Customers without accounts
SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customers c
LEFT JOIN accounts a
ON c.customer_id = a.customer_id
WHERE a.account_id IS NULL;

📄 02_customer_loan_analysis.sql

1. Customers with loans
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    l.loan_amount
FROM customers c
JOIN loans l
ON c.customer_id = l.customer_id;

2. Customers with multiple loans
SELECT
    customer_id,
    COUNT(*) AS total_loans
FROM loans
GROUP BY customer_id
HAVING COUNT(*) > 1;

3. Customers whose loan is above average
SELECT
    customer_id,
    loan_amount
FROM loans
WHERE loan_amount >
(
SELECT AVG(loan_amount)
FROM loans
);

4. High-income customers with loans
SELECT
    c.customer_id,
    c.first_name,
    c.annual_income,
    l.loan_amount
FROM customers c
JOIN loans l
ON c.customer_id = l.customer_id
WHERE c.annual_income > 1000000;

📄 03_transaction_analysis.sql

1. Customers with highest transaction amount
SELECT
    c.customer_id,
    c.first_name,
    SUM(t.amount) AS total_transactions
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
JOIN transactions t
ON a.account_id = t.account_id
GROUP BY
    c.customer_id,
    c.first_name
ORDER BY total_transactions DESC
LIMIT 20;

2. Failed transactions
SELECT *
FROM transactions
WHERE status <> 'Success';

3. Merchant-wise transaction volume
SELECT
    m.merchant_name,
    COUNT(*) AS total_transactions,
    SUM(t.amount) AS total_amount
FROM merchants m
JOIN transactions t
ON m.merchant_id = t.merchant_id
GROUP BY m.merchant_name
ORDER BY total_amount DESC;

📄 04_branch_performance.sql
Branch deposits
SELECT
    b.branch_name,
    SUM(a.balance) AS deposits
FROM branches b
JOIN accounts a
ON b.branch_id = a.branch_id
GROUP BY b.branch_name
ORDER BY deposits DESC;

Branch loan portfolio
SELECT
    b.branch_name,
    SUM(l.loan_amount) AS total_loans
FROM branches b
JOIN loans l
ON b.branch_id = l.branch_id
GROUP BY b.branch_name
ORDER BY total_loans DESC;

📄 05_fraud_analysis.sql
Large transactions (> ₹5,00,000)
SELECT
    transaction_id,
    amount,
    transaction_city,
    device_type
FROM transactions
WHERE amount > 500000;


International transactions
SELECT *
FROM transactions
WHERE is_international = TRUE;


Pending transactions
SELECT *
FROM transactions
WHERE status = 'Pending';

📄 06_subqueries.sql
Customers above average income
SELECT
    customer_id,
    annual_income
FROM customers
WHERE annual_income >
(
SELECT AVG(annual_income)
FROM customers
);


Accounts above average balance
SELECT
    account_id,
    balance
FROM accounts
WHERE balance >
(
SELECT AVG(balance)
FROM accounts
);

📄 07_case_having.sql
Income groups
SELECT
CASE
WHEN annual_income <300000 THEN 'Low'
WHEN annual_income<800000 THEN 'Middle'
ELSE 'High'
END AS income_group,
COUNT(*) AS customers
FROM customers
GROUP BY income_group;


States having more than 500 customers
SELECT
state,
COUNT(*) AS customers
FROM customers
GROUP BY state
HAVING COUNT(*)>500;


📄 08_correlated_subqueries.sql

Customers richer than the average income of their state
SELECT
customer_id,
first_name,
annual_income,
state
FROM customers c1
WHERE annual_income >
(
SELECT AVG(c2.annual_income)
FROM customers c2
WHERE c1.state=c2.state
);

Accounts with balance above the average balance of their branch

SELECT
account_id,
branch_id,
balance
FROM accounts a1
WHERE balance >
(
SELECT AVG(a2.balance)
FROM accounts a2
WHERE a1.branch_id=a2.branch_id
);