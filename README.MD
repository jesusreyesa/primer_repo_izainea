# 🧠 Proyecto de Ciencia de Datos

![Banner del Proyecto](https://via.placeholder.com/800x200.png?text=Proyecto+Ciencia+de+Datos)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![pandas](https://img.shields.io/badge/pandas-2.2.3-orange)
![tqdm](https://img.shields.io/badge/tqdm-4.67.0-lightgrey)

## 📌 Descripción

Este proyecto tiene como objetivo analizar información educativa a nivel municipal en Colombia, integrando bases de datos oficiales con fuentes geográficas para facilitar la visualización y el análisis espacial.

---

## 📂 Carga y Preparación de Datos

Se procesaron múltiples fuentes de información, entre ellas la base oficial de **DIVIPOLA**, la cual contiene los códigos únicos para departamentos y municipios. También se trabajó con información geográfica y educativa a nivel territorial.

### 🧭 Inclusión manual de coordenadas: Mapiripana (Guainía)

Durante la depuración de la base geográfica se detectó que el municipio de **Mapiripana (código DIVIPOLA: 94663)** no contaba con coordenadas disponibles.  
Por lo tanto, se incorporaron manualmente las coordenadas a partir de una fuente confiable:

🔗 [municipio.com.co - Mapiripana](https://www.municipio.com.co/municipio-mapiripana.html)

**Coordenadas usadas:**

- 📍 Latitud: `2.617`  
- 📍 Longitud: `-70.533`

Estas coordenadas fueron integradas en la base para permitir su visualización y análisis junto al resto de los municipios.

---

## 📊 Visualización

Se generaron distintos gráficos y mapas con el objetivo de explorar y comunicar los hallazgos de manera efectiva. Algunos ejemplos:

- Mapas de calor por desempeño educativo.
- Gráficos de barras comparativas por grupo o categoría de municipios.
- Mapas interactivos georreferenciados.

---

## 🚀 Tecnologías utilizadas

- **Python 3.10**
- `pandas` para procesamiento de datos
- `tqdm` para seguimiento de procesos
- `matplotlib` y `seaborn` para visualización
- `geopandas` y `folium` para análisis espacial

---

## 📎 Licencia

Este proyecto se encuentra bajo la licencia MIT.
