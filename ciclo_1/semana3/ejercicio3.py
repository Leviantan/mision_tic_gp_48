# Lista

'''
lista =[2.1,2.5,'DevCode',[10,11],5] 

print(lista[0]) # 2.1
print(lista[1]) # 2.5
print(lista[2]) # DevCode
print(lista[3]) # [10,11]
print(lista[3][0]) # 10
print(lista[3][1]) # 11
print(lista[1:9])
print(lista[1:6:2])
'''

# ejercicio 2

# variable vacia

'''
lista = []
lista2 = list()

print(lista)
print(lista2)
'''

# ejercicio 3

'''
nombre = 'Juan'
edad = 32

lista3 = [nombre,edad]
print(lista3)

nombre = 'Carlos' # Queda en memoria cargada ?
print(lista3)
'''

#Ejercicio 4

'''
nombres = ['Juan','Luis']
edades = [21,24]
lista4 =[nombres,edades]

print(lista4)

nombres += ['Carolina'] # si qued cargada.
print(lista4)
'''

# Ejercicio 5
# Método append(), agregar un elemento al final de una lista.

'''
versiones_plone = [2.1,2.5,3.6,4,5]
print(versiones_plone)

versiones_plone.append(9)
print(versiones_plone)
'''

# Ejercicio 6 
# Método count(), recibe un elemento como argumento, y cuenta las veces que aparece en la lista.

'''
versiones_plone = [2.1,2.5,3.6,6,4,5,6]
print('6 ->',versiones_plone.count(6))
'''

#Ejercicio 7
# Método extend(), extiende una lista agregando una iteración al final.

'''
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone)

versiones_plone.extend([5])
print(versiones_plone)
versiones_plone.extend(range(12))
print(versiones_plone)
'''

# Ejercicio 8
# Método index(), recibe un elemento como argumento 
# y devuelve el índice de primera aparición en la lista

'''
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone.index(6))
'''

# Ejercicio 9
# Método insert(), inserta el elemento x en la lista,en el índice i.

'''
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.insert(1, 5.4)
print(versiones_plone)
'''

# Ejercicio 10
# Método pop(), devuelve el ultimo elemento de la lista. 
# ademas podemos enviar un argumento el cual va funcionar como índice.

'''
versiones_plone = [2.1,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.pop(2)
print(versiones_plone)
'''

# Ejercicio 11
# Método remove(), recibe un argumento y borra su primera aparición

'''
versiones_plone = [2.1,4,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.remove(4)
print(versiones_plone)
'''

# Ejercicio 12
# Método reverse(), invertir el orden los elemento de una lista

'''
versiones_plone = [8,4,9,2.1,2.5,3.6,4,5,6]
print(versiones_plone)
'''
'''
versiones_plone.reverse()
print(versiones_plone)
'''

#Ejercicio 13
#Método sort(), Ordena los elemento de una lista.

'''
versiones_plone = [8,4,9,2.1,2.5,3.6,4,5,6]
print(versiones_plone)
versiones_plone.sort()
print(versiones_plone)

versiones_plone.sort(reverse = True)
print(versiones_plone)
'''

'''
versiones_plone = ['a','b', 'P']
print(versiones_plone)

versiones_plone.sort()
print(versiones_plone)
'''
