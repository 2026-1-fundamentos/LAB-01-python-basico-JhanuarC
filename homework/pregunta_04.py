"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import pathlib


"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

def pregunta_04():
    lista_fechas = []
    filepath = pathlib.Path(__file__).parent.parent / "files" / "input" / "data.csv"
    with open(filepath, "r") as file:
            for linea in file:
                columns = linea.split("\t")
                lista_fechas.append(columns[2])  

    conteo_meses = {}
    for fecha in lista_fechas:
        mes = fecha.split("-")[1]  #
        conteo_meses[mes] = conteo_meses.get(mes, 0) + 1

    resultado = sorted(conteo_meses.items())
    return resultado

