# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, jsonify

app = Flask(__name__)

categories = [
    {"id": 1, "name": "Category 1"},
    {"id": 2, "name": "Category 2"},
    {"id": 3, "name": "Category 3"},
    {"id": 4, "name": "Category 4"},
    {"id": 5, "name": "Category 5"},

]

@app.route('/categories', methods=['GET'])
def get_categories():
    # Use a breakpoint in the code line below to debug your script.
    return jsonify(categories)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
