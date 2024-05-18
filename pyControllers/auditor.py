from flask import Flask, render_template, request, Blueprint
from dbConnection import connectDB

app = Flask(__name__, static_folder='../static', template_folder='../templates')
auditor_blueprint = Blueprint('auditor', __name__)


@auditor_blueprint.route('/auditorV4')
def auditorV4():
    # Aquí va la lógica para manejar la página de "Nuevo contrato"
    return render_template('auditorV4.html')


@auditor_blueprint.route('/AuditorV3')
#Debe recibir el auditor y el contratista, o la cédula de ellos
def auditorV3(auditor, contratista):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    linkDocs = cursor().execute(
        "SELECT documento FROM documento as d join auditor as a join contratista as c " 
        "WHERE c.cedula=%s and a.cedula=%s", (contratista.cedula, auditor.cedula))
    cursor.close()

    documentos = linkDocs
    return render_template('AuditorV3.html', documentos=documentos)


@auditor_blueprint.route('/auditorV2')
def auditorV2():
    # Aquí va la lógica para manejar la página de "Ver contratos"
    return render_template('auditorV2.html')


@auditor_blueprint.route('/auditorV1')
def auditorV1():
    # Aquí va la lógica para manejar la página de "Ver contratos"
    return render_template('auditorV1.html')


@auditor_blueprint.route('/ruta', methods=['POST'])
def formulario_nuevo_contrato():
    # procesar data
    return render_template('home.html')

