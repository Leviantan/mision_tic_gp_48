# Función filter

'''
def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,5,3,2,7,6,4,11,56)
print('numero de elementos de la tupla original: ', len(tupla))
print(tupla)

resultado = tuple( filter(mayor_a_cinco, tupla) )
print('numero de elementos de la tupla filtrada: ', len(resultado))
print(resultado)

resultado = list( filter( lambda e: e>=5,tupla ) )
print('numero de elementos de la tupla filtrada: ', len(resultado))
print(resultado)
'''

pares = list() # []

for i in range(50):
    if i % 2 == 0:
        pares.append(i)
#print(pares)

tupla = tuple(range(30))
resultado = list( filter( lambda elemento: elemento % 2 == 0, tupla))
print('numeros pares : ', resultado)

resultado = list( filter( lambda elemento: elemento % 2, tupla))
print('numeros impres : ', resultado)

resultado = list( map( lambda e: e % 2 == 0, tupla ) )
print(resultado)
resultado = list( map( lambda e: e % 2, tupla ) )
print(resultado)