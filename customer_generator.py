from faker import Faker
import pandas as pd
import random

# --------------------------------
# Faker Configuration
# --------------------------------

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

NUMBER_OF_CUSTOMERS = 20000

customers = []

male_first_names = [
    "Aarav","Vivaan","Aditya","Arjun","Krishna","Rohan","Rahul","Akash","Karan","Raj",
    "Mohit","Rishi","Aman","Ayush","Shivam","Varun","Siddharth","Manav","Ritik","Nikhil"
]

female_first_names = [
    "Aanya","Ananya","Priya","Neha","Pooja","Riya","Sneha","Anjali","Kavya","Diya",
    "Meera","Ishita","Nandini","Sakshi","Simran","Shreya","Khushi","Muskan","Radhika","Aditi"
]

last_names = [
    "Sharma","Singh","Patel","Verma","Gupta","Yadav","Joshi","Kapoor","Mishra","Mehta",
    "Agarwal","Jain","Kulkarni","Nair","Reddy","Chauhan","Bose","Das","Iyer","Pandey"
]

cities = [
    "Mumbai","Delhi","Bengaluru","Hyderabad","Pune","Ahmedabad","Chennai",
    "Kolkata","Jaipur","Lucknow","Indore","Nagpur","Surat","Patna",
    "Bhopal","Noida","Gurgaon","Kochi","Chandigarh","Kanpur"
]

states = {
    "Mumbai":"Maharashtra",
    "Delhi":"Delhi",
    "Bengaluru":"Karnataka",
    "Hyderabad":"Telangana",
    "Pune":"Maharashtra",
    "Ahmedabad":"Gujarat",
    "Chennai":"Tamil Nadu",
    "Kolkata":"West Bengal",
    "Jaipur":"Rajasthan",
    "Lucknow":"Uttar Pradesh",
    "Indore":"Madhya Pradesh",
    "Nagpur":"Maharashtra",
    "Surat":"Gujarat",
    "Patna":"Bihar",
    "Bhopal":"Madhya Pradesh",
    "Noida":"Uttar Pradesh",
    "Gurgaon":"Haryana",
    "Kochi":"Kerala",
    "Chandigarh":"Punjab",
    "Kanpur":"Uttar Pradesh"
}

for i in range(1, NUMBER_OF_CUSTOMERS + 1):

    gender = random.choice(["Male","Female"])

    if gender == "Male":
        first_name = random.choice(male_first_names)
    else:
        first_name = random.choice(female_first_names)

    last_name = random.choice(last_names)

    city = random.choice(cities)

    customer = {

        "customer_code": f"CUST{i:06}",

        "first_name": first_name,

        "last_name": last_name,

        "gender": gender,

        "date_of_birth": fake.date_of_birth(
            minimum_age=18,
            maximum_age=75
        ),

        "email": f"{first_name.lower()}.{last_name.lower()}{i}@gmail.com",

        "phone": str(random.randint(6000000000,9999999999)),

        "city": city,

        "state": states[city],

        "annual_income": random.randint(
            250000,
            3000000
        ),

        "credit_score": random.randint(
            300,
            900
        ),

        "join_date": fake.date_between(
            start_date="-10y",
            end_date="today"
        ),

        "customer_status": random.choices(
            ["Active","Inactive"],
            weights=[90,10]
        )[0]

    }

    customers.append(customer)

df = pd.DataFrame(customers)

df.to_csv(
    "datasets/raw/customers.csv",
    index=False
)

print("="*60)
print("Customers Generated Successfully")
print("="*60)
print(df.head())
print()
print("Total Customers :",len(df))