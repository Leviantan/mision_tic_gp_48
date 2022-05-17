# Ciclo while

'''
n = 5
while n > 0: # -> condición del ciclo
    print(n)
    n = n - 1 # -> variable para el avance
print('Finalizar')
'''

# break -> Terminar la iteración del ciclo

'''
while True:
    numero = int(input('Ingrese un número: '))
    if numero % 2 == 0:
        print('El número es par')
        break
    else:
        print('El número es impar')
        break
'''

# ejercicio 2

'''
n = int(input('Por favor, ingrese un número mayor a cero. '))
while n > 0:
    print(n)
    print('Correcto!')
    break
'''

'''
n = int(input('Digite un número positivo. '))
while n > 0:
    print(n)
    n = n-1
print('Despegue!')
'''

# ejercicio 3
# Alejarse de la terminación

'''
i = 0
while i >= 0:
    print(i)
    i += 1
print('Finalizar')
'''

#ejercicio 4
# Brincarse la meta

'''
i = 1
while i != 10:
    print(i)
    i += 2
print('Finalizar')
'''

# ejercicio 5
# problema de indentación

'''
i = 1
while i < 10:
    print(i)
i = i + 1
print('Finalizar')
'''

# ejercicio 6
# olvidar el avance

'''
i = 1 
while i < 10:
    print(i)
print('Fin')
'''

# ejercicio 7
# mostrar los 40 primero numeros de 100

'''
n = 1
while n <= 100:
    print(n)
    if n == 40:
        break
    n = n+1
print('Fin') 
'''

'''
n = 1 
while n > 0:
    if n != 40:
        print(n)
        n += 1
    else:
        print('Llegamos a 40')
print('Fin')
'''

'''
n = 1
while n < 100:
    print(n)
    n -= 40
'''

'''
i = 0
while i <= 100:
    i +=1
    if i > 40:
        break
    print(i)
print('Fin')
'''

'''
j = 0 
while j <= 100:
    j +=1
    if j <= 40:
        print(j)
print('Fin')
'''

# ejercicio 8
# continue -> salto la iteración del ciclo

'''
n = 0
while n < 100:
    n += 1
    if n == 40:
        continue
    print(n)
print('Finalizar')
'''

# ejemplo 9
# Mostrar los primero 5 números impares, saltando el cuarto valor.

'''
1
3
5
9
11
'''

'''
n = -1
while n != 11:
    n = n + 2
    if n == 7:
        continue
    print(n)
print('Fin')
'''

'''
i = -1
while i < 11:
    i +=2
    if i >11:
        break
    print(i)
print('fin')
'''

'''
i = -1
while i < 50:
    i += 2
    if i == 31:
        break
    print(i)
print('Fin')
'''

'''
i = 0
impar = -1
while i <= 15:
    impar = impar + 2
    i = i + 1
    if i == 15:
        break
    print(impar)
print('Fin')
'''


