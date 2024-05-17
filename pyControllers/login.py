from flask import Flask, render_template, request

app = Flask(__name__, static_folder='../static', template_folder='../templates')


def login():
    if request.method == 'POST':
        request.form.get('email')
        request.form.get('nombre')
        request.form.get('password')
        request.form.get('apellido')
        request.form.get('cedula')
        request.form.get('telefono')

        #manejar post, al hundirse el boton "registrarse" habra que hacer exepciones y redigir al sign in o home

    if request.method == 'GET':
        return render_template('logInContratista.html')


if __name__ == '__main__':
    app.run()
