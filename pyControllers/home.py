from flask import Flask, render_template

from contratista import contratista_blueprint
from auditor import auditor_blueprint
from login import login
from signin import signin


app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.register_blueprint(auditor_blueprint)
app.register_blueprint(contratista_blueprint)

# nombre en html ,  nombre del archivo, nombre del metodo
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/signin', 'signin', signin, methods=['GET', 'POST'])



@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run()
