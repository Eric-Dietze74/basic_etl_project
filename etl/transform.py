#Import Statement 

import extract
import pandas as pd
from datetime import datetime

new_df = extract.extract_customers()

def transform_df(df):
    
    #Changing Variable from String to DateTime
    df["TransactionDate"] = pd.to_datetime(df.TransactionDate)
    
    #Creating a new Variable that shows what day of the week it is 
    df["TransactionDayofWeek"] = df.TransactionDate.dt.day_name()
    
    
    #The previous transaction date variable seems to be messed up, with all
        #"previous" transactions coming AFTER the transaction on the same row
        #Typically, this would justify auditing this data
        #However, because this is practice data from a csv we will just drop the column 
    df = df.drop(["PreviousTransactionDate"], axis = 1)


    #Creating a new Variable that shows what hour of the month, day and hour it is. 
        #Will allow for some better data analysis breakdowns 
    df["TransactionHour"] = df.TransactionDate.dt.hour

    df["TransactionMonth"] = df.TransactionDate.dt.month

    df["TransactionDay"] = df.TransactionDate.dt.day

    #Get rid of any errant spaces
    df.columns = df.columns.str.replace(' ', '')
    
    return df

def Aggregate_Transaction_Amt(Group_by_Cols_list, df):
    return pd.DataFrame(df.groupby(by = Group_by_Cols_list)['TransactionAmount'].sum())


def Return_dfs(df):
    df = transform_df(df)
    
    month_day_df = Aggregate_Transaction_Amt(["TransactionMonth", "TransactionDay"], df)
    
    hour_df = Aggregate_Transaction_Amt(["TransactionHour"], df)
    
    location_df = Aggregate_Transaction_Amt(["Location"], df)
    
    return df, month_day_df, hour_df, location_df