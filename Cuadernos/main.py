
import streamlit as st
from carga import show_data_tab
from transformacion import show_transform_tab
from mapa import show_map_tab

st.set_page_config(page_title="Modelo Educativo USTA", layout="wide")

st.title("📘 Plataforma Educativa - Universidad Santo Tomás")

# Navegación lateral
seccion = st.sidebar.radio("📂 Navegación", ["1. Cargar Datos", "2. Transformación y Métricas", "3. Mapa Interactivo"])

# Mostrar la sección seleccionada
if seccion == "1. Cargar Datos":
    show_data_tab()
elif seccion == "2. Transformación y Métricas":
    show_transform_tab()
elif seccion == "3. Mapa Interactivo":
    show_map_tab()
