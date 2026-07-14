from faker import Faker
import pandas as pd
import random

# ---------------------------------------
# Configuration
# ---------------------------------------

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

NUMBER_OF_EMPLOYEES = 1000
TOTAL_BRANCHES = 120

designations = [
    "Branch Manager",
    "Assistant Manager",
    "Relationship Manager",
    "Cashier",
    "Loan Officer",
    "Customer Service Executive",
    "Operations Executive",
    "Sales Executive",
    "Credit Analyst",
    "IT Support Officer"
]

salary_range = {
    "Branch Manager": (90000, 180000),
    "Assistant Manager": (60000, 100000),
    "Relationship Manager": (45000, 80000),
    "Cashier": (25000, 45000),
    "Loan Officer": (40000, 75000),
    "Customer Service Executive": (25000, 45000),
    "Operations Executive": (30000, 55000),
    "Sales Executive": (25000, 50000),
    "Credit Analyst": (50000, 85000),
    "IT Support Officer": (40000, 70000)
}

employees = []

for employee_id in range(1, NUMBER_OF_EMPLOYEES + 1):

    designation = random.choice(designations)

    min_salary, max_salary = salary_range[designation]

    employees.append({

        "employee_id": employee_id,

        "branch_id": random.randint(1, TOTAL_BRANCHES),

        "employee_name": fake.name(),

        "designation": designation,

        "salary": random.randint(min_salary, max_salary),

        "hire_date": fake.date_between(
            start_date="-20y",
            end_date="today"
        )

    })

df = pd.DataFrame(employees)

df.to_csv(
    "datasets/raw/employees.csv",
    index=False
)

print("=" * 60)
print("Employees Generated Successfully")
print("=" * 60)
print(df.head())
print()
print("Total Employees :", len(df))