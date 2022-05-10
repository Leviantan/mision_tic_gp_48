# Forma de clasificaciín de condicionales

'''
# Decisiones simples

if:

if:
else:


horaDelDia = 8

if horaDelDia >= 12:
    print("PM")
else: # debe ser AM
    print("AM")
'''

'''
# Decisiones secuencia

if:
if:
if:
if:

resultadoExamen = 93

if resultadoExamen > 60:
    print("aprobado")

if resultadoExamen > 90:
    print("excelente actividad")
'''

'''
num = input('Por favor, ingrese un número entero: ')
num = int(num)

if (num < 0):
    num = num * ( -1 )
if num > 0:
    if ((num >= 1) and (num <= 9)):
        print('El número tiene 1 dígito')
    else:
        if (num >= 10) and (num <= 99):
            print('El número tiene 2 dígitos')
        else:
            if (num >= 100) and (num <= 999):
                print('El número tiene 3 dígitos')
            else:
                if num >= 1000 and num <= 9999:
                    print('El número tiene 4 dígitos')
                else:
                    print('El número tiena más de 4 dígitos')

print('final')

#num = int(input('Por favor, digite el número entero: '))

if num < 0:
    num *= -1
if num > 0 and num < 10:
    print('El número tiene 1 dígito')
elif num > 9 and num < 100:
    print('El número tiene 2 dígitos')
elif num > 99 and num < 1000:
    print('El número tiene 3 dígitos')
elif num > 999 and num < 10000:
    print('El número tiene 4 dígitos')
else:
    print('El número tiene mas de 4 digitos')
'''

num = int(input('Digite el numero entero: '))

'''
if num > 0:
    if ((num>= 10) and (num<=99)):
        print('El número es positivo y tiene 2 dígitos')
    else:
        print('El número es positivo y no tiene 2 dígitos')
if (num >= -999) and (num <= -1000):
    print('El número es negativo y tiene 3 dígitos')
else:
    print('El numero es negativo y no tiene 3 digitos')

print('fin')
'''


if num > 0:
    if ((num>= 10) and (num<=99)):
        print('El número es positivo y tiene 2 dígitos')
    else:
        print('El número es positivo y no tiene 2 dígitos')
else:
    if (num >= -999) and (num <= -1000):
        print('El número es negativo y tiene 3 dígitos')
    else:
        if num == 0:
            print('Número invalido')
        else:
            print('El numero es negativo y no tiene 3 digitos')

print('fin')









