from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

# =====================================
# Configuration
# =====================================

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

NUMBER_OF_TRANSACTIONS = 500000

# =====================================
# Load CSV Files
# =====================================

accounts = pd.read_csv("datasets/raw/accounts.csv")
merchants = pd.read_csv("datasets/raw/merchants.csv")

TOTAL_ACCOUNTS = len(accounts)
TOTAL_MERCHANTS = len(merchants)

transactions = []

reference_number = 100000000000

transaction_type_ids = [
    1,   # Deposit
    2,   # Withdrawal
    3,   # Transfer
    5,   # UPI
    6,   # Debit Card
    7,   # Credit Card
    8,   # NEFT
    9,   # RTGS
    10,  # IMPS
    11,  # ATM Withdrawal
    12,  # Cash Deposit
    13   # POS Purchase
]

channels = [
    "UPI",
    "ATM",
    "Mobile Banking",
    "Internet Banking",
    "Branch",
    "POS",
    "NEFT",
    "RTGS",
    "IMPS"
]

device_types = [
    "Android",
    "iPhone",
    "ATM",
    "POS Machine",
    "Laptop",
    "Desktop"
]

status_list = [
    "Success",
    "Success",
    "Success",
    "Success",
    "Success",
    "Pending",
    "Failed"
]

currencies = [
    "INR",
    "USD",
    "EUR"
]

cities = [
    "Mumbai",
    "Delhi",
    "Pune",
    "Bengaluru",
    "Hyderabad",
    "Ahmedabad",
    "Jaipur",
    "Chennai",
    "Lucknow",
    "Kolkata"
]

print("Generating Transactions...")

for i in range(NUMBER_OF_TRANSACTIONS):

    account = accounts.sample(1).iloc[0]

    account_id = int(account.name) + 1

    current_balance = float(account["balance"])

    transaction_type = random.choice(transaction_type_ids)

    amount = round(
        random.uniform(50,50000),
        2
    )

    transaction_date = fake.date_time_between(
        start_date="-5y",
        end_date="now"
    )
    merchant = merchants.sample(1).iloc[0]

    merchant_id = int(merchant.name) + 1

    # -----------------------------
    # Balance Calculation
    # -----------------------------

    if transaction_type in [2, 3, 5, 6, 7, 8, 9, 10, 11, 13]:

        balance_after = max(
            current_balance - amount,
            0
        )

    else:

        balance_after = current_balance + amount

    # -----------------------------
    # Transaction Status
    # -----------------------------

    status = random.choices(

        ["Success", "Pending", "Failed"],

        weights=[94, 4, 2]

    )[0]

    # -----------------------------
    # Channel
    # -----------------------------

    channel = random.choice(channels)

    # -----------------------------
    # Device
    # -----------------------------

    device = random.choice(device_types)

    # -----------------------------
    # International Transaction
    # -----------------------------

    is_international = random.choices(

        [True, False],

        weights=[2, 98]

    )[0]

    # -----------------------------
    # Currency
    # -----------------------------

    if is_international:

        currency = random.choice(

            ["USD", "EUR", "GBP", "AED"]

        )

    else:

        currency = "INR"

    # -----------------------------
    # City
    # -----------------------------

    city = random.choice(cities)

    # -----------------------------
    # Reference Number
    # -----------------------------

    reference = f"TXN{reference_number}"

    reference_number += 1

    # -----------------------------
    # Append Transaction
    # -----------------------------

    transactions.append({

        "account_id": account_id,

        "merchant_id": merchant_id,

        "transaction_type_id": transaction_type,

        "transaction_date": transaction_date,

        "amount": amount,

        "balance_after_transaction": round(balance_after,2),

        "channel": channel,

        "transaction_city": city,

        "device_type": device,

        "status": status,

        "is_international": is_international,

        "currency": currency,

        "reference_number": reference

    })

    if (i + 1) % 50000 == 0:

        print(f"{i+1:,} transactions generated...")

    # =====================================
# Create DataFrame
# =====================================

df = pd.DataFrame(transactions)

# =====================================
# Save CSV
# =====================================

output_path = "datasets/raw/transactions.csv"

df.to_csv(
    output_path,
    index=False
)

# =====================================
# Summary
# =====================================

print("\n" + "=" * 60)
print("Transactions Generated Successfully")
print("=" * 60)

print(f"Total Transactions : {len(df):,}")
print(f"Output File        : {output_path}")

print("\nSample Data:\n")
print(df.head())

print("\nTransaction Status Distribution:")
print(df["status"].value_counts())

print("\nChannel Distribution:")
print(df["channel"].value_counts())

print("\nInternational Transactions:")
print(df["is_international"].value_counts())

print("=" * 60)