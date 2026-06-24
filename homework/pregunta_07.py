"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    lista_valor = []
    
    filepath = pathlib.Path(__file__).parent.parent / "files" / "input" / "data.csv"
    with open(filepath, "r") as file:
        for linea in file:
            columns = linea.split("\t")
            lista_valor.append((columns[0],int(columns[1])))

    rango = max(lista_valor,key=lambda x: x[1])#Numero mas alto dentro de las tuplas 
    
    lista_rta = []
    for i in range(rango[1] + 1 ):
        marker = []
        for element in lista_valor: 
            if i == element[1]:
                marker.append(element[0])
            else:
                pass
        lista_rta.append((i,marker))
    
    return lista_rta