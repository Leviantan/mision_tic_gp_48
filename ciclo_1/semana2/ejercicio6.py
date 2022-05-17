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

'''
informacion = {'nombre': 'Emiro'}

def ejemplo(informacion: dict):
    dict_nuevo = {
        'nombre' : informacion['nombre'],
        'estado' : 'Aceptado'
    }

    return dict_nuevo

print(ejemplo(informacion))
'''

diccionario7 = {
    "Nombre" : "Sixto Manuel",
    "Apellido" : "García Romero",
    "Cedula" : 7504440,
    "Direccion": "Cra 12 # 10 10",
    "Telefono": 3103243030,
    "Titulo" : "Ingeniero",
    "Ciudad" : "Barranquilla",
    "Trabajo" : "Independiente"
}

print("Cantidad de datos: ", len(diccionario7),"\n")
print(diccionario7,"\n")
print(diccionario7.keys(), "\n")
print(diccionario7.values(),"\n")

# ejercicio 8

datos = {
    'id' : '934823429f34',
    'nombre': 'Andres',
    'apellido':'Pizarro',
    'email': 'apizarro@gmail.com',
    'telefono': 3249834894,
    'direccion': 'cra 43 # 40-34',
    'ciudad': 'Pereira',
    'departamento': 'Risaraldas',
    'pais': 'Colombia'
}

print(f'Numero de items: {len(datos)}')
print('Numero de items: ', len(datos))
print()

for clave in datos.keys():
    print(f'{clave} = {datos[clave]}')


diccionario8 = dict(
    id = '45238923gh23',
    nombre = 'Mauro',
    apellido = 'Posada',
    email = 'mposada@gmail.com',
    telefono = 32043454,
    github = '@mposada',
    instagram = '@mposadasites',
    direccion = 'cra 34 # 20 - 43'
)

print()
print('Cantidad de datos: ', len(diccionario8))
print(diccionario8)
print()
print(diccionario8.keys())
print()
print(diccionario8.values())
print()

# ejercicio 9

diccionario9 = {
    'clave1' : 4787,
    'clave2' : True,
    'clave3' : "Eduardo"
}

print(diccionario9)
print(type(diccionario9))

print(diccionario9['clave1'])
print(type(diccionario9['clave1']))
print(diccionario9['clave2'])
print(type(diccionario9['clave2']))
print(diccionario9['clave3'])
print(type(diccionario9['clave3']))


# Encapsulamiento con Diccionarios

def promedioNotas2(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']

    promedio = round(sumatoria / 4, 2)
    return promedio

dicNotas = {}

dicNotas['Nota1'] = 3.9
dicNotas['Nota2'] = 3
dicNotas['Nota3'] = 4
dicNotas['Nota4'] = 1

print('El promedio es de: ', promedioNotas2(dicNotas))

def promedioNotas3(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']

    promedio = round(sumatoria / 4, 2)
    return promedio

dicNotas3 = {
    'Nota1': 4,
    'Nota2': 3.6,
    'Nota3': 3.7,
    'Nota4': 2
}

print('El promedio es de: ', promedioNotas3(dicNotas3))

# paso entre funciones

def reportePromedio(dicReporte):
    return dicReporte['estudiante'] + " = " + str(dicReporte['promedio'])


def generarReporteNotas(dicNotas):
    sumatoria = 0
    sumatoria += dicNotas['Nota1']
    sumatoria += dicNotas['Nota2']
    sumatoria += dicNotas['Nota3']
    sumatoria += dicNotas['Nota4']

    promedio = round(sumatoria / 4, 2)
    reporteNotas = {
        'estudiante': dicNotas['estudiante'],
        'promedio': promedio
    }

    return reporteNotas

dicNotas4 = {
    'estudiante': 'Beneficiario R.',
    'Nota1': 4,
    'Nota2': 3.6,
    'Nota3': 3.7,
    'Nota4': 2
}

print(reportePromedio(generarReporteNotas(dicNotas4)))



