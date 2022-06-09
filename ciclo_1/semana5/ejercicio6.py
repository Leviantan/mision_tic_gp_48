# leer archivo txt

datos = ['linea 1','linea 2','linea 3','linea 4','linea 5']

ruta = r'C:\Users\israelarbonaguerrero\Desktop\RUTA2_MISIONTIC_2022\grupo_48\ciclo_1\semana5\archivo.txt'
fichero = open(ruta,'w')

for i in range(2001):
    for x in datos:
        valor = str(i)+', ' + x
        fichero.write(valor)
    fichero.write('\n')

fichero.close()