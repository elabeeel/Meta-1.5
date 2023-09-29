import pandas as pd
import random
def cargar_csv(ruta):
    """
    Carga un archivo CSV y devuelve un DataFrame.
    """
    try:
        datos = pd.read_csv(ruta)
        return datos
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {ruta} no existe.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"El archivo {ruta} está vacío o no es un archivo CSV válido.")

def primeras_lineas(datos, n):
    """
    Devuelve las primeras n líneas del DataFrame.
    """
    if n <= 0:
        raise ValueError("n debe ser mayor que cero.")
    return datos.head(n)

def ultimas_lineas(datos, n):
    """
    Devuelve las últimas n líneas del DataFrame.
    """
    if n <= 0:
        raise ValueError("n debe ser mayor que cero.")
    return datos.tail(n)

def aleatorio_lineas(datos, n):
    """
    Devuelve n líneas aleatorias del DataFrame.
    """
    if n <= 0:
        raise ValueError("n debe ser mayor que cero.")
    return datos.sample(n)

def nombres_columnas(datos):
    """
    Devuelve una lista con los nombres de las columnas del DataFrame.
    """
    return datos.columns.tolist()

def tipos_datos_columnas(datos):
    """
    Devuelve una lista con los tipos de datos de las columnas del DataFrame.
    """
    return datos.dtypes.tolist()

def dimensiones_dataframe(datos):
    """
    Devuelve las dimensiones del DataFrame como una tupla (filas, columnas).
    """
    shape = datos.shape
    return (shape[0], shape[1])


ruta_csv = "C:\Users\lange\PycharmProjects\meta 1.5.csv"
datos_csv = cargar_csv(ruta_csv)
primeras = primeras_lineas(datos_csv, 5)
print(primeras)