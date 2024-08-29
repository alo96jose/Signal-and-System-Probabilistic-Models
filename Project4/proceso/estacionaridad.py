"""Definiciones de funciones de wss(), prom_temporal() y ergodicidad().

Se trata de un programa que contiene tres funciones como parte del paquete
proceso.
"""

import pandas as pd
import numpy as np
import math
from proceso import proceso, momentos


def wss(intervalo, variable, loc, inicio, fin):
    """
    Función que determina si la secuencia aleatoria M(t) es WSS.

    Implementar una función wss() capaz de determinar si la
    secuencia aleatoria es estacionaria en sentido amplio.
    Se basa en verificar 2 requisitos:
    1. E[X(t)] = Constante.
    2. E[X(t)X(t+τ)] == Rxx(τ).

    Parameters
    ----------
    intervalo : str
        Solo dos opciones: "semanal" o "diario".
    variable : str
        Opciones "so2", "no2", "co", "o3", "pm10", "pm2.5".
    loc : int
        Opciones desde 102 hasta 125
    inicio : int
        Fecha de inicio, ejemplo, 2020031400
    fin : int
        Fecha de fin, ejemplo, 2020031723

    Returns
    -------
    PROMEDIO : float
        Es el valor promedio de los promedios
        de las muestras por hora.
    """
    # Llamada a función proceso()
    matriz = proceso.proceso(intervalo, variable, loc, inicio, fin)

    # Se guarda copia matriz original
    M = matriz

    # Lista de DataFrames se convierte en DataFrame
    matriz = pd.concat(matriz, ignore_index=True)

    # Deshacerse de columna loc
    matriz = matriz.loc[:, ["dt", "o3"]]

    # Deshacerse de filas con valores NaN
    matriz.dropna(subset=['o3'], inplace=True)

    # Cambio de formato para fecha y hora
    matriz['dt'] = pd.to_datetime(matriz['dt'], format="%Y%m%d%H")

    # Creación lista de horas
    horas = [
        '00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00',
        '06:00:00', '06:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00',
        '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
        '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00']

    # Se inicializa un vector vacío
    vector = []

    # Matriz de 24 horas x n columnas de días
    for x in horas:
        # Subconjunto de datos hora XX:00:00
        hora_x = matriz.loc[matriz['dt'].dt.time == pd.to_datetime(x).time()]
        # Se extraen únicamente muestras
        muestra = hora_x['o3'].values
        # Cada conjunto de muestras por hora se agrega en lista
        vector.append(muestra)

    # Unir cada conjunto de muestras con hora en matriz 24xn
    matriz = pd.DataFrame(list(zip(horas, vector)), columns=['Horas', 'Días'])
    print(matriz)

    # Requisito 1: ¿Promedio constante?

    print(" ")
    print("Requisito 1: ¿Promedio constante? ")
    print(" ")

    # Crear un vector vacío para guardar los promedios de las muestras
    mean_vector = []

    # Calcular el promedio de cada lista y anexarlo al vector vacío anterior
    for lst in matriz['Días']:
        mean_value = np.mean(lst)
        mean_vector.append(mean_value)

    # Unir cada hora con su promedio en un DataFrame
    promedios = pd.DataFrame(list(zip(horas, mean_vector)),
                             columns=['Horas', 'Promedio de Días'])
    print('')
    print('Promedio de días según hora: ')
    print('')
    print(promedios)

    # Promedio de los promedios
    PROMEDIO = promedios['Promedio de Días'].mean()
    print(" ")
    print('El promedio de los promedios es: ', PROMEDIO)
    print(" ")

    # Promedio de los promedios con +5% tolerancia
    mas5 = PROMEDIO + 0.05*PROMEDIO

    # Promedio de los promedios con -5% tolerancia
    menos5 = PROMEDIO - 0.05*PROMEDIO

    print(" ")
    print("Promedio será constante si se mantiene entre el rango [",
          menos5, ',', mas5, ']')
    print(" ")

    # El promedio máximo en lista promedios es
    print("El promedio máximo en lista promedios es ")
    print(float(promedios['Promedio de Días'].max()))
    print(" ")

    # El promedio mínimo en lista promedios es
    print("El promedio mínimo en lista promedios es ")
    print(float(promedios['Promedio de Días'].min()))
    print(" ")

    # Lista pasa a arreglo
    vector = np.array(promedios['Promedio de Días'])

    # Se verifica que promedios se mantenga en rango tolerancia
    valida = ((vector >= menos5) & (vector <= mas5)).all()
    if valida:  # Si valida == True
        print("El promedio es constante. Se cumple requisito 1. ")
    else:
        print("El promedio no es constante. No se cumple requisito 1. ")

    # Requisito 2: ¿E[X(t)X(t+τ)] == Rxx(τ)?
    print(" ")
    print("Requisito 2: E[X(t)X(t+τ)] == Rxx(τ)")
    print(" ")

    print("Se procede a realizar 2 pruebas con τ = 3 horas. ")
    print(" ")

    # Prueba 1 con τ = 3 horas
    print("Prueba 1: t1 = '04:00:00' y t2 = '07:00:00' ")
    print(" ")

    # Definición de tiempo con diferencia entre ellos de 3 horas
    t1 = '04:00:00'
    t2 = '07:00:00'

    # Se obtiene autocorrelación Rxx(t1, t2)
    Rxx_1 = momentos.autocorrelacion(M[0], t1, t2, variable)

    print('Correlación prueba 1 es: ', Rxx_1)
    print(" ")

    # Prueba 2 con τ = 3 horas
    print("Prueba 2:  t1 = '13:00:00' y t2 = '16:00:00' ")
    print(" ")

    # Definición de tiempo con diferencia entre ellos de 3 horas
    t1 = '13:00:00'
    t2 = '16:00:00'

    # Se obtiene autocorrelación Rxx(t1, t2)
    Rxx_2 = momentos.autocorrelacion(M[0], t1, t2, variable)
    print('Correlación prueba 2 es: ', Rxx_2)
    print(" ")

    # Tolerancia al 5%
    tolerancia = 0.05

    # El método math.isclose() verifica si dos valores son
    # cercanos el uno al otro, o no.
    # Retorna True si los valores son cercanos, de los contrario retorna falso.
    if math.isclose(Rxx_1, Rxx_2, rel_tol=tolerancia):
        print(f"{Rxx_1} y {Rxx_2} se encuentran dentro de la tolerancia 5% ")
        print('Requisito 2 se cumple')
        print(" ")
    else:
        print(
            f"{Rxx_1} y {Rxx_2} no se encuentran dentro de la tolerancia 5% ")
        print('Requisito 2 no se cumple')
        print(" ")

    return PROMEDIO


def prom_temporal(variable, loc, inicio, fin):
    """Calcula el promedio temporal A[m(t)].

    Esta función, permite calcular y hallar el promedio temporal
    para una muestra de P(t).Es capaz de encontrar la media temporal
    A[m(t)] para una función muestra m(t) de la secuencia aleatoria M(t).

    Parameters
    ----------
    variable : str
        Opciones "so2", "no2", "co", "o3", "pm10", "pm2.5".
    loc : int
        Opciones desde 102 hasta 125
    inicio : int
        Fecha de inicio, ejemplo, 2020031400
    fin : int
        Fecha de fin, ejemplo, 2020031723

    Returns
    -------
    m : float
        Es el valor promedio de una muestra.
    """
    # Llamada a función muestra()
    m = proceso.muestra(variable, loc, inicio, fin)
    # Se calcula el promedio de las muestras extraídas
    m = float(m['o3'].mean())
    print('A[m(t)] = ', m)
    print(' ')

    return m


def ergodicidad(M, m):
    """Esta función determina si la secuencia aleatoria M(t) es ergódica.

    Recibe como parámetros M y m, donde M es la matriz del
    conjunto de funciones muestra que conforman el proceso
    aleatorio y m, es una única función muestra de ese proceso
    aleatorio.

    Parameters
    ----------
    M : float
        Promedio del conjunto de muestras M(t).
    m : float
        Promedio de una muestras m(t).

    Returns
    -------
    "Aquí está la ergodicidad." : str
        Respuesta si es ergódica o no.
    """
    # Se disminuye la cantidad decimales
    M = round(M, 5)
    m = round(m, 5)
    # Se establece tolerancia del 5%
    tolerancia = 0.05

    print('Prueba ergodicidad:')
    print('E[M(t)] = ', M)
    print('E[m(t)] = ', m)

    # El método math.isclose() verifica si dos valores son
    # cercanos el uno al otro, o no.
    # Retorna True si los valores son cercanos, de los contrario retorna falso.
    if math.isclose(m, M, rel_tol=tolerancia):
        print(f"m: {m} y M: {M} se encuentran dentro de la tolerancia 5% ")
        print('Ergodicidad se cumple.')
        print(" ")
    else:
        print(f"m: {m} y M: {M} no se encuentran dentro de la tolerancia 5% ")
        print('Ergodicidad no se cumple.')
        print(" ")

    return "Aquí está la ergodicidad."
