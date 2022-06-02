def ordenes(rutinaContable):
    # importar la función 'reduce' desde la libreria functools
    from functools import reduce as r

    # Valor minimo de venta
    valorMinimo = 600000
    # Valor incremento de la venta
    valorIncre = 25000

    # Sumar el total de cada tupla de cada lista
    ordenTotal = list( map( lambda x: [x[0]] + list( map( lambda y: y[1]*y[2], x[1:] ) ),rutinaContable ) ) 
    # Sumar los totales de todas las tuplas de toda la lista
    ordenTotal = list( map( lambda x: [x[0]] + [ r( lambda acu,elem: round(acu+elem, 2), x[1:]) ], ordenTotal ) )
    # Suma incremento si la venta no llega al minimo
    ordenTotal = list( map( lambda x: (x[0],x[1]) if x[1] >= valorMinimo else (x[0],x[1] + valorIncre), ordenTotal ))

    print('------------------------ Inicio Registro diario ---------------------------------')
    # Ciclo imprimir las facturaa con su total
    for x in range(len(ordenTotal)):
        print(f'La factura {ordenTotal[x][0]} tiene un total en pesos de {ordenTotal[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')


# Pruebas

rutinaContable = [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

ordenes(rutinaContable)


'''

[
    [1201], 
    [1202], 
    [1203], 
    [1204]
]

[
    [1201, 103371.96, 418589.82, 440567.55], 
    [1202, 346087.74, 42389.81999999999], 
    [1203, 125698.2, 271290.4, 13645.2, 8226.0], 
    [1204, 83.93, 208.89, 1954.75]
]

[
    [103371.96, 962529.33], 
    [346087.74, 388477.56], 
    [125698.2, 418859.8], 
    [83.93, 2247.57]
]

[
    [103371.96, 962529.33], 
    (346087.74, 413477.56), 
    (125698.2, 443859.8), 
    (83.93, 27247.57)
]

[
    [103371.96, 962529.33], 
    [346087.74, 413477.56], 
    [125698.2, 443859.8], 
    [83.93, 27247.57]
]

[
    (103371.96, 962529.33), 
    (346087.74, 413477.56), 
    (125698.2, 443859.8), 
    (83.93, 27247.57)
]

'''