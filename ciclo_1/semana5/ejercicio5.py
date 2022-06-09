# Creación de archivos txt

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_48\ciclo_1\semana5\archivo.txt'

# Crear y escribir archivo txt (Elimina el contenido del txt)
fichera = open(ruta,'w')

# Agregar información al final del archivo txt
fichero = open(ruta,'a')

# Solo lectura del archivo txt
fichero = open(ruta,'r')

fichero.close()

