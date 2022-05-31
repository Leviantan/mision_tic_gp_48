# Conversión entre contenedores

# conversión de cadenas
# cadena -> lista (str - list)

'''
cadena = 'hola'
lista = list(cadena)
print(lista)
'''

# cadena -> tupla (str - tuple)

'''
cadena1 = 'hola'
cadena2 = 'mundo'
numero = 18
tupla = tuple(cadena1)
tuplaGeneral = (tupla,numero,tuple(cadena2))
print(tupla)
print(tuplaGeneral)
'''

# cadena -> conjunto (str - set)

'''
cadena = 'hhola'
conjunto = set(cadena)
print(conjunto)
'''

# Conversión listas
# lista - cadena (list - str)

'''
lista = ['h','o','l','a',(6,7)]

try:
    cadena = ''.join(lista)
    print(cadena)
except:
    print('No se puede concatenar tipo de datos diferentes a str')

cadenaConvertir = ''
for elemento in lista:
    cadenaConvertir = cadenaConvertir + str(elemento)

print(cadenaConvertir)
'''

# lista -> tupla (list - tuple)

'''
lista = ['h','o','o','l','a',123,123,(1,2,3)]
tupla = tuple(lista)
print(tupla)
'''

# lista -> conjunto (list - set)

'''
lista =  ['h','o','o','l','a',1,1,2,2,3]
conjunto = set(lista)
print(conjunto)
'''

# Convertir Tuplas
# tupla -> cadena (tuple - str)

'''
tupla = ('h','o','l','a')
cadena = ''.join(tupla)
print(cadena)
'''

# tupla -> lista (tuple - list)

'''
tupla = ('hola',123,'mundo')
lista = list(tupla)
print(lista)
'''

# tupla -> conjunto (tuple - set)

'''
tupla = ('hola',111,'mundo','hola')
conjunto = set(tupla)
conjunto.add(13)
print(conjunto)
'''

# Conjunto -> Cadena (set - str)

'''
conjunto = {'h','o','l','a'}
cadena = ''.join(conjunto)
print(cadena)
'''

# conjunto -> tupla (set - tuple)

'''
conjunto = {'h','o','l','a'}
tupla = tuple(conjunto)
print(tupla)
'''

# conjunto -> lista (set - list)

'''
conjunto = {'h','o','l','a'}
lista = list(conjunto)
print(lista)
'''

# Conversión a diccionario.
# cadena -> diccionario (str - dict)

'''
cadena = 'grupo_48'

diccionario = dict()

for posicion in range(len(cadena)):
    diccionario[posicion] = cadena[posicion]
print(diccionario)

diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)
'''

# lista -> diccionario (list - dict)

'''
lista = ['h','o','l','a']
diccionario = dict(zip(range(len(lista)),lista))
print(diccionario)
'''

# tupla -> diccionario (tuple - dict)

'''
tupla = ('h','o','l','a')
diccionario = dict(zip(range(len(tupla)), tupla))
print(diccionario)
'''

# conjunto -> diccionario (set - dict)

conjunto = {'h','o','l','a'}
diccionario = dict(zip(range(len(conjunto)),conjunto))
print(diccionario)