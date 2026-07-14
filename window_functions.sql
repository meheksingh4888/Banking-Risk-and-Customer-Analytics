01_row_number.sql
Latest transaction per account
SELECT *
FROM
(
    SELECT
        transaction_id,
        account_id,
        amount,
        transaction_date,
        ROW_NUMBER() OVER(
            PARTITION BY account_id
            ORDER BY transaction_date DESC
        ) rn
    FROM transactions
)t
WHERE rn=1;
Top account in every branch
SELECT *
FROM
(
SELECT
branch_id,
account_id,
balance,
ROW_NUMBER() OVER(
PARTITION BY branch_id
ORDER BY balance DESC
) rn
FROM accounts
)t
WHERE rn=1;
02_rank.sql
Highest balance ranking
SELECT
account_id,
balance,
RANK() OVER(
ORDER BY balance DESC
) ranking
FROM accounts;
Customer income ranking
SELECT
customer_id,
annual_income,
RANK() OVER(
ORDER BY annual_income DESC
) ranking
FROM customers;
03_dense_rank.sql
SELECT
customer_id,
credit_score,
DENSE_RANK() OVER(
ORDER BY credit_score DESC
) credit_rank
FROM customers;
Rank customers inside every state
SELECT
customer_id,
state,
annual_income,

DENSE_RANK() OVER(

PARTITION BY state

ORDER BY annual_income DESC

) income_rank

FROM customers;
04_ntile.sql
Divide customers into 4 income groups
SELECT

customer_id,

annual_income,

NTILE(4)

OVER(

ORDER BY annual_income

) income_quartile

FROM customers;
Divide accounts into 10 groups
SELECT

account_id,

balance,

NTILE(10)

OVER(

ORDER BY balance DESC

)

FROM accounts;
05_running_total.sql
Running transaction amount
SELECT

transaction_id,

account_id,

transaction_date,

amount,

SUM(amount)

OVER(

PARTITION BY account_id

ORDER BY transaction_date

) running_total

FROM transactions;
Running deposits
SELECT

transaction_date,

SUM(amount)

OVER(

ORDER BY transaction_date

) total_amount

FROM transactions;
06_moving_average.sql
7-day moving average
SELECT

transaction_date,

amount,

AVG(amount)

OVER(

ORDER BY transaction_date

ROWS BETWEEN 6 PRECEDING

AND CURRENT ROW

)

AS moving_average

FROM transactions;
30 transaction average
SELECT

transaction_id,

amount,

AVG(amount)

OVER(

ORDER BY transaction_date

ROWS BETWEEN 29 PRECEDING

AND CURRENT ROW

)

FROM transactions;
07_lag.sql
Previous transaction
SELECT

transaction_id,

account_id,

transaction_date,

amount,

LAG(amount)

OVER(

PARTITION BY account_id

ORDER BY transaction_date

)

AS previous_amount

FROM transactions;
Previous balance
SELECT

account_id,

balance,

LAG(balance)

OVER(

ORDER BY account_id

)

FROM accounts;
08_lead.sql
Next transaction
SELECT

transaction_id,

account_id,

amount,

LEAD(amount)

OVER(

PARTITION BY account_id

ORDER BY transaction_date

)

AS next_amount

FROM transactions;
Next loan amount
SELECT

loan_id,

loan_amount,

LEAD(loan_amount)

OVER(

ORDER BY loan_amount

)

FROM loans;
09_first_last_value.sql
First transaction
SELECT

account_id,

transaction_date,

amount,

FIRST_VALUE(amount)

OVER(

PARTITION BY account_id

ORDER BY transaction_date

)

FROM transactions;
Last transaction
SELECT

account_id,

transaction_date,

amount,

LAST_VALUE(amount)

OVER(

PARTITION BY account_id

ORDER BY transaction_date

ROWS BETWEEN UNBOUNDED PRECEDING

AND UNBOUNDED FOLLOWING

)

FROM transactions;
10_percent_rank.sql
SELECT

customer_id,

annual_income,

PERCENT_RANK()

OVER(

ORDER BY annual_income

)

FROM customers;
11_cume_dist.sql
SELECT

customer_id,

credit_score,

CUME_DIST()

OVER(

ORDER BY credit_score

)

FROM customers;
12_business_cases.sql
Top 3 customers in every state
SELECT *
FROM
(
SELECT

customer_id,

first_name,

state,

annual_income,

ROW_NUMBER()

OVER(

PARTITION BY state

ORDER BY annual_income DESC

) rn

FROM customers

)t

WHERE rn<=3;
Top 5 branches by deposits
SELECT *
FROM
(
SELECT

branch_id,

SUM(balance) deposits,

RANK()

OVER(

ORDER BY SUM(balance) DESC

) ranking

FROM accounts

GROUP BY branch_id

)t

WHERE ranking<=5;
Running loan portfolio
SELECT

loan_id,

loan_amount,

SUM(loan_amount)

OVER(

ORDER BY loan_amount DESC

)

AS cumulative_portfolio

FROM loans;
Highest transaction in every city
SELECT *
FROM
(
SELECT

transaction_city,

transaction_id,

amount,

ROW_NUMBER()

OVER(

PARTITION BY transaction_city

ORDER BY amount DESC

)

rn

FROM transactions

)t

WHERE rn=1;