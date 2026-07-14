# Database Normalization

## Project

**Banking Risk Customer Analytics**

---

# Introduction

Database normalization is the process of organizing data to eliminate redundancy, improve data integrity, and optimize database performance.

This project follows normalization principles up to the Third Normal Form (3NF).

---

# First Normal Form (1NF)

## Rules

- Each column contains atomic (single) values.
- No repeating groups.
- Each row is uniquely identified by a primary key.

### Implementation

All tables have unique primary keys.

Examples:

- customer_id
- account_id
- transaction_id
- loan_id
- merchant_id
- branch_id

Each field stores only one value.

Example:

| customer_id | first_name | state |
|-------------|------------|--------|
| 101 | Rahul | Maharashtra |

There are no multiple values stored in a single column.

---

# Second Normal Form (2NF)

## Rules

- Must satisfy 1NF.
- Every non-key column depends on the entire primary key.

### Implementation

Each table has a single-column primary key.

For example:

### Customers

customer_id → first_name, last_name, annual_income, credit_score

### Accounts

account_id → customer_id, balance, account_type_id

### Transactions

transaction_id → account_id, merchant_id, amount, status

There are no partial dependencies.

---

# Third Normal Form (3NF)

## Rules

- Must satisfy 2NF.
- No transitive dependencies.

### Implementation

Lookup information is stored in separate master tables.

Examples:

### Account Types

account_type_id → account_type_name

Instead of storing:

Savings

Current

Salary

inside the Accounts table repeatedly, only the ID is stored.

---

### Loan Types

loan_type_id → loan_type_name

Loan descriptions are stored in the Loan Types table.

---

### Branches

Branch information is stored only once.

Accounts reference branches using:

branch_id

instead of repeating branch names for every account.

---

### Merchants

Merchant information is stored in a separate Merchant table.

Transactions reference merchants using:

merchant_id

This eliminates duplicate merchant information.

---

# Database Relationships

Customers (1) --------< Accounts

Accounts (1) --------< Transactions

Customers (1) --------< Loans

Branches (1) --------< Accounts

Merchants (1) --------< Transactions

Account Types (1) --------< Accounts

Loan Types (1) --------< Loans

---

# Benefits of Normalization

- Eliminates duplicate data
- Improves storage efficiency
- Reduces update anomalies
- Maintains referential integrity
- Simplifies maintenance
- Improves query performance
- Supports scalable database design

---

# Conclusion

The Banking Risk Customer Analytics database is designed according to Third Normal Form (3NF), ensuring efficient storage, reduced redundancy, and strong data integrity suitable for analytical reporting and business intelligence.

Question 1 :--

Can one customer have multiple accounts?

Yes.

So :-

Customers

customer_id

name

↓

Accounts

customer_id

instead of :-

Accounts

customer_name

customer_city

customer_phone

This avoids repeating customer details.