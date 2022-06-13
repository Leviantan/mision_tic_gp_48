def AutoPartes(ventas: list):
    # inicializar diccionario
    dicVenta = dict()

    # Ciclo para agregar un nuevo evento
    for idProducto, dProducto, pnProducto, cvProducto,sProducto, \
        nComprador, cComprador, fVenta in ventas:

        if dicVenta.get(idProducto) == None:
            # Creación de un nuevo item
            dicVenta[idProducto] = []
        
        dicVenta[idProducto].append((dProducto,pnProducto, cvProducto, \
            sProducto, nComprador,cComprador,fVenta))

    return dicVenta
        
def consultaRegistro(ventas, idProducto):
    
    # Verificar el ipProducto
    if idProducto in ventas:
        for dProducto,pnProducto,cvProducto,sProducto, \
            nComprador,cComprador,fVenta in ventas[idProducto]:

            # Mostrar todos los registros encontrados
            print('Producto consultado : ',idProducto, ' Descripción ' \
                , dProducto,' #Parte ', pnProducto,' Cantidad vendida' \
                , cvProducto, ' Stock ',sProducto,' Comprador' \
                , nComprador, ' Documento ', cComprador,' Fecha Venta ',fVenta)


