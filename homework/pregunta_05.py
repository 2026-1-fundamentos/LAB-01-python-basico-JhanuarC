"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib

"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

"""
def pregunta_05():

    lista_letras = []
    filepath = pathlib.Path(__file__).parent.parent / "files" / "input" / "data.csv"
    with open(filepath, "r") as file:
        for linea in file:
            columns = linea.split("\t")
            lista_letras.append((columns[0],int(columns[1])))
    
    lista_rta = []

    for i in ["A","B","C","D","E"]:
        filtro = [tup for tup in lista_letras if tup[0] == i]
        maxi = max(filtro, key=lambda x: x[1])
        mini = min(filtro, key=lambda x: x[1])
        lista_rta.append((i,maxi[1],mini[1]))
    
    return lista_rta
