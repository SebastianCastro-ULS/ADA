# Análisis Exploratorio de Datos de Red Social a Gran Escala

## Descripción General

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre una red social simulada a gran escala, utilizando un conjunto de datos que contiene 10 millones de ubicaciones geográficas y listas de adyacencia de usuarios.

El sistema está diseñado con énfasis en **eficiencia**, **uso optimizado de memoria**, **procesamiento en lote y streaming**, y una arquitectura **modular** que permite realizar EDA de manera clara y reproducible.

---

## Estructura del Proyecto

```
.
├── main.py              # Script principal que orquesta la carga y el EDA
├── loader.py            # Módulo de carga optimizada de datos
├── eda.py               # Módulo de análisis exploratorio (estadísticas, visualización, outliers)
├── utils.py             # Utilidades generales (uso de memoria, logs, validaciones)
├── 10_million_location.txt   # Archivo de ubicaciones (lat, long)
├── 10_million_user.txt       # Archivo de listas de adyacencia
├── README.md            # Documentación del proyecto
```

---

## Instrucciones de Uso

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar el análisis:
```bash
python main.py
```

3. Los resultados visuales se guardarán automáticamente en la carpeta `output/`.

---

## Flujo de Análisis

1. **Carga eficiente de datos**
   - Se usa `Polars` para cargas rápidas con validación de estructura.
   - Se manejan archivos grandes usando `streaming` y `procesamiento por lotes` para minimizar el uso de memoria.

2. **EDA sobre datos geográficos (`10_million_location.txt`)**
   - Estadísticas básicas: media, mediana, desviación estándar de latitud y longitud.
   - Visualizaciones:
     - Histogramas de distribución geográfica
     - Gráfico de dispersión de coordenadas
   - Detección de outliers mediante IQR (Interquartile Range)
   - Identificación de regiones más densas y patrones de dispersión

3. **EDA sobre listas de adyacencia (`10_million_user.txt`)**
   - Estadísticas de conectividad por usuario: número de amigos, grado promedio, grado máximo/mínimo.
   - Visualización del grado de conexión por usuario
   - Detección de usuarios outliers con conexiones atípicamente altas o bajas

---

## Hallazgos del EDA

- **Ubicación:**
  - La mayoría de las ubicaciones están agrupadas en un rango geográfico definido (concentración alta cerca de ciertos valores de latitud/longitud).
  - Algunos valores extremos fueron detectados y eliminados como outliers.
  - La dispersión geográfica sugiere múltiples clústeres regionales.

- **Red de Usuarios:**
  - El grado promedio de conexión es moderado (~5-10), pero algunos usuarios alcanzan cientos de conexiones (posibles hubs).
  - Se detectaron usuarios sin conexiones, lo cual podría indicar nodos aislados o datos erróneos.
  - La red podría estar formada por múltiples comunidades densas.

---

## Validación y Manejo de Recursos

- Uso de `psutil` para medir el consumo de memoria en tiempo real.
- Captura y logueo de excepciones para evitar caídas durante el análisis.
- Procesamiento robusto que maneja errores en formatos o estructura de datos.
- Visualizaciones y estadísticas generadas sin bloquear el sistema.

---

## Autores

- **Sebastian Adriano Castro Mamani**
- **Piero Adrian Delgado Chipana**

---
