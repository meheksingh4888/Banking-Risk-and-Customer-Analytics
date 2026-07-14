import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\DATASETS\RAW\customers.csv")

engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

df.to_sql("customers", engine, if_exists="append", index=False)

print("Data loaded successfully")