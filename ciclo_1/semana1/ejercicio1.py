# declaramos una variable de tipo entero (Numero)
var_int = 40

# declaramos una variable de tipo float, double (Numero)
var_pi = 3.1416

# declaramos una variable de tipo cadena de texto (String)
var_str = "Grupo 48"

# declaramos una variable de tipo boolean (True, False)
var_boo = False

# declaramos una variable de tipo diccionario
var_dict = {
    "nombre": "Juliana",
    "apellido": "Correa",
    "edad": 37
}

# modificar el valor de campo del diccionario
var_dict["nombre"] = "Maria"

# agregar campo a la variable de diccionario
var_dict["peso"] = 53.6

# eliminar un campo del diccionario
var_dict.pop("apellido")


'''     
    # comentar un bloque de código        -- tres comillas siples

print("El nombre de la persona es " + var_dict["nombre"] + " y tiene " 
                                    + str(var_dict["edad"]) 
                                    + " edad y su peso es " + str(var_dict["peso"]))

print("El nombre de la persona es " + var_dict["nombre"] + " y tiene", var_dict["edad"])

print(f"El nombre de la persona es {var_dict['nombre']} y tiene {var_dict['edad']}")

print("El nombre de la persona es {} y tiene {}".format(var_dict["nombre"],var_dict["edad"]))

print(f"el valor de la variable var_pi es {var_pi}")
'''

var = "3.7.1"
print(var)
print(type(var))

var = 1.5
print(var)
print(type(var))

var = var + 5
print(var)
print(type(var))

var = 500
print(var)
print(type(var))

var = 30 + 50
print(var)
print(type(var))

