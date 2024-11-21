import mysql.connector
import pandas as pd
import numpy as np

# Function to connect to the MySQL database
def connect_to_db(db_host, db_user, db_password, db_name):
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        return connection
    except mysql.connector.Error as err:
        return f"Error: {err}"

# Function to extract data from a specified table
def extract_data_from_table(connection, table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        data = pd.read_sql(query, connection)
        return data
    except Exception as e:
        return f"Error while fetching data: {e}"

# Function to detect fraud (analyzing commission-to-deposit ratio)
def detect_fraud(data):
    # Calculate Commission-to-Deposit Ratio
    data['commission_to_deposit_ratio'] = data['commission'] / data['deposit_amount']
    
    # Define an outlier detection rule for fraud (e.g., high ratio = potential fraud)
    fraud_threshold = 5  # Arbitrary threshold for demonstration
    fraud_data = data[data['commission_to_deposit_ratio'] > fraud_threshold]
    
    return fraud_data

# Function to detect churn behavior (based on user activity in the first month)
def detect_churn(data):
    # Assuming 'user_signup_date' and 'last_activity_date' exist in the dataset
    data['churn'] = np.where(pd.to_datetime(data['last_activity_date']) - pd.to_datetime(data['user_signup_date']) > pd.Timedelta(days=30), 1, 0)
    
    churn_data = data[data['churn'] == 1]
    return churn_data

# Function to analyze product usage trends
def analyze_usage_trends(data):
    feature_usage = data.groupby('feature_used').size().reset_index(name='usage_count')
    return feature_usage

# Additional helper functions can be added as needed
