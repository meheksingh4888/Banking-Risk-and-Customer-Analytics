01_customer_360.sql
Complete Customer Profile
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.state,
    c.credit_score,
    c.annual_income,
    COUNT(DISTINCT a.account_id) AS total_accounts,
    COALESCE(SUM(a.balance),0) AS total_balance,
    COUNT(DISTINCT l.loan_id) AS total_loans,
    COALESCE(SUM(l.loan_amount),0) AS total_loan_amount
FROM customers c
LEFT JOIN accounts a
ON c.customer_id=a.customer_id
LEFT JOIN loans l
ON c.customer_id=l.customer_id
GROUP BY
c.customer_id,
c.first_name,
c.last_name,
c.city,
c.state,
c.credit_score,
c.annual_income
ORDER BY total_balance DESC;
Top Valuable Customers
SELECT
customer_id,
first_name,
last_name,
annual_income,
credit_score
FROM customers
ORDER BY annual_income DESC,credit_score DESC
LIMIT 20;
Customers with High Balance and Loan
SELECT
c.customer_id,
c.first_name,
SUM(a.balance) balance,
SUM(l.loan_amount) loans
FROM customers c
JOIN accounts a
ON c.customer_id=a.customer_id
JOIN loans l
ON c.customer_id=l.customer_id
GROUP BY c.customer_id,c.first_name
HAVING SUM(a.balance)>1000000
ORDER BY balance DESC;
02_branch_business_analysis.sql
Deposit vs Loan
SELECT
b.branch_name,
SUM(a.balance) deposits,
SUM(l.loan_amount) loans
FROM branches b
LEFT JOIN accounts a
ON b.branch_id=a.branch_id
LEFT JOIN loans l
ON b.branch_id=l.branch_id
GROUP BY b.branch_name;
Customers Per Branch
SELECT
b.branch_name,
COUNT(DISTINCT a.customer_id) customers
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
GROUP BY b.branch_name
ORDER BY customers DESC;
Branch Transaction Volume
SELECT
b.branch_name,
COUNT(t.transaction_id) transactions,
SUM(t.amount) volume
FROM branches b
JOIN accounts a
ON b.branch_id=a.branch_id
JOIN transactions t
ON a.account_id=t.account_id
GROUP BY b.branch_name
ORDER BY volume DESC;
03_loan_risk_analysis.sql
High Risk Loans
SELECT
loan_id,
customer_id,
loan_amount,
interest_rate
FROM loans
WHERE interest_rate>
(
SELECT AVG(interest_rate)
FROM loans
);
Default Percentage
SELECT
ROUND(
100.0*
SUM(CASE WHEN default_flag THEN 1 ELSE 0 END)
/
COUNT(*),2
) default_percentage
FROM loans;
Loan Distribution
SELECT
loan_type,
COUNT(*) total_loans,
SUM(loan_amount) portfolio
FROM loans
GROUP BY loan_type
ORDER BY portfolio DESC;
04_transaction_intelligence.sql
Monthly Transaction Trend
SELECT
DATE_TRUNC('month',transaction_date) month,
COUNT(*) total_transactions,
SUM(amount) amount
FROM transactions
GROUP BY month
ORDER BY month;
Highest Spending Cities
SELECT
transaction_city,
SUM(amount) spending
FROM transactions
GROUP BY transaction_city
ORDER BY spending DESC
LIMIT 20;
Merchant Revenue
SELECT
m.merchant_name,
SUM(t.amount) revenue
FROM merchants m
JOIN transactions t
ON m.merchant_id=t.merchant_id
GROUP BY m.merchant_name
ORDER BY revenue DESC
LIMIT 20;
05_customer_profitability.sql
Customer Lifetime Value
SELECT
c.customer_id,
c.first_name,
SUM(t.amount) transaction_value,
SUM(a.balance) deposits,
SUM(l.loan_amount) loans
FROM customers c
LEFT JOIN accounts a
ON c.customer_id=a.customer_id
LEFT JOIN transactions t
ON a.account_id=t.account_id
LEFT JOIN loans l
ON c.customer_id=l.customer_id
GROUP BY
c.customer_id,
c.first_name
ORDER BY transaction_value DESC;
06_executive_dashboard_queries.sql
Executive KPIs
SELECT

(SELECT COUNT(*) FROM customers) total_customers,

(SELECT COUNT(*) FROM accounts) total_accounts,

(SELECT COUNT(*) FROM loans) total_loans,

(SELECT COUNT(*) FROM transactions) total_transactions,

(SELECT SUM(balance) FROM accounts) deposits,

(SELECT SUM(loan_amount) FROM loans) loans,

(SELECT SUM(amount) FROM transactions) transaction_volume;
07_fraud_detection.sql
High Value Transactions
SELECT *
FROM transactions
WHERE amount>500000;
Multiple Failed Transactions
SELECT
account_id,
COUNT(*) failures
FROM transactions
WHERE status='Failed'
GROUP BY account_id
HAVING COUNT(*)>=3;
International Transactions
SELECT *
FROM transactions
WHERE is_international=TRUE;
08_cross_selling.sql
Customers Eligible for Loan
SELECT
customer_id,
first_name,
credit_score,
annual_income
FROM customers
WHERE credit_score>750
AND customer_id NOT IN
(
SELECT customer_id
FROM loans
);
Customers Eligible for Credit Card
SELECT
customer_id,
first_name,
annual_income
FROM customers
WHERE annual_income>1000000;
09_customer_segmentation.sql
SELECT
customer_id,
first_name,

CASE

WHEN annual_income<300000 THEN 'Low Income'

WHEN annual_income<800000 THEN 'Middle Income'

ELSE 'High Income'

END income_segment,

CASE

WHEN credit_score>=800 THEN 'Excellent'

WHEN credit_score>=700 THEN 'Good'

WHEN credit_score>=600 THEN 'Average'

ELSE 'Poor'

END credit_segment

FROM customers;
10_business_kpis.sql
SELECT

ROUND(AVG(balance),2) average_balance,

ROUND(AVG(loan_amount),2) average_loan,

ROUND(AVG(amount),2) average_transaction,

MAX(balance) highest_balance,

MAX(loan_amount) highest_loan,

MAX(amount) highest_transaction

FROM

accounts,
loans,
transactions;