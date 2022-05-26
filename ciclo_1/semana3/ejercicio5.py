# Creación de conjuntos
# Para crear un conjunto especificamos sus elementos entre llaves.

s = {1,2,3,4,5}
print(type(s))
print(s)

# Al igual que otras colecciones, sus elementos puede ser de diferente tipo de datos.

s = {True,3.14,None,False,"Hola grupo 48",(3,4)}
print(type(s))
print(s)


# Los conjuntos no pueden incluir objetos mutables como las listas.

'''
s = {[1,2]}
'''

# Python distingue este tipo de operación 
# para crear un diccionario a pesar que no se incluyen los dos puntos.

'''
s = {}
print(type(s))
'''

# para crear un conjunto vacio utilizamos el constructor set
s = set()
print(s)

# De la misma forma podemos obtener un conjunto a partir de cualquier objeto mutable.

s1 = set([1,2,3,4])
s2 = set(range(10))

print()
print(s1)
print(s2)

# un conjunto puede ser convertido a una lista y viseversa, en el ultimo caso
# los elementos duplicados son unificados.

lista = list({1,2,3,4,5})
conjunto = set([1,2,3,4,5])

print(lista)
print(conjunto)

# los elementos repetidos en un conjunto se eliminan.

c = {1,3,2,9,3,1}
print(c)

# Crea un conjunto a partir de un String

a = set('Hola grupo 48')
print(a)

# se puede acceder y recorrer todos los elementos de un conjunto.

conjunto = {1,3,2,9,3,1}
print(conjunto)

for numero in conjunto:
    print(numero)

'''
listaC = list(conjunto)

print(listaC)
listaC.reverse()
print(listaC)

print(dir(conjunto))
'''

print(' -------------------------- ')
# Métodos de los conjuntos.

# add(), agregar un elemento a un conjunto.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
print(setMutable1)
setMutable1.add(20.55555)
setMutable1.add(9)
setMutable1.add(9)
print(setMutable1)
'''

# clear(), Eliminamos o removemos todos los elementos de un conjunto.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
print(setMutable1)
setMutable1.clear()
print(setMutable1)
'''

# copy(), devuelve una copia del conjunto.

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
setMutableCopy = setMutable1.copy()

print(setMutableCopy)


conjunto = set([4.0, 'Carro',True,1,3,4,'20'])
conjuntoCopy = conjunto.copy()

print(conjunto)
print(conjuntoCopy)
print(conjunto == conjuntoCopy)
'''

# difference(), devuelve la diferencia que hay entre dos conjunto

'''
setMutable1 = set([4,3,11,7,5,2,1,4])
setMutable2 = set([11,5,9,2,4,8])

print()
print(setMutable1)
print(setMutable2)
print(setMutable1.difference(setMutable2))
print(setMutable2.difference(setMutable1))
'''

# difference_update(), se actuliza el conjunto.

'''
c1 = {'python','Zope2','ZODB3','pytz'}
c2 = {'python','Plone','diazo'}

print(c1)
print(c2)
c1.difference_update(c2)
print(c1)
'''

# pop(), eliminar un elemento aleatorio del conjunto.

'''
paquetes = {'python','zope','plone','django'}
print(paquetes)
print('Valor aleatorio devuelve es : ', paquetes.pop())
print('Valor aleatorio devuelve es : ', paquetes.pop())
print('Valor aleatorio devuelve es : ', paquetes.pop())
print(dir(paquetes))
'''

# remove(), Buscar y eliminar un elemento del conjunto

'''
paquetes = {'python','zope','plone','django'}
print(paquetes)
paquetes.remove('zope')
print(paquetes)
'''

# update(), agregar elemento de un conjunto mutable

'''
version = set([4.6])
version_plone = set([2.1,2.5,3.6,4])

print(version)
print(version_plone)

version.update(version_plone)
print(version)
'''

