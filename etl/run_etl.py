#Import statements
import extract
import transform
import load

if __name__ == "__main__":
    raw = extract.extract_customers()
    df_tuple = transform.Return_dfs(raw)
    load.load_to_sqlite(df_tuple)
    print("ETL Successful")