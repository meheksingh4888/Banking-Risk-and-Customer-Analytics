from faker import Faker
import pandas as pd
import random
from datetime import timedelta

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

# Load Customers
customers = pd.read_csv("datasets/raw/customers.csv")

cards = []

NUMBER_OF_CARDS = 15000

card_types = [
    "Visa",
    "MasterCard",
    "RuPay",
    "American Express"
]

for i in range(1, NUMBER_OF_CARDS + 1):

    customer_id = random.randint(1, len(customers))

    credit_limit = random.choice([
        50000,
        100000,
        200000,
        500000,
        1000000
    ])

    outstanding = random.randint(0, credit_limit)

    due_date = fake.date_between(
        start_date="today",
        end_date="+60d"
    )

    card = {

        "customer_id": customer_id,

        "card_number": str(fake.unique.random_number(digits=16)),

        "card_type": random.choice(card_types),

        "credit_limit": credit_limit,

        "outstanding_amount": outstanding,

        "due_date": due_date

    }

    cards.append(card)

df = pd.DataFrame(cards)

df.to_csv(
    "datasets/raw/credit_cards.csv",
    index=False
)

print(df.head())

print("\n✅ credit_cards.csv generated successfully!")