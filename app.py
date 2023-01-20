from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import api_data
import data_json
import os
app = Flask(__name__)
#remove files if already exists to upload new data
try:
    os.remove('static\js\month_data.js')
    os.remove('static/js/today_data.js')
    os.remove('static\js\week_data.js')
    os.remove('static\js\year_data.js')
except:
    print('no files to be removed')
#call function to get all the necessary data
data_json.json_data()
@app.route('/')
def echo():
    return render_template('index.html')
@app.route('/monthly')
def month():
    return render_template('monthly.html')
@app.route('/weekly')
def weekly():
    return render_template('weekly.html')
@app.route('/yearly')
def yearly():
    return render_template('yearly.html')
#debugger to edit while running
if __name__ == "__main__":
    app.run(debug=True)