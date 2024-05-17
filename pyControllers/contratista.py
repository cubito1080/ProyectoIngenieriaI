from flask import Flask, render_template, request, Blueprint

app = Flask(__name__, static_folder='../static', template_folder='../templates')

contratista_blueprint = Blueprint('contratista', __name__)

@contratista_blueprint.route('/contratistaV2')
def contratistaV2():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')


@contratista_blueprint.route('/volverDeV3')
def volverDeV3():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')

@app.route('/')
def home():
    # Aquí va la lógica para manejar la página de inicio
    return render_template('home.html')

@contratista_blueprint.route('/subir_documento_contratista')
def subir_documento_contratista():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')

@contratista_blueprint.route('/verifica_estado_documento_contratista')
def verifica_estado_documento_contratista():
    # Aquí va la lógica para manejar la página de "Mis contratos"
    return render_template('contratistaV2.html')



if __name__ == '__main__':
    app.run()
