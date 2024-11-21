import pandas as pd

def fraud_analysis(connection, table):
    query = f"""
    SELECT agent_id, transaction_id, commission, deposit_time, client_id
    FROM {table}
    WHERE transaction_type = 'Deposit';
    """
    data = pd.read_sql(query, connection)

    # Calculate metrics
    grouped = data.groupby('agent_id').agg({
        'commission': 'sum',
        'transaction_id': 'count'
    })
    grouped['commission_to_deposit_ratio'] = grouped['commission'] / grouped['transaction_id']
    
    # Detect fraud
    threshold = grouped['commission_to_deposit_ratio'].mean() + 2 * grouped['commission_to_deposit_ratio'].std()
    potential_fraud = grouped[grouped['commission_to_deposit_ratio'] > threshold]
    return potential_fraud.to_dict(orient='records')
