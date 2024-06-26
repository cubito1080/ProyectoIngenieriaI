import mysql.connector
from flask import Flask, render_template, request, Blueprint, send_from_directory, redirect, url_for
from dbConnection import connectDB
from documento import documentosContrato


app = Flask(__name__, static_folder='../static', template_folder='../templates')
auditor_blueprint = Blueprint('auditor', __name__)





@auditor_blueprint.route('/auditorV4/<nombre>/<cedula>',methods=['GET', 'POST'])
def auditorV4(nombre, cedula):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    get_query = (
        "SELECT cedula FROM contratista"
    )
    cursor.execute(get_query)
    cedulas = cursor.fetchall()
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
            connection.close()


            return redirect(url_for(f'auditor.auditorV1',
                                    nombre=nombre, cedula=cedula))
        except mysql.connector.Error as e:
            print(e)
            return render_template('auditorV4.html', auditor={"nombre": nombre, "cedula":cedula},cedulas=cedulas)

    if request.method == 'GET':
        return render_template('auditorV4.html', auditor={"nombre": nombre, "cedula":cedula},cedulas=cedulas)


@auditor_blueprint.route('/auditorV3/<contrato_id>', methods=['GET', 'POST'])
def auditorV3(contrato_id):
    print(request.method)
    if request.method == 'POST':
        connection = connectDB()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "UPDATE contrato SET estado='finalizado' WHERE id=%s", (contrato_id, ))
        connection.commit()
        cursor.close()
        if cursor.rowcount == 1:
            print("Contrato updated")
        else:
            print(cursor.rowcount)
            print("Contrato update failed")
        return render_template('AuditorV3.html', documentos=documentosContrato(contrato_id), 
                                opciones=['en espera', 'aprobado', 'no aprobado'])

    if request.method == 'GET':
        documentos = documentosContrato(contrato_id)
        return render_template('AuditorV3.html', documentos=documentos, 
                                opciones=['en espera', 'aprobado', 'no aprobado'])


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
    return render_template('auditorV1.html', auditor={"nombre": nombre, "cedula": cedula})


@auditor_blueprint.route('/ruta', methods=['POST'])
def formulario_nuevo_contrato():
    # procesar data
    return render_template('home.html')


@auditor_blueprint.route('/ver_documento/<filename>')
def ver_documento(filename):
    return send_from_directory('./documentos/', filename)


@auditor_blueprint.route('/actualizar_estado/<documento_id>/<contrato_id>', methods=['POST'])
def actualizar_estado(documento_id, contrato_id):
    nuevo_estado = request.form.get('estado')
    print("nuevo ESTADO: ", nuevo_estado)
    connection = connectDB()
    cursor = connection.cursor()
    cursor.execute("UPDATE documento SET estado=%s WHERE id=%s", (nuevo_estado, documento_id))
    connection.commit()
    cursor.close()
    return redirect(url_for('auditor.auditorV3', contrato_id=contrato_id)) 