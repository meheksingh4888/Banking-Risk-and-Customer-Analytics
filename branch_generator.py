from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

NUMBER_OF_BRANCHES = 120

cities = [
    ("Mumbai", "Maharashtra"),
    ("Pune", "Maharashtra"),
    ("Nagpur", "Maharashtra"),
    ("Nashik", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Noida", "Uttar Pradesh"),
    ("Lucknow", "Uttar Pradesh"),
    ("Kanpur", "Uttar Pradesh"),
    ("Jaipur", "Rajasthan"),
    ("Udaipur", "Rajasthan"),
    ("Ahmedabad", "Gujarat"),
    ("Surat", "Gujarat"),
    ("Vadodara", "Gujarat"),
    ("Bengaluru", "Karnataka"),
    ("Mysuru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Warangal", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Coimbatore", "Tamil Nadu"),
    ("Madurai", "Tamil Nadu"),
    ("Kolkata", "West Bengal"),
    ("Siliguri", "West Bengal"),
    ("Patna", "Bihar"),
    ("Ranchi", "Jharkhand"),
    ("Bhopal", "Madhya Pradesh"),
    ("Indore", "Madhya Pradesh"),
    ("Raipur", "Chhattisgarh"),
    ("Bhubaneswar", "Odisha"),
    ("Kochi", "Kerala"),
    ("Thiruvananthapuram", "Kerala"),
    ("Chandigarh", "Punjab"),
    ("Amritsar", "Punjab"),
    ("Guwahati", "Assam"),
    ("Shillong", "Meghalaya"),
    ("Dehradun", "Uttarakhand"),
    ("Jammu", "Jammu & Kashmir")
]

manager_first = [
    "Rahul","Amit","Rohit","Neha","Priya","Anjali","Karan",
    "Vikas","Pooja","Sneha","Aditya","Riya","Sakshi",
    "Aarav","Vivek","Nikhil","Manish","Akash","Meera","Diya"
]

manager_last = [
    "Sharma","Patel","Singh","Gupta","Verma","Mehta","Kapoor",
    "Jain","Joshi","Kulkarni","Yadav","Das","Bose","Nair"
]

branches = []

for i in range(1, NUMBER_OF_BRANCHES + 1):

    city, state = random.choice(cities)

    branch = {

        "branch_code": f"BR{i:04}",

        "branch_name": f"{city} Branch",

        "city": city,

        "state": state,

        "manager_name": random.choice(manager_first) + " " + random.choice(manager_last),

        "employee_count": random.randint(25,150),

        "opening_date": fake.date_between(
            start_date="-25y",
            end_date="-1y"
        )

    }

    branches.append(branch)

df = pd.DataFrame(branches)

df.to_csv(
    "datasets/raw/branches.csv",
    index=False
)

print("="*60)
print("Branches Generated Successfully")
print("="*60)
print(df.head())
print()
print("Total Branches :", len(df))