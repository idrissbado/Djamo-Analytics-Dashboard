# Djamo Analytics Dashboard

## Overview
This web-based application provides insights into:
1. Fraud detection in the Foot Soldiers program.
2. Churn analysis and retention strategies.
3. Product usage trends to optimize user engagement.

## Features
- **Dynamic Database Connection**: Users can input database credentials.
- **Interactive Dashboards**: View results with visualizations for each business case.
- **Scalable Design**: Easily extend to other business cases.

## Installation
1. Clone the repository:  
   `git clone https://github.com/idrissbado/Djamo-Analytics-Dashboard.git`
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Start the application:  
   `python run.py`

## Usage
1. Navigate to `http://localhost:5000`.
2. Enter your database credentials and table name.
3. View the results on the dashboard.
# Explanation
connect_to_db: Establishes the connection to the MySQL database using the credentials provided by the user.
extract_data_from_table: Fetches data from the specified table in the database.
detect_fraud: Identifies potential fraud by calculating the commission-to-deposit ratio. It returns rows where the ratio exceeds a defined threshold (in this case, 5).
detect_churn: Flags users who are considered to have churned. This is determined by checking if their last activity date is more than 30 days after their sign-up date.
analyze_usage_trends: Analyzes usage patterns, like the most commonly used features, by aggregating data on feature usage.


## Future Work
- Add authentication for security.
- Deploy on cloud platforms like AWS or Azure.

## GitHub Repository
All source code and documentation are hosted on [GitHub](https://github.com/idrissbado/Djamo-Analytics-Dashboard).
## How It Works
index.html allows users to enter database credentials and table name, which are then sent to the server for processing.
The server fetches the relevant data from the database, performs analysis for the three business cases (Fraud Detection, Churn Analysis, Product Usage Trends), and passes the results to dashboard.html.
If an error occurs, the user is redirected to error.html with an appropriate error message.
dashboard.html displays the results of the analysis in tables and text format, including fraud detection data, churn analysis, and usage trends.
## Next Steps
You can customize the tables and the analysis results to suit the format of your business case data.
Use Plotly or Matplotlib to create more interactive or advanced visualizations, which can also be integrated into dashboard.html.
Ensure the application is deployed on a server for real-time use.
