from flask import Flask, render_template, request, Blueprint, redirect, url_for
from dbConnection import connectDB
from documento import *

app = Flask(__name__, static_folder='../static', template_folder='../templates')

contratista_blueprint = Blueprint('contratista', __name__)

@contratista_blueprint.route('/contratistaV1/<nombre>/<cedula>')
def contratistaV1(nombre, cedula):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT nombre FROM contratista WHERE "
        "cedula=%s", (cedula,))

    nombre = cursor.fetchone()["nombre"]
    cursor.close()
    
    return render_template('contratistaV1.html', contratista={"nombre": nombre, "cedula": cedula})


@contratista_blueprint.route('/contratistaV2/<nombre>/<cedula>')
                                    #cédula QUEMADA!!
def contratistaV2(nombre, cedula):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM contrato as c WHERE "
        "c.cedula_contratista=%s", (cedula,))

    contratos = cursor.fetchall()
    cursor.close()
    return render_template('contratistaV2.html',
                            contratista={"nombre": nombre, "cedula": cedula},
                            contratos=contratos)


@contratista_blueprint.route('/volverDeV3')
def volverDeV3():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')

@app.route('/')
def home():
    # Aquí va la lógica para manejar la página de inicio
    return render_template('home.html')


@contratista_blueprint.route('/contratistaV3/<cedula>/<cedulaAuditor>', methods=['GET', 'POST'])
#Datos QUEMADOS. Debe recibir el contratista y auditor, o la cedula de ellos
def contratistaV3(cedula, cedulaAuditor):
    if request.method  == "POST":
        if request.files['file']:
            f = request.files['file']
            file = handleFile(f)
            result = uploadFile(file)
        
        if result == 1:
            print("File added successfully to the db")
        else:
            print("Couldn't add file")
        return render_template("contratistaV3.html", documentos=documentosContrato(cedula, cedulaAuditor)), 200

    return render_template("contratistaV3.html", documentos=documentosContrato(cedula, cedulaAuditor))


@contratista_blueprint.route('/verifica_estado_documento_contratista')
def verDocumento():
    # Aquí va la lógica para ver el documento que seleccionó el contratista 
    pass
