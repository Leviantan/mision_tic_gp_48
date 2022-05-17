# Ejercicio tipo reto

def datosPersonales(Ficha: dict)-> dict:
    uCed = Ficha['Cedula']
    uNom = Ficha['Nombre']
    uApe = Ficha['Apellido']
    uCor = Ficha['Correo']

    #Condicion validar cedula mayores a 1000000
    if uCed > 1000000:
        condicion = True
    else:
        condicion = False
    
    dicSalida = dict(
        Cedula = uCed,
        Condicion = condicion
    )

    return dicSalida

Ficha = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print(datosPersonales(Ficha))

'''
    Método clear()
    Este método remueve o elimina todos los elementos (items) del diccionario.
'''

diccionario = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print(diccionario)
diccionario.clear()
print(diccionario)

'''
    Método copy()
    Este método devuelve una copia del diccionario.
'''

diccionario2 = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print('Diccionario original: ', diccionario2)

nuevo_diccionario2 = diccionario2.copy()
print('Copia diccionario2: ', nuevo_diccionario2)


'''
    fromkeys()
    Este método crear un nuevo diccionario con clave a partir de un tipo de dato secuencia.
    el valor por defecto es de tipo none.
'''

lista_tupla = ('python','zope','plone')
versiones = dict.fromkeys(lista_tupla)

print('Nuevo diccionario: %s ' % str(versiones))

diccionario3 = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

versiones = dict.fromkeys(diccionario3)
print('Nuevo diccionario: %s' % str(versiones))

versiones = dict.fromkeys(diccionario3,1)
print('Nuevo diccionario: %s' % str(versiones))

'''
    Método get()
    Devuelve el valor de una clave solicitada, sino la encuentra devuelve None
'''

diccionario4 = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print()
print(diccionario4.get('Cedula'))
print(diccionario4.get('correo'))
#print(diccionario4['correo'])

'''
    Método items()
    Devuelve una lista de pares de diccionarios (clave, valor), como una tupla
        [
            ('Cedula', 1100324332), 
            ('Nombre', 'Carlos'), 
            ('Apellido', 'Diaz'), 
            ('Correo', 'cdiaz@gmail.com')
        ]
'''

diccionario5 = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print()
print(diccionario5.items())

'''
    Método pop()
    Remover específicamente una clave de un diccionario y devolver el valor correspondiente.
    Laza una excepción de KeyError si la clave no es encontrada.
'''

diccionario6 = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print('Versión original: ', diccionario6)
valor_eliminado = diccionario6.pop('Apellido')
print('valor eliminado: ', valor_eliminado)

print('Diccionario modificado: ', diccionario6)

'''
    Método update()
    Actualizar un diccionario agregando nuevos pares clave-valor.
    Si se llama el método update() sin pasar parametros, el diccionario
    permanece sin cambios.
'''

diccionarioOriginal = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

print()
print('Diccionario original', diccionarioOriginal)

nuevoDiccionario = ({'Telefono': 12323323})

print('Nuevo diccionario - complemento', nuevoDiccionario)

diccionarioOriginal.update(nuevoDiccionario)

print('Diccionario original actualizado ', diccionarioOriginal)
print()

# ejercicio 7

usuario_1 = {
    'Cedula': 1100324332,
    'Nombre': 'Carlos',
    'Apellido': 'Diaz',
    'Correo': 'cdiaz@gmail.com'
}

usuario_2 = {
    'Cedula': 11180239432,
    'Nombre': 'Maria',
    'Apellido': 'Lara',
    'Correo': 'mlara@gmail.com'
}

print('Usuario 1: ', usuario_1)
print()
print('Usuario 2: ', usuario_2)
print()

usuario_1.update(usuario_2)

print('Usuario 1 actualizado: ', usuario_1)


# ejemplo 8

datos = {
    'nombre': 'Miguel',
    'apellido': 'Diaz',
    'cedula': 1100232434
}

# Agregar dos nuevos datos y actualizar el diccionario.

datos_add = {
    'cuenta_ahorros': 2139243833,
    'saldo': 10000000
}

print()
print(datos)
datos.update(datos_add)

print()

for k in datos.keys():
    print('{} = {}'.format(k,datos[k]))