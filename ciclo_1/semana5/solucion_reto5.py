import pandas as pd

# Ruta del archivo csv
rutaFileCsv = 'https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv'

def listaPeliculas(rutaFileCsv: str)->str:
    # print(rutaFileCsv.split('.')[-1])

    # Validar la extensión del archivo
    if rutaFileCsv.split('.')[-1] == 'csv':
        
        try:
            # leer el archivo
            aCsv = pd.read_csv(rutaFileCsv)
            # print(aCsv)

            # Se crea un subconjunto con las columnas 'Country', 'Language' y 'Gross Earnings'
            subGrupoPeliculas = aCsv[['Country','Language','Gross Earnings']]
            #print(subGrupoPeliculas)

            # Se usa las columnas 'Country' y 'Language' como índice de la tabla dinámica,
            # y 'Gross Earnings' como tabla de resumen
            ganaciaPaisLenguaje = subGrupoPeliculas.pivot_table(index=['Country','Language'])

            return ganaciaPaisLenguaje.head(10)

        except:
            print('Error al leer el archivo de datos.')

    else:
        print('Extensión inválida')


print(listaPeliculas(rutaFileCsv))