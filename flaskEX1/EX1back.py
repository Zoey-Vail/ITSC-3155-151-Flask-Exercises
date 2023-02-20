from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import calendar

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    today = datetime.now()
    output = "The current date time is " + calendar.day_name[today.weekday()] + ", " + today.strftime("%B %d, %Y") + " " + today.strftime("%H:%M:%S")
    if request.method == 'GET':
        return render_template('EX1front.html', output = output)

if __name__ == "__main__":
    app.run(debug=True)