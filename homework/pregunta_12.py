"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    lista_valor  = []
    with open("files\input\data.csv", "r") as file:
        for linea in file:
            columns = linea.split("\t")
            columns_split = columns[4].replace("\n","").split(",")
            numeros = []#Esta lista es para manejo en Bulk 
            
            for i in columns_split:
                i = i.split(":") 
                numeros.append(int(i[1]))

            lista_valor.append((columns[0],tuple(numeros)))

    dict_letras  = {}

    for i in lista_valor:
        if i[0] in dict_letras:
            dict_letras[i[0]] += sum(i[1])
        else:
            dict_letras[i[0]] = sum(i[1])

    dict_letras =  dict(sorted(dict_letras.items()))
    return dict_letras