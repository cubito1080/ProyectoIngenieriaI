from flask import Flask, render_template, request

app = Flask(__name__, static_folder='../static', template_folder='../templates')



def signin():
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        return render_template('signIn.html')



if __name__ == '__main__':
    app.run()