from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/live-data')
def live_data():
    # Replace with actual logic to display live data
    return render_template('index.html')

# @app.route('/about')
# def about():
#     # Replace with your "About" page content
#     return render_template('about.html', title="About")
