"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    lista_valor= []
    filepath = pathlib.Path(__file__).parent.parent / "files" / "input" / "data.csv"
    with open(filepath, "r") as file:
        for linea in file:
            columns = linea.split("\t")
            columns_split = columns[4].replace("\n","").split(",")
            for element in columns_split:   
                element = element.split(":")
                lista_valor.append((element[0],int(element[1])))
    
    valor = []
    for i in lista_valor:
        valor.append(i[0])
    valor = sorted(set(valor))
    

    lista_rta = []

    for i in valor:
        filtro = [tup for tup in lista_valor if tup[0] == i]
        maxi = max(filtro, key=lambda x: x[1])
        mini = min(filtro, key=lambda x: x[1])
        lista_rta.append((i,mini[1],maxi[1]))
        
    return lista_rta