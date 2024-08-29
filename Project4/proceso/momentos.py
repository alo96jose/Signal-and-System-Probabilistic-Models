"""
Programa contiene funciones de autocorrelación y autocovarianza.

Se trata de un programa que contiene dos funciones como parte del paquete
proceso.
"""

import pandas as pd
import numpy as np


def autocorrelacion(M, t1, t2, variable):
    """Función calcula el valor de la autocorrelación'.

    Parameters
    ----------
    M : list
        Lista de valores obtenida de proceso.
    t1 : str
        Valor de la hora1 ingresada por el usuario en formato: '23:00:00'.
    t2 : str
        Valor de la hora2 ingresada por el usuario en formato: '23:00:00'.
    variable : str
        Valor del nombre de la columna que se desea analizar.

    Returns
    -------
    float64
        Valor de la autocorrelación.
    """
    # Se configura la columna dt en formato datetime
    M['dt'] = pd.to_datetime(M['dt'], format='%Y%m%d%H')

    # Se extraen los datos correspondientes a la hora t1 para la variable dada
    hora1 = M[M['dt'].dt.time == pd.Timestamp(t1).time()][variable
                                                          ].dropna().tolist()

    # Se extraen los datos correspondientes a la hora t2 para la variable dada
    hora2 = M[M['dt'].dt.time == pd.Timestamp(t2).time()][variable
                                                          ].dropna().tolist()

    # Se calcula el valor de la autocorrelación
    valor_correlacion = np.correlate(hora1, hora2, mode='valid')

    # Se guarda en una variable el valor de la autocorrelacion
    autocorrelacion = valor_correlacion[0]

    # Se devuelve el valor de la autocorrelación
    return autocorrelacion


def autocovarianza(M, t1, t2, variable):
    """Función calcula el valor de la autocovarianza.

    Parameters
    ----------
    M : list
        Lista de valores obtenida de proceso.
    t1 : str
        Valor de la hora1 ingresada por el usuario en formato: '23:00:00'.
    t2 : str
        Valor de la hora2 ingresada por el usuario en formato: '23:00:00'.
    variable : str
        Valor del nombre de la columna que se desea analizar.

    Returns
    -------
    float64
        Valor de la autocovarianza.
    """
    # Se configura la columna dt en formato datetime
    M['dt'] = pd.to_datetime(M['dt'], format='%Y%m%d%H')

    # Se extraen los datos correspondientes a la hora t1 para la variable dada
    hora1 = M[M['dt'].dt.time == pd.Timestamp(t1).time()][variable
                                                          ].dropna().tolist()

    # Se extraen los datos correspondientes a la hora t2 para la variable dada
    hora2 = M[M['dt'].dt.time == pd.Timestamp(t2).time()][variable
                                                          ].dropna().tolist()

    # Se obtiene la matriz para el cálculo de la covarianza
    matrixcov = np.array([hora1, hora2]).T

    # Se calcula la covarianza
    valor_covarianza = np.cov(matrixcov)

    # Se guarda en una variable el valor de la covarianza
    autocovarianza = valor_covarianza[0, 0]

    # Se devuelve el valor de la covarianza
    return autocovarianza
