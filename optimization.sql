Phase 7 — SQL Performance Optimization

01_indexes.sql
Create indexes
CREATE INDEX idx_customer_city
ON customers(city);
CREATE INDEX idx_account_customer
ON accounts(customer_id);
CREATE INDEX idx_transaction_date
ON transactions(transaction_date);
CREATE INDEX idx_transaction_status
ON transactions(status);
CREATE INDEX idx_transaction_account
ON transactions(account_id);
CREATE INDEX idx_loan_customer
ON loans(customer_id);
CREATE INDEX idx_branch_city
ON branches(city);
Composite Index
CREATE INDEX idx_transactions_account_date
ON transactions(account_id,transaction_date);

Useful for

SELECT *
FROM transactions
WHERE account_id=101
AND transaction_date>=CURRENT_DATE-30;
Unique Index
CREATE UNIQUE INDEX idx_reference
ON transactions(reference_number);

02_explain_analyze.sql

Check query execution.

EXPLAIN ANALYZE

SELECT *
FROM transactions
WHERE account_id=1500;

Look for

Seq Scan
Index Scan
Bitmap Scan

Large query

EXPLAIN ANALYZE

SELECT
c.customer_name,
SUM(t.amount)

FROM customers c

JOIN accounts a
ON c.customer_id=a.customer_id

JOIN transactions t
ON a.account_id=t.account_id

GROUP BY c.customer_name;


03_query_tuning.sql
Bad Query
SELECT *
FROM transactions
WHERE EXTRACT(YEAR FROM transaction_date)=2025;

Uses Sequential Scan.

Better

SELECT *
FROM transactions
WHERE transaction_date>='2025-01-01'
AND transaction_date<'2026-01-01';

Now PostgreSQL can use the index.

Avoid

SELECT *
FROM customers;

Instead

SELECT
customer_id,
customer_name,
credit_score
FROM customers;

Use EXISTS instead of IN

Bad

SELECT *

FROM customers

WHERE customer_id IN
(
SELECT customer_id
FROM loans
);

Better

SELECT *

FROM customers c

WHERE EXISTS
(
SELECT 1

FROM loans l

WHERE l.customer_id=c.customer_id
);


04_materialized_views.sql

Create summary table.

CREATE MATERIALIZED VIEW monthly_transactions AS

SELECT

DATE_TRUNC('month',transaction_date) month,

COUNT(*) total_transactions,

SUM(amount) total_amount

FROM transactions

GROUP BY DATE_TRUNC('month',transaction_date);

View data

SELECT *
FROM monthly_transactions;

Refresh

REFRESH MATERIALIZED VIEW monthly_transactions;


05_partitioning.sql

Example

CREATE TABLE transactions_2025
PARTITION OF transactions

FOR VALUES FROM ('2025-01-01')

TO ('2026-01-01');

Benefits

Faster queries
Faster backups
Easy archival


06_best_practices.sql

Avoid

SELECT *

Always

SELECT customer_id,
customer_name

Avoid functions on indexed columns.

Bad

UPPER(customer_name)

Create indexes on

Foreign Keys
Frequently searched columns
Join columns

Use LIMIT

SELECT *

FROM transactions

LIMIT 100;

Always check

EXPLAIN ANALYZE

before optimizing.

Folder Structure
optimization/

01_indexes.sql

02_explain_analyze.sql

03_query_tuning.sql

04_materialized_views.sql

05_partitioning.sql

06_best_practices.sql
What you have completed

Your SQL portfolio now covers:

sql_queries/

basic/
✓ SELECT
✓ WHERE
✓ ORDER BY
✓ GROUP BY
✓ HAVING

intermediate/
✓ JOIN
✓ CASE
✓ Subqueries
✓ Correlated Subqueries

advanced/
✓ Business Analytics
✓ Fraud Detection
✓ Customer Segmentation
✓ KPIs

window_functions/
✓ ROW_NUMBER()
✓ RANK()
✓ DENSE_RANK()
✓ LAG()
✓ LEAD()
✓ Running Totals

cte/
✓ Common Table Expressions

recursive_cte/
✓ Hierarchies
✓ Recursive Reports

optimization/
✓ Indexes
✓ EXPLAIN ANALYZE
✓ Query Tuning
✓ Materialized Views
✓ Partitioning