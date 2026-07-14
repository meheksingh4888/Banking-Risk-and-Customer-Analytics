from faker import Faker
import pandas as pd
import random

# ---------------------------------------
# Configuration
# ---------------------------------------

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

FRAUD_PERCENTAGE = 1  # 1% of transactions

# ---------------------------------------
# Load Transactions
# ---------------------------------------

transactions = pd.read_csv("datasets/raw/transactions.csv")

total_transactions = len(transactions)

number_of_frauds = int(total_transactions * FRAUD_PERCENTAGE / 100)

# Randomly select unique transactions
fraud_transactions = transactions.sample(
    n=number_of_frauds,
    random_state=100
)

fraud_types = [
    "Card Skimming",
    "Phishing",
    "Identity Theft",
    "Suspicious Transfer",
    "Money Laundering",
    "Duplicate Transaction",
    "Account Takeover",
    "Fake Merchant",
    "High Value Withdrawal",
    "International Fraud"
]

investigation_status = [
    "Open",
    "Under Investigation",
    "Resolved",
    "Closed"
]

fraud_alerts = []

fraud_id = 1

for _, row in fraud_transactions.iterrows():

    fraud_alerts.append({

        "fraud_id": fraud_id,

        "transaction_id": int(row.name) + 1,

        "fraud_type": random.choice(fraud_types),

        "risk_score": random.randint(60,100),

        "detected_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),

        "investigation_status": random.choice(
            investigation_status
        )

    })

    fraud_id += 1

df = pd.DataFrame(fraud_alerts)

df.to_csv(
    "datasets/raw/fraud_alerts.csv",
    index=False
)

print("=" * 60)
print("Fraud Alerts Generated Successfully")
print("=" * 60)
print(df.head())
print()
print("Total Fraud Alerts :", len(df))