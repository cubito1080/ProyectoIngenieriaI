import mysql.connector
from flask import Flask, render_template, request, Blueprint, send_from_directory, redirect, url_for
from dbConnection import connectDB
from documento import documentosContrato


app = Flask(__name__, static_folder='../static', template_folder='../templates')
auditor_blueprint = Blueprint('auditor', __name__)





@auditor_blueprint.route('/auditorV4/<nombre>/<cedula>',methods=['GET', 'POST'])
def auditorV4(nombre, cedula):
    if request.method == 'POST':

        nombre_ = request.form.get('nombre_')
        tipo_contrato = request.form.get('tipo_contrato')
        clase_arl = request.form.get('clase_arl')
        cedula_contratista = request.form.get('cedula_')
        metodo_de_pago = request.form.get('metodo_de_pago')
        fecha = request.form.get('fecha')
        sueldo = request.form.get('sueldo')
        bancaria = request.form.get('bancaria')
        fecha_fin = request.form.get('fecha_fin')
        servicio = request.form.get('servicio')

        try:
            connection = connectDB()

            cursor = connection.cursor(dictionary=True)

            insert_query = (
                "INSERT INTO contrato "
                "(fecha_inicio, fecha_culminacion, estado, cedula_contratista, "
                "cedula_auditor, clase_ARL, metodo_pago, tipo, descripcion, honorario) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            )

            # Datos a insertar
            data = (
                fecha, fecha_fin, "en progreso", int(cedula_contratista),
                int(cedula), clase_arl, metodo_de_pago, tipo_contrato, servicio, sueldo
            )
            # Ejecuta la consulta
            cursor.execute(insert_query, data)


            connection.commit()
            cursor.close()

            return redirect(url_for(f'auditor.auditorV1',
                                    nombre=nombre, cedula=cedula))
        except mysql.connector.Error as e:
            return render_template('qqqq.html', auditor={"nombre": nombre, "cedula":cedula})

    if request.method == 'GET':
        return render_template('qqqq.html', auditor={"nombre": nombre, "cedula":cedula})




@auditor_blueprint.route('/auditorV3/<cedula>/<cedulaContratista>')
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

