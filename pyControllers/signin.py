from flask import Flask, render_template, request
from dbConnection import connectDB

app = Flask(__name__, static_folder='../static', template_folder='../templates')



def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Handle form submission here
        # SEGUN EL TIPO DE USUARIO, EL RENDER SERA DE CONTRATISTA V1 O AUDITOR V1
        connection = connectDB()
        cursor = connection.cursor()

        contratista = cursor.execute(f"SELECT * FROM contratista WHERE email={email} and contraseña={password}")
        if contratista:
            return render_template('ContratistaV1.html')

        auditor = cursor.execute(f"SELECT * FROM auditor WHERE email={email} and contraseña={password}")
        if auditor:
            return render_template('auditorV1.html')


    if request.method == 'GET':
        return render_template('signIn.html')



if __name__ == '__main__':
    app.run()
