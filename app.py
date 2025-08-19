# cd ~/Desktop/myproject   # or your project folder
# source venv/bin/activate # Activate your virtual environment
# pip install flask # Create a file named app.py
# python app.py # to run the Flask app => http://127.0.0.1:5000/
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! 🚀 Your app is running."

if __name__ == "__main__":
    app.run(debug=True)