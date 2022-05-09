# condicionales operaciones boolean

var1 = 5
var2 = 5

'''
print(var1 > var2)
print(var1 >= var2)
print(var1 < var2)
print(var1 <= var2)
print(var1 != var2)
print(var1 == var2)
'''

'''
x = 10

print(x > 0 and x < 10)

print(4%2 == 0 or 4%3 == 0)
'''

'''
x = 10

if x > 0:
    print("x es un número clear
    ")
'''

'''
x = 37

if x % 2 == 0:
    print("x es un número par")
else:
    print("x es un número impar")
'''

'''
x = 20
y = 20

if x < y:
    print("x es menor a y")
elif x > y:
    print("x es mayor a y")
else:
    print("x es igual a y")
'''

'''
letra = 'a'

if letra == 'a':
    print('Mal resultado')
elif (letra == 'b'):
    print('Buen resultado')
elif (letra == 'c'):
    print('Cerca, pero no es correcto')
'''

'''
x = 9
y = 32

if x == y:
    print("x es igual a y")
else:
    if x > y:
        print("x es mayor a y")
    else:
        print("x es menor a y")
'''


'''
x = 11

if 0 < x and x < 10:
    print("correcto")
else:
    print("incorrecto") 
'''


temperatura_fahr = input('Ingrese la temperatura en grados fahr: ')
try:
    fahr = float(temperatura_fahr)
    c = (fahr - 32.0) * 5.0 / 9.0
    print(c)
except:
    print('No ingreso ningún número, gracias')




