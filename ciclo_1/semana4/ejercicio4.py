# importar pow
from math import pow

# la función pow toma dos argumentos, renumero y potencia
# print(pow(2, 3))

numeros = [1,2,3,4,3,4,5,6,7,8,7,6]
potencias = [5,6,7,8,9]

resultado = tuple( map(pow,numeros,potencias) )
print(resultado)
