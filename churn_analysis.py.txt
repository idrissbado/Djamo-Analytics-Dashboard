def churn_analysis(connection, table):
    query = f"SELECT user_id, age, sessions, deposits, churned FROM {table};"
    data = pd.read_sql(query, connection)
    
    # Summarize churn causes
    churned_users = data[data['churned'] == 1]
    summary = churned_users.describe()
    return summary.to_dict()
