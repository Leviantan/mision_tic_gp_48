# Envolturas en funciones python.

'''
def suma(val1= 0,val2= 0):
    return val1 + val2
print(suma())

# Asignar una funcion a una variable.
funcion_suma = suma

# Enviar como parametro una funcion.

def operacion(funcion,val1,val2):
    return funcion(val1,val2)

resultado = operacion(funcion_suma,25,20)
print(resultado)
'''

# Envoltura de funciones.

'''
def crear_funcion(operador):
    if operador == '+':
        def suma(val1= 0, val2 = 0):
            return val1 + val2
        return suma
    if operador == '-':
        def resta(val1, val2):
            return val1 - val2
        return resta

def operacion(funcion,val1 = 0, val2 =0):
    return funcion(val1,val2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma,50,50)

print(resultado)

funcion_resta = crear_funcion('-')
resultado = operacion(funcion_resta,26,24)
print(resultado)

'''

# Función Anónima (lambda)

'''
def sumar(val1 = 0, val2 = 0):
    return val1 + val2

sumar = lambda val1 = 0, val2 = 0 : val1 + val2
operacion = lambda operacion,val1 = 0, val2 = 0 : operacion(val1,val2)

resultado = operacion(sumar,37,43)
print(resultado)
'''

# Función lambda sin parametros.

'''
sin_parametros = lambda : True
print(sin_parametros() ==   True)
'''

# Funcion lambda con valores

'''
con_valores = lambda val, val1 = 0, val2 = 0 : val + val1 + val2
resultado = con_valores(5,10,25)

print(resultado)
'''

# Funcion lambda con *args.
# *args significa cero o mas parametros que se almacenan en tuplas.

'''
con_asterisco = lambda *args : args[0]
lista = [1,2,3,4,5,6,7]

resultado = con_asterisco(*lista)
print(resultado)

resultado = con_asterisco(2)
print(resultado)

resultado = con_asterisco(1,2,3,4,5,6,7,8,9,8,7,6,5,4)
print(resultado)

def suma (*valor):
    return sum(valor)

print(suma(1,2,3,4,5,6,7,8,9))
'''

# **kwargs 

lista = [1,2,3,4,5,6,7]

con_doble_asterisco = lambda **kwargs : kwargs[0]

resultado = con_doble_asterisco(**lista)
