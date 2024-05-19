from flask import Flask, render_template, request, Blueprint, send_from_directory
from dbConnection import connectDB
from documento import documentosContrato


app = Flask(__name__, static_folder='../static', template_folder='../templates')
auditor_blueprint = Blueprint('auditor', __name__)


@auditor_blueprint.route('/auditorV4', methods=['POST'])
def auditorV4():
    nombre = request.form.get('nombre_input')
    tipo_contrato = request.form.get('tipo_contrato_input')
    clase_arl = request.form.get('clase_arl_input')
    cedula = request.form.get('cedula_input')
    metodo_de_pago = request.form.get('metodo_de_pago_input')
    fecha = request.form.get('fecha_input')
    sueldo = request.form.get('sueldo_input')
    bancaria = request.form.get('bancaria_input')
    fecha_fin = request.form.get('fecha_fin_input')
    servicio = request.form.get('servicio_input')
    return render_template('auditorV4.html')


@auditor_blueprint.route('/AuditorV3/<cedula>/<cedulaContratista>')
#Datos QUEMADOS. Debe recibir el contratista y auditor, o la cedula de ellos
def auditorV3(cedula, cedulaContratista):

    return render_template('AuditorV3.html', documentos=documentosContrato(cedulaContratista, cedulaAuditor=cedula))


@auditor_blueprint.route('/auditorV2/<nombre>/<cedula>')
def auditorV2(nombre, cedula):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM contrato WHERE "
        "cedula_auditor=%s", (cedula, ))

    contratos = cursor.fetchall()
    cursor.close()
    return render_template('auditorV2.html', auditor={"nombre":nombre,"cedula":cedula}, contratos=contratos)


@auditor_blueprint.route('/auditorV1/<nombre>/<cedula>')
def auditorV1(nombre, cedula):
    return render_template('auditorV1.html', auditor={"nombre": nombre, "cedula":cedula})


@auditor_blueprint.route('/ruta', methods=['POST'])
def formulario_nuevo_contrato():
    # procesar data
    return render_template('home.html')


@auditor_blueprint.route('/ver_documento/<filename>')
def ver_documento(filename):
    return send_from_directory('./documentos/', filename)

