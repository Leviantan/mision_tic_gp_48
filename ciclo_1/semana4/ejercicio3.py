# Función map

'''
def cuadrado(elemento = 0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

resultado = list( map(cuadrado,lista) )
print(resultado)

resultado_l = list( map( lambda elem: elem * elem, lista ) )
print(resultado_l)
'''

def factorial(numero = 0):
    contar = 2
    resultado = 1
    while contar <= numero:
        resultado *= contar
        contar += 1
    return resultado

lista = [1,2,3,4,5,6,7,8,9]
resultado = list( map( factorial,lista))

print(resultado)
