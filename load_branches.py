import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    r"C:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\datasets\raw\branches.csv"
)

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

df.to_sql("branches", engine, if_exists="append", index=False)

print("Branches loaded successfully!")