from flask import Flask, render_template, url_for, request


app = Flask(__name__)

stu_dict = {}

@app.route('/')
def index():
    return render_template('EX3register.html')
    
@app.route('/reg_list', methods = ['POST'])
def reg_list():
    if request.method == 'POST':
        try:
            name = request.form['content']
            org = request.form['orgs']
            key_list = stu_dict.keys()
            stu_dict.update({name: org })
        except:
            output = 'Invalid input'
        
        return render_template('EX3reg_list.html', key_list = key_list, stu_dict = stu_dict)

if __name__ == "__main__":
    app.run(debug=True)