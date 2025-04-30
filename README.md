
# Análisis Exploratorio de Datos - Proyecto

## Descripción

Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre dos grandes conjuntos de datos relacionados con ubicaciones geográficas y usuarios de una red social. Utilizamos dos bibliotecas populares para el manejo de datos en Python: **Pandas** y **Polars**. Este proyecto incluye la carga eficiente de archivos grandes (10 millones de registros), estadísticas descriptivas, visualización de datos, y la detección de outliers.

## Estructura del Proyecto

El proyecto está dividido en los siguientes archivos:

```
├── main.py              # Script principal
├── loader.py            # Carga eficiente y validada de datos
├── eda.py               # Análisis exploratorio (EDA)
├── utils.py             # Funciones auxiliares
├── requirements.txt     # Dependencias del proyecto
```

- **main.py**: Es el script principal que orquesta la carga de datos y el análisis exploratorio.
- **loader.py**: Contiene funciones para cargar los datos de manera eficiente utilizando **Pandas** y **Polars**.
- **eda.py**: Incluye funciones para realizar el análisis exploratorio de los datos, incluyendo visualizaciones y detección de outliers.
- **utils.py**: Proporciona funciones auxiliares como la detección de outliers mediante el método IQR.

## Requisitos

El proyecto depende de las siguientes bibliotecas:

- **Polars**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Numpy**

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Instrucciones de Uso

1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener los archivos de datos `10_million_location.txt` y `10_million_user.txt` en la misma carpeta.
3. Ejecuta el script principal:

```bash
python main.py
```

Esto cargará los datos de ubicación y usuarios, y luego realizará un análisis exploratorio con visualizaciones y estadísticas.

## Comparación de Carga de Datos: Pandas vs Polars

### Carga de Ubicación

- **Pandas**: La carga de datos con Pandas fue exitosa, pero con un tiempo ligeramente mayor debido a la sobrecarga inherente a esta biblioteca cuando se manejan grandes volúmenes de datos.
- **Polars**: Polars, al ser una biblioteca más optimizada para el procesamiento paralelo, mostró tiempos de carga más rápidos y utilizó menos memoria en comparación con Pandas. Sin embargo, hubo problemas al realizar conversiones de tipo y algunas configuraciones de columnas que fueron resueltas en el código.

**Tiempo de carga:**

- **Pandas**: 4.57 segundos
- **Polars**: 2.93 segundos

### Carga de Usuarios

- **Pandas**: En la carga de los usuarios, Pandas también cumplió bien, pero debido a la estructura de los datos, se utilizó más memoria y un tiempo de procesamiento ligeramente más alto.
- **Polars**: Polars resultó ser más eficiente, con tiempos de carga significativamente más bajos.

**Tiempo de carga:**

- **Pandas**: 11.91 segundos
- **Polars**: 0.54 segundos

## Análisis Exploratorio de Datos (EDA)

### Ubicación

**Estadísticas**:  
Se obtuvieron las estadísticas descriptivas de latitudes y longitudes, que nos proporcionan un buen entendimiento de las distribuciones y rangos de los datos. Las latitudes están distribuidas principalmente entre -90 y 90 grados, mientras que las longitudes se distribuyen entre -180 y 180 grados.

**Visualización**:  
Se generaron histogramas para las latitudes y longitudes, mostrando la distribución de los puntos geográficos.

- La distribución de **latitudes** muestra una forma casi uniforme con algunas concentraciones en áreas específicas.
- La distribución de **longitudes** también muestra una distribución más dispersa.

**Detección de Outliers**:  
Se detectaron outliers utilizando el método de rango intercuartílico (IQR), y se identificaron algunas observaciones extremas tanto para latitudes como longitudes. Sin embargo, estos outliers no representaron un problema significativo y se gestionaron adecuadamente.

### Usuarios

**Estadísticas**:  
El análisis de la cantidad de vecinos por usuario reveló que la mayoría de los usuarios tienen un número moderado de vecinos, con algunos usuarios extremadamente conectados. La distribución muestra una cola larga, lo que indica que hay algunos usuarios con conexiones muy altas.

**Visualización**:  
Se generaron histogramas para el número de vecinos por usuario. Se observó que la mayoría de los usuarios tienen entre 10 y 100 vecinos.

**Detección de Outliers**:  
También se detectaron outliers en el número de vecinos, con algunos usuarios mostrando un número de vecinos que podría considerarse inusualmente alto.

## Hallazgos del EDA

- **Distribución de Latitudes y Longitudes**: Las distribuciones son coherentes con lo que se espera de datos geográficos. No se observaron patrones anómalos, lo que indica que los datos de ubicación están bien distribuidos.
- **Usuarios con Vecinos**: La distribución de los vecinos muestra que algunos usuarios tienen una cantidad inusualmente alta de conexiones, lo que podría indicar nodos altamente conectados o comunidades dentro de la red.

## Conclusión

El análisis exploratorio de los datos ha proporcionado una visión general útil tanto de las ubicaciones geográficas como de las conexiones de los usuarios en la red social. Los resultados obtenidos son consistentes con las expectativas, y la implementación ha mostrado ser eficiente en términos de tiempo y uso de memoria, especialmente con **Polars**.

## Integrantes

- **Sebastián Adriano Castro Mamani**
- **Piero Adrian Delgado Chipana**
