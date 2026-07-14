import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\sakas\SQL PROJECTS\📁 Banking-Risk-Customer-Analytics\DATASETS\RAW\accounts.csv")


engine = create_engine(
    "postgresql+psycopg2://postgres:root@localhost:5432/Banking_Risk_Customer_Analytics"
)

# ✅ ADD THIS FIX

valid_branches = pd.read_sql("SELECT branch_id FROM branches", engine)

df = df[df['branch_id'].isin(valid_branches['branch_id'])].reset_index(drop=True)

# load into DB
df.to_sql("accounts", engine, if_exists="append", index=False,chunksize=500)