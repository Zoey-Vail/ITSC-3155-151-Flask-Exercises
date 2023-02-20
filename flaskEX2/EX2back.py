from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('EX2home.html')
    
@app.route('/Calculate', methods = ['POST'])
def Calculate():
    if request.method == 'POST':
        try:
            num = int(request.form.get('content'))
            if (num % 2 == 1):
                output = str(num) + ' is odd'
            else:
                output = str(num) + ' is even'
        except:
            output = 'Invalid input'
        
        return render_template('EX2calculate.html', output = output)

if __name__ == "__main__":
    app.run(debug=True)