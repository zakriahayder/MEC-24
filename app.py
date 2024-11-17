from flask import Flask, render_template, flash
from helpers import load_pedestrian_data

app = Flask(__name__)
app.secret_key = "12345"

ped = load_pedestrian_data("data.csv")


@app.route("/")
def live_data():
    # Replace with actual logic to display live data
    return render_template("data.html", ped=ped)


@app.route("/data")
def about():
    # Replace with your "About" page content
    return render_template("index.html", ped=ped)
