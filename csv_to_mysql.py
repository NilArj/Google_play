import pandas as pd
import glob, os
from sqlalchemy import create_engine

for file in glob.glob("*.csv"):
  df = pd.read_csv(file)
  
  engine = create_engine("mysql+pymysql://root:***@localhost:3306/project")
  
  df.to_sql(file[:-4], engine, index=False)
  
  print("CSV to database created successfully")