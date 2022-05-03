# Crear una función
def imprime_Cosas():
    print("La clase esta genial")
    print("Python es lo máximo")

# llamar una función
# imprime_Cosas()

def repetir_funciones():
    print("\n")
    imprime_Cosas()
    imprime_Cosas()

# repetir_funciones()

def operacionSuma():
    a = 4
    b = 16
    suma = a + b
    return "La suma de " + str(a) + " + " + str(b) + " es igual a: " + str(suma)

resultado = operacionSuma()

#print(type(resultado))
#print(resultado)

#print(operacionSuma())

def operacionSumaP():
    a = 24
    b = 66
    suma = a + b
    print("La suma de",a,"+",b,"es igual a:",suma)

#operacionSumaP()

'''
def sumarDosnumeros():
    num1 = float(input("Ingrese el numero 1: "))
    num2 = float(input("Ingrese el numero 2: "))
    print("La suma de", int(num1),"+", int(num2) , "es igual a:", int(num1 + num2))

# Llamar la función sumarDosnumeros
#sumarDosnumeros()
'''

def raizCuadrada():
    valor = float(input("Por favor, introduzca un numero a calcular su raiz cuadrada "))
    raiz = valor ** 0.5
    return print("La raiz cuadrada de :", valor,"es",valor ** 0.5)
    #return raiz

# print("El resultado de la raiz cuadrada es : ", raizCuadrada())

#raizCuadrada()

def raizcubica():
    valor = float(input("Por favor, introduzca un numero a calcular su raiz cubica "))
    raiz = valor ** 0.3
    #return print("La raiz cubica de :", valor,"es",round((valor ** 0.3))) 
    return print("La raiz cubica de :", valor,"es",round(raiz))   

#raizcubica()


# Creación de funciones con argumentos o parametros

def suma(a,b):
    return (a + b) 

# print(suma(45,55))

a = 3
b = 7

#print(suma(a,b))


# Crear la función
def mi_funcion(nombre, apellido):
    miNombre = nombre + apellido
    return miNombre

# print(mi_funcion("Luis ", "Molero"))

# Creamos la función saludar
def saludar(nombre, mensaje = "Hola"):
    print(mensaje,nombre)

# llamar la función
#saludar("Pepe Grillo")


# Creamos la función
def mensaje():
    print("Ingrese por favor un valor")
    
# Creamos la función
def sumarDosnumeros():
    mensaje()
    num1 = float(input())
    mensaje()
    num2 = float(input())
    suma = num1 + num232

    return print("La suma de", num1, "+", num2, "es igual a:",suma)

# llamar la función sumarDosnumeros
# sumarDosnumeros()

'''
def primeraFuncion(): # función externa
    print("\n \"Hola desde la función externa\" \n")
    def segundaFuncion(): # función interna
        print("\n \"Hola desde la función interna\" \n")

    segundaFuncion()

primeraFuncion()
'''


'''
def primerNumero(x):
    def segundoNumero(y):
        return x * y
    return segundoNumero

resultado = primerNumero(2)
print(type(resultado))
print(resultado(5))
'''

def primeraFuncion():
    x = 2
    def segundaFuncion(a):
        x = 6
        print(a + x)
        return x
    # llamo la función
    x = segundaFuncion(3)
    print(x)

# llamo la función
primeraFuncion()



