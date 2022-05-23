# Bucle for
# range(start, stop,step)
# range(inicio, final, contador)


'''
for x in range(0,4):
    print('Estamos en la iteración: ', x)
'''

'''
for x in range(0,10, 2):
    print('Estamos en la iteracion : ', x)
'''

'''
for x in range(10,0, -2):
    print('Estamos en la iteración : ' + str(x))
'''

# ejercicio 2
# Mètodo split()

'''
oracion = 'Mary entiende muy bien Python'
frases = oracion.split() # Convierte la cadena a una lista de palabras

print(type(frases))
print(frases)
print('La oración es', oracion, '\n')

for palabra in range(len(frases)):
    print('palabra: {} , en su posición es: {}'.format(frases[palabra], palabra))
'''

'''
datos_personales = {
    'nombres' : 'Jose Lenardo',
    'apellidos': 'Garcia Lara',
    'ceudla': '11002324333',
    'fecha_nacimiento': ' 02/04/1983',
    'lugar_nacimiento' : 'Bucaramanga, Santander',
    'nacionalidad': 'Colombiano',
    'estado_civil': 'soltero'
}

clave = datos_personales.keys()
valor = datos_personales.values()

cantidad_datos = datos_personales.items()

for clave, valor in cantidad_datos:
    print(clave, ' => ', valor)

for k in datos_personales.keys():
    print(k, ' = ', datos_personales[k])

for cla in datos_personales:
    print(cla, ' -> ', datos_personales[cla])
'''

# ejercicio 3
# Buclw con else

db_conection = '107.0.0.1','5432','root','nomina'
print(type(db_conection))
print(db_conection)

for parametro in db_conection:
    print(parametro)

print('El comando postgreSQL es: -h {} -p {} -u {} -d{}'.
format(db_conection[0], db_conection[1], db_conection[2], db_conection[3]))