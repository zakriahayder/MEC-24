from flask import Flask, render_template
from helpers import load_pedestrian_data

app = Flask(__name__)

ped = load_pedestrian_data("data.csv")

@app.route('/')
@app.route('/live-data')
def live_data():
    # Replace with actual logic to display live data

    return render_template('index.html', ped=ped)

@app.route('/data')
def about():
    # Replace with your "About" page content
    return render_template('data.html', ped=ped)
