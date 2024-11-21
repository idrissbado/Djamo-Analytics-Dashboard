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
