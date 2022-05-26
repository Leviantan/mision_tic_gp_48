# Inicializamos el diccionario

tareas = {
    '01':{
        'descripcion':'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },
    '02': {
        'descripcion': 'Estudiar',
        'estado': 'pendiente',
        'tiempo': 180,
    },
    '03': {
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50
    }
}

def create(tareas,identificador,tareaNueva):
    tareas[identificador] = tareaNueva
    return tareas

def read(tareas):
    for identificador,tarea in tareas.items():
        print(identificador,' - ',end='')
        for atributo in tarea.values():
            print(atributo, ' ,',end='')
        print()
    print()

def validarTarea(identificador,tareas):
    if identificador in tareas:
        return True
    else:
        return False
    
while True:

    print('\n --- Aplicación CRUD Tareas Pendientes --- \n')
    print(' 1: Adicionar Tarea')
    print(' 2: Consultar Tarea')
    print(' 3: Actualizar Tarea')
    print(' 4: Eliminar Tarea')
    print(' 5: Salir')

    opcion = int(input('Ingresar una opción : '))

    if opcion == 1:
        print()
        print(' -> Adicionar Tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea : '))

        if not validarTarea(identificador, tareas):
            descripcion = str(input('Ingrese la descripción de la tarea : '))
            estado = str(input('Ingrese el estado de la tarea : '))
            tiempo = int(input('Ingrese el tiempo de realización de la tarea : '))

            tareaNueva = {
                'descripcion': descripcion,
                'estado': estado,
                'tiempo': tiempo
            }

            # llamar a la función para agregar la tarea al diccionario.
            tareas = create(tareas,identificador,tareaNueva)
        else:
            print('La tarea ya existe!')
 
    elif opcion == 2:
        print()
        print(' -> Listado de tareas')
        print()

        # llamar la funcion para listar todas las tareas del diccionario.
        read(tareas)
    
    elif opcion == 3:
        print()
        print(' -> Actualizar Tarea')
        print()

        identificador = str(input('Ingrese el identidicador de la tarea para modificar : '))

        if validarTarea(identificador,tareas):
            nuevoDescripcion = str(input('Nueva descripción : '))
            if nuevoDescripcion:
                tareas[identificador]['descripcion'] = nuevoDescripcion
            nuevoEstado = str(input('Nuevo estado : '))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = int(input('Nuevo tiempo :'))
            if nuevoTiempo:
                tareas[identificador]['tiempo'] = nuevoTiempo
        else:
            print('No ha sido encontrada la tarea. ')

    elif opcion == 4:
        print()
        print(' -> Eliminar tarea')
        print()

        identificador = str(input('Ingrese el identidicador de la tarea para modificar : '))

        if validarTarea(identificador, tareas):
            tareas.pop(identificador)
        else:
            print('No es posible eliminar la tarea (no existe)')
    elif opcion == 5:
        break