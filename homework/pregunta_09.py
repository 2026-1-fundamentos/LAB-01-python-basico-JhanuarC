"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    lista_valor = []

    with open("files\input\data.csv", "r") as file:
        for linea in file:
            columns = linea.split("\t")
            columns_split = columns[4].replace("\n","").split(",")
            for i in columns_split:
                i = i.split(":")
                lista_valor.append(i[0])
        
    dic_keys = {}
    for i in lista_valor:
        if i in dic_keys:
            dic_keys[i] += 1
        else:
            dic_keys[i] = 1

    dic_keys = dict(sorted(dic_keys.items()))
    
    return dic_keys
