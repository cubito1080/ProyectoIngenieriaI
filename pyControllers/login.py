import mysql.connector
from flask import Flask, render_template, request

from dbConnection import connectDB

app = Flask(__name__, static_folder='../static', template_folder='../templates')

def registrarse():
    if request.method == 'POST':
        #manejar post, al hundirse el boton "registrarse" habra que hacer exepciones y redigir al sign in o home

        try:
            email = request.form.get('email')
            nombre = request.form.get('nombre')
            password = request.form.get('password')
            password_confirm = request.form.get('password_')
            apellido = request.form.get('apellido')
            cedula = (request.form.get('cedula'))
            telefono = request.form.get('telefono')

            if not (email and nombre and password and password_confirm and apellido and cedula and telefono):
                return render_template("logInContratista.html", alert_message="Debe llenar todos los campos del formulario")

            if not password_confirm == password:
                return render_template("logInContratista.html", alert_message="Las contraseñas no son iguales")



            connection = connectDB()

            cursor = connection.cursor(dictionary=True)

            # Completar la consulta SQL para insertar los datos en la tabla "contratista"
            query = "INSERT INTO contratista (email, nombre, contraseña, apellido, cedula, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (email, nombre, password, apellido, int(cedula), telefono))
            connection.commit()
            cursor.close()
            return render_template('home.html')

        except mysql.connector.Error as e:
            print(e)
            return render_template("logInContratista.html",alert_message="Error interno, intente mas tarde ")

        except Exception as e:
            return render_template("logInContratista.html",alert_message="No se pudo realizar el registro exitosamente")


    if request.method == 'GET':
        return render_template('logInContratista.html')


if __name__ == '__main__':
    app.run()
