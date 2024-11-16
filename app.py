from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/live-data')
def live_data():
    # Replace with actual logic to display live data
    ped = {
        "12:00": 69,
        "13:00": 45,
        "14:00": 30,
        "15:00": 50,
        "16:00": 80,
    }
    
    return render_template('index.html', ped=ped)

@app.route('/about')
def about():
    # Replace with your "About" page content
    return render_template('about.html')
