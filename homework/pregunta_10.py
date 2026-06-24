"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    lista_valor = []

    with open("files\input\data.csv", "r") as file:
        for linea in file:
            columns = linea.split("\t")
            suma_c_4  = len(columns[3].split(","))
            suma_c_5  = len(columns[4].replace("\n","").split(","))
            lista_valor.append((columns[0],suma_c_4,suma_c_5))

    return lista_valor

