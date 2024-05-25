import mysql.connector
from flask import Flask, render_template, request

from dbConnection import connectDB

app = Flask(__name__, static_folder='../static', template_folder='../templates')

def registrarse():
    if request.method == 'POST':
        #manejar post, al hundirse el boton "registrarse" habra que hacer exepciones y redigir al sign in o home

        email = request.form.get('email')
        nombre = request.form.get('nombre')
        password = request.form.get('password')
        apellido = request.form.get('apellido')
        cedula = int(request.form.get('cedula'))
        telefono = request.form.get('telefono')

        try:
            connection = connectDB()

            cursor = connection.cursor(dictionary=True)

            # Completar la consulta SQL para insertar los datos en la tabla "contratista"
            query = "INSERT INTO contratista (email, nombre, contraseña, apellido, cedula, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (email, nombre, password, apellido, cedula, telefono))
            connection.commit()
            cursor.close()
            return render_template('home.html')

        except mysql.connector.Error as e:
            return render_template("logInContratista.html")


    if request.method == 'GET':
        return render_template('logInContratista.html')


if __name__ == '__main__':
    app.run()
