from faker import Faker
import pandas as pd
import random

# -------------------------------------
# Configuration
# -------------------------------------

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

# Load master datasets
customers = pd.read_csv("datasets/raw/customers.csv")
branches = pd.read_csv("datasets/raw/branches.csv")

TOTAL_CUSTOMERS = len(customers)
TOTAL_BRANCHES = len(branches)

TARGET_ACCOUNTS = 30000

accounts = []

account_number = 100000000001

# Track number of accounts generated
generated_accounts = 0

# Every customer gets at least 1 account.
# Around half will get a second account.
# A smaller number will get a third account.

for customer_id in range(1, TOTAL_CUSTOMERS + 1):

    if generated_accounts >= TARGET_ACCOUNTS:
        break

    no_of_accounts = random.choices(
        [1, 2, 3],
        weights=[50, 40, 10]
    )[0]

    for _ in range(no_of_accounts):

        if generated_accounts >= TARGET_ACCOUNTS:
            break

        account_type = random.choices(
            [1, 2, 3, 4],
            weights=[65, 20, 10, 5]
        )[0]

        # Balance based on account type
        if account_type == 1:      # Savings
            balance = random.randint(5000, 300000)

        elif account_type == 2:    # Current
            balance = random.randint(20000, 1500000)

        elif account_type == 3:    # Salary
            balance = random.randint(0, 250000)

        else:                      # Fixed Deposit
            balance = random.randint(50000, 5000000)

        open_date = fake.date_between(
            start_date="-10y",
            end_date="today"
        )

        last_txn = fake.date_between(
            start_date=open_date,
            end_date="today"
        )

        account_status = random.choices(
            ["Active", "Inactive"],
            weights=[95, 5]
        )[0]

        accounts.append({

            "account_number": str(account_number),

            "customer_id": customer_id,

            "branch_id": random.randint(
                1,
                TOTAL_BRANCHES
            ),

            "account_type_id": account_type,

            "balance": balance,

            "open_date": open_date,

            "account_status": account_status,

            "last_transaction_date": last_txn

        })

        account_number += 1
        generated_accounts += 1

# Convert to DataFrame
df = pd.DataFrame(accounts)

# Save CSV
df.to_csv(
    "datasets/raw/accounts.csv",
    index=False
)

print("=" * 60)
print("Accounts Generated Successfully")
print("=" * 60)
print(df.head())
print()
print("Total Accounts :", len(df))