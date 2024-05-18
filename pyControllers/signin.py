from flask import Flask, render_template, request, redirect, url_for
from dbConnection import connectDB

app = Flask(__name__, static_folder='../static', template_folder='../templates')


def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("email: ", email)
        print("pass: ", password)

        # SEGUN EL TIPO DE USUARIO, EL RENDER SERA DE CONTRATISTA V1 O AUDITOR V1
        try:
            connection = connectDB()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM contratista WHERE email=%s and contraseña=%s",
                                        (email, password))
            contratista = cursor.fetchone()
            
            if contratista:
                cursor.close()
                return redirect(url_for('contratista.contratistaV1'))


            cursor.execute("SELECT * FROM auditor WHERE email=%s and contraseña=%s",
                                        (email, password))
            auditor = cursor.fetchone()
            cursor.close()

            if auditor:
                return render_template('auditorV1.html')
                
            raise Exception
        except Exception as e:
            print("Error in Sign in: ",e)
            return "User not found or incorrect password", 401
        


    if request.method == 'GET':
        return render_template('signIn.html')

