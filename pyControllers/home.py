from flask import Flask, render_template

from pyControllers.auditor import auditor_blueprint
from pyControllers.login import login
from pyControllers.signin import signin


app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.register_blueprint(auditor_blueprint)

# nombre en html ,  nombre del archivo, nombre del metodo
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/signin', 'signin', signin, methods=['GET', 'POST'])



@app.route('/')
def home():
    return render_template('auditorV1.html')



if __name__ == '__main__':
    app.run()
