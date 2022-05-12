# Diccionario vacio

# ejemplo 1
diccionario = {}

print(diccionario)
print(type(diccionario))

# Diccionario vacio usando el constructor dict()
diccionario2 = dict()

print(diccionario2)
print(type(diccionario2))

# Si necesitamos almacenar nuevos valores basta con separarlos mediante una coma.

diccionario2 ={
#   clave       :  valor    
    "total"     : 53,
    "descuento" : True,
    "subtotal"  : 20.34033,
    "cliente"   : "Juan"
}

print(diccionario2)

# ejemplo 3

# Argumentos con nombre
diccionario3 = dict(uno = 1, dos = 2, tres = 3)

print(diccionario3)

# ejercicio 4

diccionario4 = {
    "gato" : "chat",
    "perro" : "chien",
    "caballo" : "cheval"
}

numeroTelefono = {
    'jefe' : '+57 430454',
    'secretaria' : '+57 34229944'
}

print(diccionario4)
print(numeroTelefono)

# ejemplo 5

usuario = {
    'nombre': 'Mauricio',
    'edad': 28,
    'curso': 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos': 100
    },
    'no_medallas': 10
}

print(usuario)

# ejemplo 6

# para poder agregar, obtener o modificar algún valor del diccionario haremos con corchetes.

usuario['activo'] = True
print(usuario)
print(usuario['activo'])

usuario['nombre'] = 'Jose'
print(usuario)
print(usuario['nombre'])

print()
print(usuario['skills'])
print(type(usuario['skills']))
print(usuario['skills']['base_de_datos'])


# ejemplo 7

'''
    Podemos obtener todas las llaves de nuestro diccionario utlizando
    el método keys, de igual forma podemos obtener todos los valores del diccionario
    con el método values

'''

diccionario7 = {'Manuel' : 1, 'Marcos' : 2, 'Felipe' : 3, 'Maria' : 4}

print(diccionario7)
print()
print(diccionario7.keys())
print()
print(diccionario7.values())

print()

informacion = {'nombre': 'Emiro'}

def ejemplo(informacion: dict):
    dict_nuevo = {
        'nombre' : informacion['nombre'],
        'estado' : 'Aceptado'
    }

    return dict_nuevo

print(ejemplo(informacion))