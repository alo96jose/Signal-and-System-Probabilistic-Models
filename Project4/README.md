### Universidad de Costa Rica
#### IE0405 - Modelos Probabilísticos de Señales y Sistemas
##### Proyecto 4: Procesos aleatorios (Primer ciclo del 2023)

- Denisse Ugalde Rivera, C07893
- Isabel Sabater Aguilar, B97037
- Alonso José Jiménez Anchía, B63561

# Paquete `proceso`

> Este es un paquete que utiliza herramientas probabilísticas convertidas en funciones para analizar un conjunto de datos, los cuales se consideran un proceso aleatorio en sí. De este proceso aleatorio, con este paquete se pueden extraer muestras. El paquete se divide en 3 módulos: estacionaridad, proceso y momentos. Cada módulo tiene distintas funciones, las cuales se utilizan incluso entre módulos. Los objetivos de las funciones es analizar tanto las muestras como el proceso aleatorio y aplicarle la teoría probabilística.
> 
## Funciones

Módulo de procesos: proporciona funciones para el procesamiento y visualización de datos.
### Función `Muestra:`
    Visualiza los datos filtrados por variable ubicación y rango de fechas.
    

    Parameters
    ----------
    variable : str
        Es el nombre de la variable que se desea filtrar y mostrar en la matriz resultante.
    loc : int
        Ubicación (localización) que se utilizará para filtrar los datos.
    inicio : int
        Fecha y hora de inicio del rango de fechas que se utilizará para filtrar los datos.
    fin : int
        Fecha y hora de fin del rango de fechas que se utilizará para filtrar los datos.

    df_filtrado_loc: list 
        Es un DataFrame que contiene los datos filtrados por la ubicación loc.
    
    df_filtrado_fecha: list
        Es un DataFrame que contiene los datos filtrados por el rango de fechas especificado.

    df_filtrado: list 
        Es la combinación de los DataFrame df_filtrado_loc y df_filtrado_fecha.
    
    matriz: list 
        Es un DataFrame que contiene las columnas seleccionadas (loc, dt, variable) y tiene un nuevo índice. Se utiliza para mostrar la matriz resultante por pantalla y se devuelve al final de la función.
    
    Returns
    -------


### Función Proceso: 
    Realiza el proceso de muestras para un intervalo de tiempo y variable dada.

    Parameters
    ----------

    intervalo: int
        Es el intervalo de tiempo que se utilizará para generar las muestras. Puede ser "semanal" o "diario".

    intervalo_inicio: int 
        Es la fecha y hora de inicio del intervalo de tiempo actual.
    
    intervalo_fin: int
        Es la fecha y hora de fin del intervalo de tiempo actual.
    
    funciones_muestra: list 
        Es una lista que almacena las funciones muestra generadas para cada intervalo de tiempo dentro del rango especificado. Esta lista se devuelve al final de la función.
    
    Returns
    -------

### Función Gráfica: 
    Genera una gráfica de la variable para la ubicación y el rango de fechas dados.

    matriz: list 
        Es el DataFrame resultante de la función muestra con los datos filtrados. Se utiliza para generar la gráfica.
    
    Returns
    -------

### Para la función `autocorrelacion()`:
    Función calcula el valor de la autocorrelación.

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

### Para la función `autocovarianza()`:
    Función calcula el valor de la autocovarianza.

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

###  Para la función `wss()`: 
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
        
###  Para la función `prom_temporal():`:
    Calcula el promedio temporal A[m(t)].

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
        
###  Para la función `ergodicidad():`:
    Esta función determina si la secuencia aleatoria M(t) es ergódica.

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


## Resultados

- Módulo de proceso
El proyecto está diseñado para el procesamiento y visualización de datos. Las funciones proporcionadas permiten filtrar y analizar datos en base a variables, ubicaciones y rangos de fechas específicos.

La función muestra(variable, loc, inicio, fin) recibe una variable, una ubicación y un rango de fechas, y filtra los datos del DataFrame df en base a esos criterios. Luego, muestra por pantalla la matriz resultante y la devuelve. 

La función proceso realiza un proceso de muestras para un intervalo de tiempo y una variable dada. Dependiendo del intervalo especificado ("semanal" o "diario"), genera funciones muestra dentro del intervalo de tiempo especificado y las almacena en una lista.

La función grafica utiliza la función muestra para obtener la matriz de datos filtrados y genera una gráfica de la variable especificada en función de la fecha. La gráfica resultante muestra la evolución de la variable a lo largo del rango de fechas y para la ubicación dada.

- Modulo momentos
La función autocorrelación calcula la autocorrelación a partir de la lista entregada por proceso y dos horas t1 y t2 cualesquiera.

La función autocovarianza calcula la autocovarianza a partir de la lista entregada por proceso y dos horas t1 y t2 cualesquiera.

- Modulo estacionaridad
La función wss(intervalo, variable, loc, inicio, fin) recibe los mismos parámetros de la función proceso porque dentro se necesita llamar a esta última. Esta función el resultado de proceso, lo vuelve una matriz con 24 filas y 1 columna, donde cada fila representa 1 hora y la columna es el conjunto de listas con todas las muestras del proceso aleatorio M(t) en forma de listas. Consecutivamente, esta función buscar comprobar los requisitos siguientes: E[X(t)] = Constante y E[X(t)X(t+τ)] == Rxx(τ). Si ambos se cumple, M(t) es una secuencia estacionaria en sentido amplio.

La función prom_temporal(variable, loc, inicio, fin) recibe como parámetros los mismos que los que recibe la función muestra porque esta última se llama dentro para tomar una muestra del proceso aleatorio M(t) y obtener así la media temporal A[m(t)] para una función muestra m(t) de la secuencia aleatoria M(t) definida para el intervalo establecido en las variables inicio y fin.

La función ergodicidad(M, m) recibe como parámetros los resultados de las funciones wss() y prom_temporal(), los compara y si estos varían dentro del rango de 5% entonces el proceso se comprueba la ergodicidad de la secuencia aleatorio M(t).

# Paquete `proceso`

> Contiene funciones para calcular la autocorrelación y la autocovarianza.








