# 📊 Análisis y Limpieza de Datos con Python y SQL

Este proyecto responde a los requerimientos planteados por el profesor **Zainea**, y tiene como objetivo realizar un análisis riguroso de los datos disponibles mediante un enfoque híbrido: limpieza y modelamiento con Python, y consultas analíticas avanzadas con SQL.

---

## 🧪 Objetivo General

Desarrollar un **Notebook o Script en Python** que:
- Cargue los datos desde su origen.
- Efectúe la limpieza pertinente (como la normalización de nombres de departamentos y municipios).
- Modele adecuadamente los datos para su análisis.
- Integre principios avanzados de SQL para obtener información clave.

---

## 🧼 Limpieza de Datos

Durante esta etapa se aplicaron transformaciones esenciales como:
- Corrección ortográfica y estandarización de nombres de **departamentos** y **municipios**.
- Conversión de tipos de datos.
- Eliminación de duplicados.
- Gestión de valores faltantes.

---

## 🗃️ Modelo de Datos

El modelo de datos se estructura con entidades clave como:

- `Personas`
- `Departamentos`
- `Municipios`
- `Indicadores` u otras tablas requeridas para el análisis.

La relación entre estas entidades fue implementada para facilitar su uso en entornos analíticos.

---

## 🔍 Consultas Avanzadas: Donde Ocurre la Magia del Análisis

Una vez limpio el dataset, se diseñaron consultas SQL avanzadas para profundizar el análisis. Estas incluyen:

### 🔗 `JOIN`
Utilizados para combinar los universos de `Empleados`, `Departamentos` y otros, permitiendo una visión relacional integrada.

### 🧱 `CTE (Common Table Expressions)`
Estructura utilizada para descomponer problemas complejos en partes simples y legibles. Facilita el desarrollo incremental de consultas complejas evitando subconsultas anidadas.

```sql
WITH DepartamentosLimpios AS (
  SELECT DISTINCT TRIM(UPPER(nombre)) AS departamento_normalizado
  FROM Departamentos
)
SELECT *
FROM Empleados E
JOIN DepartamentosLimpios D
  ON TRIM(UPPER(E.departamento)) = D.departamento_normalizado;
