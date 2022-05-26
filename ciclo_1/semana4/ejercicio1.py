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

tupla = ('hola',111,'mundo','hola')
conjunto = set(tupla)
conjunto.add(13)
print(conjunto)
