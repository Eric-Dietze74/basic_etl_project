#Import Statements
import pandas as pd
import sqlite3
import logging

logging.basicConfig(
    filename='logs/extract.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_to_sqlite(df_tuple):
    #db_list = ["db/big_df.db", "db/day_month_df.db","db/hour_df.db", "db/location_df.db"]
    table_names = []
    db_name_list = ["all_transactions_df", "day_month_df","hour_df", "location_df"]
  
    
    if len(df_tuple) != len(db_name_list) :
        logging.error("ERROR: db_list and df_tuple aren't the same length")
     
    
    conn = sqlite3.connect("../data/project.db")
   
    for idx in range(len(df_tuple)):
        df_tuple[idx].to_sql(db_name_list[idx], conn, if_exists = "replace", index = False)
        
    conn.close()