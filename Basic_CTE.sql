01_basic_cte.sql
Customers earning above average income
WITH avg_income AS
(
SELECT AVG(annual_income) avg_salary
FROM customers
)

SELECT
customer_id,
first_name,
annual_income
FROM customers
WHERE annual_income >
(
SELECT avg_salary
FROM avg_income
);
Accounts above average balance
WITH avg_balance AS
(
SELECT AVG(balance) avg_bal
FROM accounts
)

SELECT
account_id,
balance
FROM accounts
WHERE balance >
(
SELECT avg_bal
FROM avg_balance
);
02_customer_analysis.sql
Total balance of every customer
WITH customer_balance AS
(
SELECT

customer_id,

SUM(balance) total_balance

FROM accounts

GROUP BY customer_id
)

SELECT

c.customer_id,

c.first_name,

cb.total_balance

FROM customers c

JOIN customer_balance cb

ON c.customer_id=cb.customer_id

ORDER BY total_balance DESC;
Customers having multiple accounts
WITH account_count AS
(
SELECT

customer_id,

COUNT(*) total_accounts

FROM accounts

GROUP BY customer_id
)

SELECT *

FROM account_count

WHERE total_accounts>1;
03_account_analysis.sql
Branch average balance
WITH branch_balance AS
(
SELECT

branch_id,

AVG(balance) avg_balance

FROM accounts

GROUP BY branch_id
)

SELECT

a.account_id,

a.branch_id,

a.balance,

bb.avg_balance

FROM accounts a

JOIN branch_balance bb

ON a.branch_id=bb.branch_id;
Highest balance account per branch
WITH ranked_accounts AS
(
SELECT

branch_id,

account_id,

balance,

ROW_NUMBER()

OVER(

PARTITION BY branch_id

ORDER BY balance DESC

) rn

FROM accounts
)

SELECT *

FROM ranked_accounts

WHERE rn=1;
04_transaction_analysis.sql
Monthly transactions
WITH monthly_transactions AS
(
SELECT

DATE_TRUNC('month',transaction_date) month,

COUNT(*) total_transactions,

SUM(amount) total_amount

FROM transactions

GROUP BY month
)

SELECT *

FROM monthly_transactions

ORDER BY month;
Failed transaction summary
WITH failed_transactions AS
(
SELECT *

FROM transactions

WHERE status='Failed'
)

SELECT

account_id,

COUNT(*) failures

FROM failed_transactions

GROUP BY account_id;
05_loan_analysis.sql
Loan portfolio by type
WITH loan_summary AS
(
SELECT

loan_type,

SUM(loan_amount) portfolio

FROM loans

GROUP BY loan_type
)

SELECT *

FROM loan_summary

ORDER BY portfolio DESC;
High-risk loans
WITH avg_interest AS
(
SELECT AVG(interest_rate) avg_rate
FROM loans
)

SELECT

loan_id,

customer_id,

loan_amount,

interest_rate

FROM loans

WHERE interest_rate >

(
SELECT avg_rate

FROM avg_interest
);
06_branch_analysis.sql
Branch deposits
WITH deposits AS
(
SELECT

branch_id,

SUM(balance) total_deposits

FROM accounts

GROUP BY branch_id
)

SELECT

b.branch_name,

d.total_deposits

FROM branches b

JOIN deposits d

ON b.branch_id=d.branch_id;
Branch customer count
WITH customer_count AS
(
SELECT

branch_id,

COUNT(DISTINCT customer_id) customers

FROM accounts

GROUP BY branch_id
)

SELECT

b.branch_name,

cc.customers

FROM branches b

JOIN customer_count cc

ON b.branch_id=cc.branch_id;
07_multiple_ctes.sql
WITH deposits AS
(
SELECT

branch_id,

SUM(balance) deposits

FROM accounts

GROUP BY branch_id
),

loans AS
(
SELECT

branch_id,

SUM(loan_amount) loans

FROM loans

GROUP BY branch_id
)

SELECT

b.branch_name,

d.deposits,

l.loans

FROM branches b

LEFT JOIN deposits d

ON b.branch_id=d.branch_id

LEFT JOIN loans l

ON b.branch_id=l.branch_id;
08_cte_vs_subquery.sql
Using CTE
WITH avg_balance AS
(
SELECT AVG(balance) avg_bal
FROM accounts
)

SELECT *

FROM accounts

WHERE balance >

(
SELECT avg_bal

FROM avg_balance
);
Equivalent Subquery
SELECT *

FROM accounts

WHERE balance >

(
SELECT AVG(balance)

FROM accounts
);
09_business_cases.sql
Top 10 richest customers
WITH customer_balance AS
(
SELECT

customer_id,

SUM(balance) total_balance

FROM accounts

GROUP BY customer_id
)

SELECT

c.customer_id,

c.first_name,

cb.total_balance

FROM customers c

JOIN customer_balance cb

ON c.customer_id=cb.customer_id

ORDER BY cb.total_balance DESC

LIMIT 10;
Top transaction city
WITH city_transactions AS
(
SELECT

transaction_city,

SUM(amount) total_amount

FROM transactions

GROUP BY transaction_city
)

SELECT *

FROM city_transactions

ORDER BY total_amount DESC;
10_recursive_preparation.sql

This file prepares you for the next topic.

-- Simple recursive number generation

WITH RECURSIVE numbers AS
(
SELECT 1 AS n

UNION ALL

SELECT n+1

FROM numbers

WHERE n<10
)

SELECT *

FROM numbers;