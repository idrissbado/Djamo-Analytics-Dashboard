from app.routes import create_app

# Create and run Flask application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
