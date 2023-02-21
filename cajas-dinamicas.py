# Importar Flask
from flask import Flask, render_template
from flask import request
import forms2

# Usar el famework
app = Flask(__name__)

# Decoradores
@app.route('/', methods = ['GET','POST'])
def generarCajas():
    req_cajas = forms2.Cajas(request.form)
    cantidadCajas = req_cajas.cantidadCajas.data or 0
    valoresCajas = []
    btnGenerar = request.form.get("btnGenerar")
    btnProcesar = request.form.get("btnProcesar")
    mostrarBoton = False
    mostrarInfo = False
    sumaValores = 0
    promedio = 0.0
    valoresOrdenados = []
    maximo = 0
    minimo = 0
    vecesRepetido = 0
    numerosRepetidos = []
    veces = "No hay números repetidos."

    if (btnGenerar == 'Generar'):
        mostrarBoton = True

    if (request.method == 'POST'):
        if (btnProcesar == "Procesar"):
            mostrarBoton = True
            for valor in range(cantidadCajas):
                valoresCajas.append(request.form.get('txtCaja{}'.format(valor+1)))

            for numero in valoresCajas:
                sumaValores += int(numero)

            lista_enteros = [int(elemento) for elemento in valoresCajas]
            valoresOrdenados = sorted(lista_enteros)
            promedio = (sumaValores / cantidadCajas)
            maximo = valoresOrdenados[0]
            minimo = valoresOrdenados[0]         
            
            for numero in valoresOrdenados:
                if (numero > maximo):
                    maximo = numero

                elif (numero < minimo):
                    minimo = numero
            
            numeros = {}

            for elemento in valoresOrdenados:
                if elemento in numeros:
                    numeros[elemento] += 1

                else:
                    numeros[elemento] = 1
              
            for elemento, contador in numeros.items():
                if contador > vecesRepetido:
                    vecesRepetido = contador

            print(numeros)

            for elemento, contador in numeros.items():
                if contador == vecesRepetido:
                    numerosRepetidos.append(str(elemento))
                    veces = "{} veces.".format(contador)

            if not numerosRepetidos:
                numerosRepetidos.append("No hay números repetidos.")
            
            mostrarInfo = True

    return render_template('cajas-dinamicas.html', form = req_cajas, cantidadCajas = cantidadCajas, mostrarBoton = mostrarBoton, valoresCajas = valoresCajas, promedio = promedio, maximo = maximo, minimo = minimo, numerosRepetidos = numerosRepetidos, veces = veces, mostrarInfo = mostrarInfo)



# Indicar el nombre a partir del cual hará la ejecución la aplicación
if __name__ == "__main__":
    app.run(debug = True, port = 3000)