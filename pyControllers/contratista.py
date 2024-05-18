from flask import Flask, render_template, request, Blueprint, redirect, url_for
# from dbConnection import connectDB
from documento import *

app = Flask(__name__, static_folder='../static', template_folder='../templates')

contratista_blueprint = Blueprint('contratista', __name__)


@contratista_blueprint.route('/contratistaV2')
def contratistaV2():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')


@contratista_blueprint.route('/volverDeV3')
def volverDeV3():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')

@app.route('/')
def home():
    # Aquí va la lógica para manejar la página de inicio
    return render_template('home.html')


@contratista_blueprint.route('/contratistaV3', methods=['GET', 'POST'])
#Datos QUEMADOS. Debe recibir el contratista y auditor, o la cedula de ellos
def contratistaV3(contratista={"cedula": "1011511123"}, auditor={"cedula": "1011638823"}):
    if request.method  == "POST":
        if request.files['file']:
            f = request.files['file']
            file = handleFile(f)
            result = uploadFile(file)
        
        if result == 1:
            print("File added successfully to the db")
        else:
            print("Couldn't add file")
        return render_template("contratistaV3.html", documentos=documentosContrato(contratista, auditor)), 200

    return render_template("contratistaV3.html", documentos=documentosContrato(contratista, auditor))


@contratista_blueprint.route('/verifica_estado_documento_contratista')
def verifica_estado_documento_contratista():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')
