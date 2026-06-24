"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    lista_letras = []
    letras = ["A","B","C","D","E"]
    filepath = pathlib.Path(__file__).parent.parent / "files" / "input" / "data.csv"
    with open(filepath, "r") as file:
        for linea in file:
            columns = linea.split("\t")
            lista_letras.append((columns[0],int(columns[1])))

    acumulador = {}

    for letra, numero in lista_letras:
    
        if letra in acumulador:
            acumulador[letra] += numero
        else:
            acumulador[letra] = 0 + numero
    lista_final = []
    
    for clave, valor in acumulador.items():
        lista_final.append((clave, valor))

    lista_final = sorted(lista_final, key=lambda x: (x[0], -x[1]))
            
    return lista_final