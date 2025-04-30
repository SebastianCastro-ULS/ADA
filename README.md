# Análisis Exploratorio de Datos en Redes Sociales (10M registros)

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre un conjunto masivo de datos que representa:

- **Ubicaciones geográficas** de 10 millones de usuarios.
- **Listas de adyacencia** representando conexiones de red social entre usuarios.

Está diseñado para ser **rápido**, **eficiente en memoria**, y fácil de escalar, haciendo uso de **Polars**, procesamiento por lotes y visualizaciones automáticas.

---

## Estructura del Proyecto

```
proyecto_eda/
│
├── main.py              # Script principal
├── loader.py            # Carga eficiente y validada de datos
├── eda.py               # Análisis exploratorio (EDA)
├── utils.py             # Funciones auxiliares
├── requirements.txt     # Dependencias del proyecto
├── lat_hist.png         # Visualización de latitudes
├── long_hist.png        # Visualización de longitudes
└── user_neighbors_hist.png # Visualización de conexiones
```

---

## Instrucciones de uso

### 1. Requisitos

Asegúrate de tener Python 3.10+ instalado.

Instala las dependencias:

```bash
pip install -r requirements.txt
```

### 2. Archivos esperados

Coloca estos archivos en el directorio raíz:

- `10_million_location.txt`: archivo con 10M de líneas (`lat long`)
- `10_million_user.txt`: archivo con 10M de listas de adyacencia (separadas por espacio)

### 3. Ejecutar análisis

```bash
python main.py
```

Se generarán archivos `.png` con histogramas y se mostrará información estadística y detección de outliers por consola.

---

## Flujo del Proyecto

1. **Carga de Datos (`loader.py`)**:
   - Se valida la existencia de los archivos.
   - Se usa `Polars` para cargar grandes volúmenes eficientemente.
   - Se limpian y tipifican columnas.

2. **Análisis (`eda.py`)**:
   - Se generan estadísticas descriptivas (`mean`, `std`, `min`, `max`, `quartiles`).
   - Se visualiza la distribución de latitudes, longitudes y cantidad de vecinos por usuario.
   - Se detectan outliers usando el método de rango intercuartílico (IQR).

3. **Utilidades (`utils.py`)**:
   - Función de detección de outliers.
   - Preparado para ampliar más métricas.

---

## Hallazgos del EDA

### Ubicación (lat, long)
- **Distribución de latitudes y longitudes** muestra una posible concentración geográfica (por ejemplo, una región como América del Norte).
- **Outliers detectados** en coordenadas que se salen de los rangos típicos de latitudes [-90, 90] y longitudes [-180, 180].

### Red de usuarios
- La mayoría de usuarios tiene entre 10 y 100 vecinos.
- Se detectaron usuarios con más de 1000 vecinos, lo cual puede representar:
  - Influencers o hubs.
  - Datos erróneos o duplicados.
- **Distribución sesgada** a la derecha, como es común en redes reales (ley de potencias).

---

## Consideraciones de rendimiento

- El uso de **Polars** reduce el uso de memoria y el tiempo de carga comparado con Pandas.
- El análisis está preparado para extenderse a grafos reales (por ejemplo, NetworkX o GraphFrames si es necesario).
- Funciona bien con +10 millones de filas y podría escalar más mediante particionado o procesamiento en stream.

---
