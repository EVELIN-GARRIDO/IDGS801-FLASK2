# Importar Flask
from flask import Flask, render_template
from flask import request
import forms

# Usar el famework
app = Flask(__name__)

# Decoradores
@app.route('/calcular', methods = ['GET'])
def calcular():
    return render_template('calcular.html')

@app.route('/Alumnos', methods = ['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    mat = ''
    nom = ''

    if (request.method == 'POST' and reg_alum.validate()):
        mat = reg_alum.matricula.data
        nom = reg_alum.nombre.data

    return render_template('Alumnos.html', form = reg_alum, mat = mat, nom = nom)

# Indicar el nombre a partir del cual hará la ejecución la aplicación
if __name__ == "__main__":
    app.run(debug = True, port = 3000)