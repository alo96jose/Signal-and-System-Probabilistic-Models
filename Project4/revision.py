"""Programa que llama a las funciones del paquete proceso.

Se trata de un programa que contiene las llamadas a las
funciones: muestra, proceso, grafica, autocorrelacion,
autocovarianza, wss, prom_temporal y ergodicidad.
"""

from proceso import proceso, momentos, estacionaridad
import pandas as pd

# SECCIÓN A: Función de densidad de probabilidad

# 0. Lectura de datos
df = pd.read_csv('seoul.csv')
df['dt'] = pd.to_datetime(df['dt'], format='%Y%m%d%H')
df.set_index(['dt', 'loc'], inplace=True)

variable = input('Ingrese el nombre de la columna a analizar, ej:o3: ')
t1 = input('Ingrese el nombre de la hora1 a analizar, ej:00:00:00: ')
t2 = input('Ingrese el nombre de la hora2 a analizar, ej:23:00:00: ')
intervalo = input('Ingrese el intervalo a analizar, ya sea semanal o '
                  'diario: ')
loc = int(input('Ingrese el número de loc, ej:113: '))
inicio = int(input('Ingrese la fecha de inicio, ej:2020031400: '))
fin = int(input('Ingrese la fecha de fin, ej:2020031723: '))

# 1. Obtención de la muestra
A1 = proceso.muestra(variable=variable, loc=loc, inicio=inicio, fin=fin)
print('Resultados Muestra:')
print(A1)

# 2. Obtención del proceso
A2 = proceso.proceso(intervalo=intervalo, variable=variable, loc=loc,
                     inicio=inicio, fin=fin)
print('Resultados Proceso:')
print(A2)

# 3. Gráfica de las funciones muestra
A3 = proceso.grafica(variable, loc, inicio, fin)
print('Resultados Gráfica:')
print(A3)

# SECCIÓN B: Momentos

# 4. Autocorrelación
B4 = momentos.autocorrelacion(A2[0], t1, t2, variable)
print('Resultado Autocorrelación:')
print(B4)

# 5. Autocovarianza
B5 = momentos.autocovarianza(A2[0], t1, t2, variable)
print('Resultado Autocovarianza:')
print(B5)

# SECCIÓN C: Estacionaridad

# 6. Estacionaridad en sentido amplio
C6 = estacionaridad.wss(intervalo, variable, loc, inicio, fin)
print('Resultados wss:')
print(C6)

# 7. Promedio temporal
C7 = estacionaridad.prom_temporal(variable, loc, inicio, fin)
print('Resultados promedio temporal:')
print(C7)

# 8. Ergodicidad
C8 = estacionaridad.ergodicidad(C6, C7)
print('Resultados ergodicidad:')
print(C8)
