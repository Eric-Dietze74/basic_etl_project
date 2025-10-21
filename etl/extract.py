#Import Statement 

import pandas as pd
import os
import logging
from datetime import datetime 


#Setting Up Logging
logging.basicConfig(
    filename='logs/extract.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Required Columns, Data Path, and Staging Path 
Required_Columns = ["TransactionID", "AccountID", "TransactionAmount", "AccountBalance", "TransactionDate"]
Raw_Data_Path = "../data/bank_transactions_data_2.csv"
Staging_Path = "../data/staging_customers.csv"

def validate_columns(df, required_columns):
    
    #Check if all required columns are present.
    
    missing = [col for col in Required_Columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def remove_duplicates(df):
    #Remove duplicate rows based on TransactionID.
    return df.drop_duplicates(subset='TransactionID')

def extract_customers(file_path=Raw_Data_Path):
    
    
    #Extract raw customer data with staging and validation.
    
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")

        df = pd.read_csv(file_path)

        validate_columns(df, Required_Columns)

        df = remove_duplicates(df)

        # Save to staging area
        df.to_csv(Staging_Path, index=False)
        logging.info(f"Extracted and staged {len(df)} records successfully.")

        return df
    
    
    
    except Exception as e:
        logging.error(f"Error during extraction: {e}")
        raise