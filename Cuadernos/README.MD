# Proyecto DIP_USTA - Análisis de Cobertura Educativa

Este repositorio contiene el desarrollo de un modelo de análisis de datos para estudiar el comportamiento de la **cobertura neta** y la **tasa de matriculados** en Colombia a lo largo del tiempo y del espacio.

## Estructura del Repositorio

- `cuadernos/`  
  Contiene los notebooks y scripts en Python utilizados para la limpieza y modelado de los datos. Incluye el procesamiento de variables como nombres inconsistentes de **departamentos** y **municipios**, y la consolidación de fuentes de información.

- `streamlit_app/`  
  Aplicación desarrollada en **Streamlit**, donde se visualizan los análisis del comportamiento de la cobertura neta y la tasa de matrícula. Se integran fuentes secundarias en la medida de lo posible, y se presenta la información de forma **clara**, **autocontenida**, con escalas de color adecuadas y mensajes comprensibles.

- `datos/`  
  Archivos de datos crudos y procesados, listos para su análisis y visualización.

- `utils/`  
  Funciones de apoyo para la carga, transformación y visualización de los datos, reutilizables en diferentes notebooks o scripts.

## Descripción General

- 📊 **Notebook/Script**:  
  Se hace limpieza de datos respondiendo a los requerimientos definidos por el profesor Zainea, abordando problemas como nombres incorrectos en los campos geográficos y consolidación de información.

- 🌐 **App Streamlit**:  
  Herramienta interactiva para explorar los resultados de forma amigable. Presenta:

  - Evolución temporal de indicadores educativos.
  - Comparación espacial entre municipios y departamentos.
  - Uso de escalas de color consistentes.
  - Explicación clara de métricas y resultados.

## Instrucciones para Ejecutar

1. Clona el repositorio.
2. Instala los requerimientos:  
   ```bash
   pip install -r requirements.txt
