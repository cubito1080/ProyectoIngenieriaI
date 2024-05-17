from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def viaje():
    return render_template('loginContratista.html')


if __name__ == '__main__':
    app.run()
