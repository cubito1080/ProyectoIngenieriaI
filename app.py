from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def viaje():
    return render_template('contratistaV2.html')


if __name__ == '__main__':
    app.run()
