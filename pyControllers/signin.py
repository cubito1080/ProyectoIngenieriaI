from flask import Flask, render_template, request, redirect, url_for, flash
from dbConnection import connectDB

app = Flask(__name__, static_folder='../static', template_folder='../templates')


@app.route('/signIn', methods=['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # SEGUN EL TIPO DE USUARIO, EL RENDER SERA DE CONTRATISTA V1 O AUDITOR V1
        try:
            connection = connectDB()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT nombre, cedula FROM contratista WHERE email=%s and contraseña=%s",
                                                (email, password))
            contratista = cursor.fetchone()
            
            if contratista:
                cursor.close()
                return redirect(url_for(f'contratista.contratistaV1', 
                                        nombre=contratista["nombre"], cedula=contratista["cedula"]))


            cursor.execute("SELECT nombre, cedula FROM auditor WHERE email=%s and contraseña=%s",
                                        (email, password))
            auditor = cursor.fetchone()
            cursor.close()

            if auditor:
                return redirect(url_for('auditor.auditorV1', 
                                        nombre=auditor["nombre"], cedula=auditor["cedula"]))

                
            raise Exception


        except Exception as e:
            flash('Ocurrió un error al procesar tu solicitud', 'error')
            print("Error in Sign in: ", e)

            return render_template("signIn.html", alert_message="Datos Incorrectos")


 
          
        

    if request.method == 'GET':
        return render_template('signIn.html')

