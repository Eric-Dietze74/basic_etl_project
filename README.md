# Basic ETL Project

This project demonstrates a foundational understanding of ETL (Extract, Transform, Load) processes using Python, Pandas, and SQLite.

---

## Repository Contents

### 1. `data` Directory

#### a. `Bank_transactions_data_2.csv`
- Dataset sourced from Kaggle that can be found using the following [link](#).
- Intended for fraud detection model development.
- Used as the raw input for the ETL process.

#### b. `staging_customers.csv`
- File created when running the extraction step.
- Serves as the staging area for cleaned and validated data.

#### c. `project.db`
- SQLite database file created when running the full ETL pipeline.
- Stores all transformed and aggregated data tables.

---

### 2. `etl` Directory

#### a. `Extract.py`
- Extracts and validates raw transaction data from a specified CSV file by ensuring all required columns exist and removing duplicate transactions.
- Stages the cleaned dataset by saving it to a designated staging file path and logs the process and any errors encountered.
  
#### b. `Transform.py`
- Transforms and cleans the extracted transaction data by converting date fields, created new time-based variables (month, day, hour, weekday), and removing invalid or unnecessary columns 
- Aggregates transaction amounts across multiple dimensions (by month/day, hour and location) to produce summary DataFrames for further analysis

#### c. `Load.py`
- Loads transformed DataFrames into a SQLite database by writing each DataFrame to its corresponding table within a single project database file
- Implements basic error logging and validation to ensure the number of DataFrames matches the expected table names before saving

#### d. `run_etl.py`
- Runs extract.py, transform.py, and load.py

#### e. `logs` Directory
- Contains the extract.log file which should keep a track of any logging throughout the etl process

## How to Run
#### 1. Clone the repository
#### 2. Verifying that CSV (bank_transactions_data_2.csv) is located in the data/ directory
#### 3. Navigate to the etl/ directory
#### 4. Run the ETL pipeline with "python run_etl.py"





