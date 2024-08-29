"""Proyecto 4 MPSS.

Este módulo proporciona funciones para el
procesamiento y visualización de datos.

"""


# librerias a utilizar
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('seoul.csv')


def muestra(variable, loc, inicio, fin):
    """Muestra los datos filtrados por variable.

    ubicación y rango de fechas.

    """
    # Filtrar por ubicación

    df_filtrado_loc = df.loc[df["loc"] == loc]

    # Filtrar por fecha y hora del inicio y fin
    df_filtrado_fecha = df[(df['dt'] >= inicio) & (df['dt'] <= fin)]

    # Juntar el filtrado por loc y el filtrado por fecha/hora
    df_filtrado = df_filtrado_loc.merge(df_filtrado_fecha)

    # Dataframe que contiene solo las
    # columnas seleccionadas y con un nuevo índice.
    matriz = df_filtrado[['loc', 'dt', variable]].reset_index(drop=True)

    # Formato de fecha y hora
    matriz['dt'] = pd.to_datetime(matriz['dt'], format='%Y%m%d%H')

    print(matriz)

    return matriz


def proceso(intervalo, variable, loc, inicio, fin):
    """Realiza el proceso de muestras para un.

    intervalo de tiempo y variable dada.

    """
    if intervalo == "semanal":
        # Obtener el intervalo de tiempo semanal
        intervalo_inicio = inicio
        # Agregar una semana en segundos
        # (7 días * 24 horas * 60 minutos * 60 segundos)
        intervalo_fin = fin + 604800
    elif intervalo == "diario":
        # Obtener el intervalo de tiempo diario
        intervalo_inicio = inicio
        # Agregar un día en segundos
        # (24 horas * 60 minutos * 60 segundos)
        intervalo_fin = fin + 86400
    else:
        raise ValueError("Intervalo no válido. Debe ser 'semanal' o 'diario'.")

    # Lista para almacenar las funciones "muestra" del proceso
    funciones_muestra = []

    # Bucle para construir las funciones "muestra"
    # dentro del intervalo de tiempo especificado
    while intervalo_inicio <= fin:
        # Llamar a la función "muestra" con los parámetros actuales
        funcion = muestra(
            variable=variable,
            loc=loc, inicio=intervalo_inicio, fin=intervalo_fin
        )

        # Agregar la función "muestra" a la lista
        funciones_muestra.append(funcion)

        # Mover el intervalo de tiempo al siguiente período
        intervalo_inicio = intervalo_fin
        intervalo_fin += 604800 if intervalo == "semanal" else 86400

    # Devolver el conjunto de funciones "muestra"
    return funciones_muestra


def grafica(variable, loc, inicio, fin):
    """Genera una gráfica de la variable.

    para la ubicación y el rango de fechas dados.

    """
    matriz = muestra(variable, loc, inicio, fin)

    # Crear el gráfico
    plt.plot(matriz['dt'], matriz[variable])
    plt.xlabel('Fecha')
    plt.ylabel(f'Variable: {variable}')
    plt.title(
        f'Variable {variable} para loc {loc} (inicio: {inicio} - fin: {fin})'
        )
    plt.xticks(rotation=50)
    plt.show()
