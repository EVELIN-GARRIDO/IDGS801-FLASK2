# Importar Flask
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect

import forms

# Usar el famework
app = Flask(__name__)

app.config['SECRET_KEY'] = "Esta es tu clave encriptada"
csrf = CSRFProtect()

# Decoradores
@app.route('/calcular', methods = ['GET'])
def calcular():
    return render_template('calcular.html')

@app.route('/cookie', methods = ['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookie.html', form = reg_user))
    user = ''
    pasw = ''

    if (request.method == 'POST' and reg_user.validate()):
        user = reg_user.username.data
        pasw = reg_user.password.data
        datos = user + "@" + pasw
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(success_message)
        #print(user + ' ' + pasw)

    return response

@app.route('/Alumnos', methods = ['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    mat = ''
    nom = ''

    if (request.method == 'POST' and reg_alum.validate()):
        mat = reg_alum.matricula.data
        nom = reg_alum.nombre.data

    return render_template('Alumnos.html', form = reg_alum, mat = mat, nom = nom)


@app.route('/traductor', methods=['GET', 'POST'])
def agregarPalabras():
    req_palabras = forms.FormIngresoPalabras(request.form)
    btnAgregar = request.form.get("btnAgregar")
    btnTraducir = request.form.get("btnTraducir")
    translation = ''
    message = ''
    encontrado = False

    if (request.method == 'POST' and req_palabras.validate() and btnAgregar == "Agregar"):
        palabraEsp = req_palabras.palabraEspanol.data.lower()
        palabraIng = req_palabras.palabraIngles.data.lower()

        # Open the file in append mode and write the new words
        with open('diccionario.txt', 'a') as f:
            f.write(f'{palabraEsp},{palabraIng}\n')

        message = '¡Palabra agrewgada correctamente!'

    
    elif (request.method == 'POST' and btnTraducir == "Traducir"):
        palabraTraducir = request.form.get("txtPalabraTraducir").lower()
        lenguaje = request.form.get("rbtLenguaje")

        archivo = open('diccionario.txt', 'r')

        with open('diccionario.txt', 'r') as f:
            words = f.read().splitlines()
            word_dict = dict(word.split(',') for word in words)

        if (lenguaje == "en"):
            if (word_dict.get(palabraTraducir) == None):
                translation = palabraTraducir
                    
            else:
                translation = word_dict.get(palabraTraducir)

        elif lenguaje == "es": 
            #Crear un diccionario donde las claves sean las palabras en Inglés
            reverse_dict = {v: k for k, v in word_dict.items()}

            if (reverse_dict.get(palabraTraducir) == None):
                translation = palabraTraducir
                    
            else:
                translation = reverse_dict.get(palabraTraducir)

        for linea in archivo:
            if palabraTraducir in linea:
                encontrado = True
                break


        if (encontrado == False):
            translation = "La palabra no se encuentra"



    return render_template('traductor.html', form=req_palabras, message=message, translation = translation)



# Indicar el nombre a partir del cual hará la ejecución la aplicación
if __name__ == "__main__":
    # Protección al formulario
    csrf.init_app(app) 
    app.run(debug = True, port = 3000)