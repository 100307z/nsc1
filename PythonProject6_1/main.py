# This is a sample Python script.
from http.client import responses

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
    # Use a breakpoint in the code line below to debug your script.
    api_url = 'http://127.0.0.1:5000/categories'
    response = requests.get(api_url)
    categories = response.json()
    return render_template('index.html', categories=categories)\
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='127.0.0.2', port=8000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
