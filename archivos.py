# Declaramos una variable para poder leer el contenido del archivo usando la funcion open
#file = open('alumnos.txt', 'r')
# Leer el contenido del archivo y retornar String
#nombres = file.read()

# Retorna una lista
#nombres = file.readlines()

#nombres = file.readline()

# Imprimir el contenido
#print(nombres)

#file.close()

"""for item in nombres:
    print(item, end = '')"""

# Escribir contenido en un archivo
#file = open('alumnos2.txt', 'w')
file = open('alumnos2.txt', 'a')
file.write('\n' + 'Hola Mundo !!!!!') # Reemplaza el contenido del archivo
file.write('\n' + 'Hola Mundo 2')
file.close()

