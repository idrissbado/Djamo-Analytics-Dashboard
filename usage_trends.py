def usage_analysis(connection, table):
    query = f"SELECT user_id, feature, count(*) as usage_count FROM {table} GROUP BY user_id, feature;"
    data = pd.read_sql(query, connection)

    # Pivot data for clustering
    pivot = data.pivot(index='user_id', columns='feature', values='usage_count').fillna(0)
    feature_summary = pivot.describe()
    return feature_summary.to_dict()
