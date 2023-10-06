from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['fname']
    last_name = request.form['lname']
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('myweb_data.txt', 'a') as file:
        file.write(f"{current_time}: First Name: {first_name}, Last Name: {last_name}\n")

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
