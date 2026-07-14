from faker import Faker
import pandas as pd
import random
from datetime import timedelta

# ---------------------------------------
# Configuration
# ---------------------------------------

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

NUMBER_OF_LOANS = 10000

# ---------------------------------------
# Load Customers
# ---------------------------------------

customers = pd.read_csv("datasets/raw/customers.csv")

TOTAL_CUSTOMERS = len(customers)

loan_types = {
    1: "Home Loan",
    2: "Personal Loan",
    3: "Car Loan",
    4: "Education Loan",
    5: "Business Loan"
}

loans = []

for i in range(1, NUMBER_OF_LOANS + 1):

    customer_id = random.randint(1, TOTAL_CUSTOMERS)

    loan_type_id = random.randint(1, 5)

    # Loan amount based on type
    if loan_type_id == 1:      # Home
        loan_amount = random.randint(1000000, 10000000)

    elif loan_type_id == 2:    # Personal
        loan_amount = random.randint(50000, 1500000)

    elif loan_type_id == 3:    # Car
        loan_amount = random.randint(300000, 2500000)

    elif loan_type_id == 4:    # Education
        loan_amount = random.randint(100000, 3000000)

    else:                      # Business
        loan_amount = random.randint(500000, 20000000)

    interest_rate = round(random.uniform(7.0, 15.5), 2)

    tenure = random.choice([
        12,
        24,
        36,
        48,
        60,
        84,
        120,
        180,
        240,
        360
    ])

    emi_amount = round(loan_amount / tenure, 2)

    start_date = fake.date_between(
        start_date="-10y",
        end_date="today"
    )

    end_date = start_date + timedelta(days=tenure * 30)

    default_flag = random.choices(
        [True, False],
        weights=[8, 92]
    )[0]

    loans.append({

        "customer_id": customer_id,

        "loan_type_id": loan_type_id,

        "loan_amount": loan_amount,

        "interest_rate": interest_rate,

        "tenure_months": tenure,

        "emi_amount": emi_amount,

        "loan_start_date": start_date,

        "loan_end_date": end_date,

        "default_flag": default_flag

    })

df = pd.DataFrame(loans)

df.to_csv(
    "datasets/raw/loans.csv",
    index=False
)

print("=" * 60)
print("Loans Generated Successfully")
print("=" * 60)
print(df.head())
print()
print("Total Loans :", len(df))