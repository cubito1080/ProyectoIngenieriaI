from flask import Flask, render_template, request, Blueprint

app = Flask(__name__, static_folder='../static', template_folder='../templates')

auditor_blueprint = Blueprint('auditor', __name__)
@auditor_blueprint.route('/auditorV4')
def auditorV4():
    # Aquí va la lógica para manejar la página de "Nuevo contrato"
    return render_template('auditorV4.html')

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




if __name__ == '__main__':
    app.run()
