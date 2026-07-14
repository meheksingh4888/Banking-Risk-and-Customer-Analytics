from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

Faker.seed(100)
random.seed(100)

NUMBER_OF_MERCHANTS = 5000

merchant_categories = {

    "Supermarket": [
        "D-Mart","Reliance Fresh","Big Bazaar","More","Spencer's"
    ],

    "Restaurant": [
        "Domino's","Pizza Hut","KFC","McDonald's","Burger King"
    ],

    "Cafe": [
        "Starbucks","Cafe Coffee Day","Barista"
    ],

    "Fuel": [
        "Indian Oil","HP Petrol Pump","Bharat Petroleum","Shell"
    ],

    "Pharmacy": [
        "Apollo Pharmacy","MedPlus","Wellness Forever"
    ],

    "Electronics": [
        "Croma","Reliance Digital","Vijay Sales"
    ],

    "Shopping": [
        "Amazon","Flipkart","Myntra","Ajio","Meesho"
    ],

    "Fashion": [
        "Pantaloons","Lifestyle","Zudio","Westside","Max Fashion"
    ],

    "Hospital": [
        "Apollo Hospital","Fortis","Max Hospital","Medanta"
    ],

    "Travel": [
        "IRCTC","MakeMyTrip","Yatra","Goibibo"
    ],

    "Entertainment": [
        "PVR","INOX","BookMyShow"
    ],

    "Utilities": [
        "Electricity Board","Water Supply","Gas Agency"
    ]

}

cities = [
    ("Mumbai","Maharashtra"),
    ("Delhi","Delhi"),
    ("Bengaluru","Karnataka"),
    ("Hyderabad","Telangana"),
    ("Pune","Maharashtra"),
    ("Ahmedabad","Gujarat"),
    ("Chennai","Tamil Nadu"),
    ("Kolkata","West Bengal"),
    ("Jaipur","Rajasthan"),
    ("Lucknow","Uttar Pradesh"),
    ("Indore","Madhya Pradesh"),
    ("Nagpur","Maharashtra"),
    ("Surat","Gujarat"),
    ("Patna","Bihar"),
    ("Bhopal","Madhya Pradesh"),
    ("Noida","Uttar Pradesh"),
    ("Gurgaon","Haryana"),
    ("Kochi","Kerala"),
    ("Chandigarh","Punjab"),
    ("Kanpur","Uttar Pradesh")
]

merchants = []

for i in range(1, NUMBER_OF_MERCHANTS + 1):

    category = random.choice(list(merchant_categories.keys()))

    merchant_name = (
        random.choice(merchant_categories[category])
        + " "
        + str(i)
    )

    city, state = random.choice(cities)

    merchants.append({

        "merchant_name": merchant_name,

        "merchant_category": category,

        "city": city,

        "state": state

    })

df = pd.DataFrame(merchants)

df.to_csv(
    "datasets/raw/merchants.csv",
    index=False
)

print("=" * 60)
print("Merchants Generated Successfully")
print("=" * 60)
print(df.head())
print()
print("Total Merchants :", len(df))