# 📊 Análisis Exploratorio: Cobertura Neta y Tasa de Matriculados

Este repositorio contiene un **notebook/script de Python** y una **aplicación interactiva desarrollada en Streamlit**, desarrollados como parte del curso con el profesor Zainea. El objetivo es analizar el comportamiento de la **cobertura neta** y la **tasa de matriculados** en Colombia, a lo largo del tiempo y del espacio, apoyándonos en consultas avanzadas y visualización de datos.

---

## 🧠 Descripción del Proyecto

El proyecto responde a los requerimientos planteados en clase, con foco en:

- La **limpieza rigurosa de los datos**, incluyendo la estandarización de nombres de departamentos y municipios.
- El uso de **consultas avanzadas** tipo SQL, incluyendo:
  - `JOIN` para integrar diferentes fuentes.
  - `CTE` para estructurar consultas complejas.
  - Funciones de ventana para análisis a nivel de fila dentro de grupos.
- La construcción de un **modelo de datos limpio y reproducible** en Python.
- El desarrollo de una **App en Streamlit** clara, funcional y autocontenida.

---

## 🧹 Limpieza y Preprocesamiento

Se llevó a cabo un proceso de limpieza de datos con énfasis en:

- Corrección de nombres inconsistentes en departamentos y municipios.
- Conversión de formatos de fecha y tipos de datos.
- Validación y transformación de columnas relevantes para los análisis.

---

## 📈 Análisis Realizados

La app y el script incluyen análisis como:

- Evolución temporal de la **cobertura neta** por región y nivel educativo.
- Comportamiento de la **tasa de matriculados** por municipio.
- Comparaciones interdepartamentales utilizando funciones de ventana.
- Identificación de patrones y anomalías usando promedios móviles y percentiles.

---

## 🌐 App en Streamlit

La aplicación permite:

- Navegar visualmente los indicadores a lo largo del tiempo y el territorio.
- Ajustar filtros por año, nivel educativo, región o municipio.
- Integrar fuentes externas secundarias (como datos del DANE o Ministerio de Educación).
- Ver gráficos con escalas de color adecuadas, mapas interactivos y tablas resumen.

Ejecuta la app con:

```bash
poetry run streamlit run app.py
