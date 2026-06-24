"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    lista_valor = []

    filepath = pathlib.Path(__file__).parent.parent / "files" / "input" / "data.csv"
    with open(filepath, "r") as file:
        for linea in file:
            columns = linea.split("\t")
            lista_valor.append((int(columns[1]),columns[3]))
   
   
    #print(lista_valor)
   
   
    dict_keys = {}
    for element in lista_valor:
        string = element[1].strip(",")
        for i in string:
            if i == ",":
                pass
            elif i in dict_keys:
                dict_keys[i] += element[0]
            else:
                dict_keys[i] = element[0]
    dict_keys =  dict(sorted(dict_keys.items()))
    return dict_keys
