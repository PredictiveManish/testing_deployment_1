from app import app
from app import init_csv

if __name__ == '__main__':
    init_csv()  # Initialize CSV file when starting the application
    app.run(debug=True)