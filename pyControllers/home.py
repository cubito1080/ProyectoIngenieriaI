from flask import Flask, render_template

from contratista import contratista_blueprint
from auditor import auditor_blueprint
from logIn import registrarse
from signIn import iniciarSesion


app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.register_blueprint(auditor_blueprint)
app.register_blueprint(contratista_blueprint)
app.secret_key = 'd69e0c8f58e25781ab2e954afcd4b8314cf3ea553283156225b7763e889fe828'

# nombre en html ,  nombre del archivo, nombre del metodo
app.add_url_rule('/logIn', 'logIn', registrarse, methods=['GET', 'POST'])
app.add_url_rule('/signIn', 'signIn', iniciarSesion, methods=['GET', 'POST'])


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
