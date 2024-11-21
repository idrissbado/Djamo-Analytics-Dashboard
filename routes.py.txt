from flask import Flask, render_template, request, redirect, url_for, flash
from .utils import connect_to_database
from .fraud_detection import fraud_analysis
from .churn_analysis import churn_analysis
from .usage_trends import usage_analysis

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/dashboard', methods=['POST'])
    def dashboard():
        try:
            # Fetch user-provided credentials
            db_credentials = {
                'host': request.form['db_host'],
                'user': request.form['db_user'],
                'password': request.form['db_password'],
                'database': request.form['db_name'],
                'table': request.form['db_table']
            }

            # Connect to database
            connection = connect_to_database(**db_credentials)
            if not connection:
                raise Exception("Failed to connect to database.")

            # Process each business case
            fraud_data = fraud_analysis(connection, db_credentials['table'])
            churn_data = churn_analysis(connection, db_credentials['table'])
            usage_data = usage_analysis(connection, db_credentials['table'])

            return render_template(
                'dashboard.html',
                fraud_data=fraud_data,
                churn_data=churn_data,
                usage_data=usage_data
            )
        except Exception as e:
            flash(f"Error: {str(e)}", 'danger')
            return redirect(url_for('index'))

    return app
