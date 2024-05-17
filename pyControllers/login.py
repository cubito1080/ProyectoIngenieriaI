from flask import Flask, render_template, request

app = Flask(__name__, static_folder='../static', template_folder='../templates')


def login():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        return render_template('logInContratista.html')


if __name__ == '__main__':
    app.run()
