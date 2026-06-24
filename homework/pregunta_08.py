"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]


         """
    lista_valor = []
    
    with open("files\input\data.csv", "r") as file:
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
        
        lista_rta.append((i,list(sorted(set(marker)))))
    
    return lista_rta
