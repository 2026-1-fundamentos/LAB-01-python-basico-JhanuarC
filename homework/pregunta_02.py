"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    lista_letras = []
    letras = ["A","B","C","D","E"]
    lista_final = []

    with open("files\input\data.csv", "r") as file:
        for linea in file:
            columns = linea.split("\t")
            lista_letras.append(columns[0])
            
    lista_letras.sort()
    
    for letra in letras:
        lista_final.append((letra,lista_letras.count(letra)))

    
    return lista_final