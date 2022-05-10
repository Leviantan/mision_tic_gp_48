# Acceder a los caracteres de uno en uno en la cadena de texto

# ejercicio 1

fruta = 'fresa'
letra = fruta[1]
print(letra)

fruta = 'banana'
letra = fruta[0]
print(letra)

# Conseguir la longitud de una cadena (String)

# ejercicio 2
fruta = 'banana'
longitud = len(fruta)
print(longitud)

print(fruta[longitud - 1])

print(fruta[-6])

# Rebanadas de una cadena

# ejercicio 4
s = 'Monty_Python'
#    0 1 2 3 4 5 6 7 8 9 10 11

print(s[0:6])
print(s[6:12])

# ejercicio 5

fruta = 'banana'
print(fruta[:3])
print(fruta[3:])

print(fruta[3:3])
print(fruta[:])

# Inmutabilidad de una cadena -- solo es posible crear una nueva cadena

saludo = 'Hola mundo'
# saludo[0] = 'j'

nuevo_saludo = 'j' + saludo[1:]
print(nuevo_saludo)


# Operador in, devuelve repuesta booleana si una cadena 
# se encuentra dentro de otra cadena

var1 = 'a'
var2 = 'banana'
print(var1 in var2)

var1 = 'ala'
var2 = 'banana'
print(var1 in var2)


# Comparación de cadenas

palabra = 'banana'

if palabra == 'banana':
    print('las palabras son iguales (bananas)')


palabra2 = 'Pera'

if (palabra2 < 'banana'):
    print('La palabra ' + palabra2 + ' , viene antes de banana')
elif (palabra2 > 'banana'):
    print('La palabra ' + palabra2 + ' , viene despues de banana')
else:
    print('las palabras son iguales')


# Conseguir el tipo de datos de una variable 
# y los métodos asociados a ese tipo de variable

# ejercicio 11

cadena = 'Grupo_48'
print(type(cadena))
# print(dir(cadena))


# Convertir una cadena en mayusculas

palabra = 'fresa'
nueva_palabra = palabra.upper()
print(nueva_palabra)

# Retornar la posición de una subcadena dentro de una cadena

palabra = 'banana'
posicion = palabra.find('a')
print(posicion)

print(palabra.find('na'))
print(palabra.find('na', 3))

# Retirar los espacios de los extremos de una cadena

linea = '          Aquí vamos               '
print(linea.strip())

linea = 'Que Tengas Un Buen Día'
print(linea.startswith('Que'))
print(linea.startswith('que'))

print(linea.lower().startswith('q'))


# Pieza de código que permite cortar 
# el host del correo electronico e imprimirlo luego

# conseguir @
dato = 'De stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
posicion = dato.find('@')
print(posicion) # imprime el valor entero de la posición
espacio = dato.find(' ',posicion)
print(espacio)
host = dato[posicion+1:espacio]
print(host)


