import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="🗂️", layout="wide")

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; }
        .info-box {
            background-color: #f7f9fc;
            border-left: 4px solid #5b9bd5;
            padding: 1rem 1.2rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# ── Carga ─────────────────────────────────────────────────────────────────────
@st.cache_data
def cargar_datos():
    return pd.read_csv("data/processed/streaming_users_clean.csv")

df = cargar_datos()

# ── Encabezado ────────────────────────────────────────────────────────────────
st.title("🗂️ Dataset")
st.markdown("---")

# ── Descripción general ───────────────────────────────────────────────────────
st.markdown("## Descripción general")

st.markdown("""
El dataset contiene registros de usuarios de una plataforma de streaming.
Cada fila representa un usuario con información sobre su perfil, comportamiento
de consumo y uso del servicio de soporte.
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Registros originales", "8.160")
col2.metric("Registros tras limpieza", f"{len(df):,}".replace(",", "."))
col3.metric("Variables", str(df.shape[1]))
col4.metric("Retención", "86,6 %")

st.markdown("### Variables del dataset")

variables = {
    "user_id": ("Identificador único de usuario", "Numérica — identificador"),
    "age": ("Edad del usuario en años", "Numérica continua"),
    "subscription_plan": ("Plan de suscripción contratado", "Categórica nominal"),
    "monthly_watch_time_mins": ("Minutos de visualización en el último mes", "Numérica continua"),
    "country": ("País del usuario", "Categórica nominal"),
    "favorite_genre": ("Género de contenido favorito", "Categórica nominal"),
    "last_login_date": ("Fecha del último inicio de sesión", "Fecha"),
    "customer_support_tickets": ("Cantidad de tickets de soporte generados", "Numérica discreta"),
}

tabla_vars = pd.DataFrame(
    [(v, desc, tipo) for v, (desc, tipo) in variables.items()],
    columns=["Variable", "Descripción", "Tipo"]
)
st.dataframe(tabla_vars, use_container_width=True, hide_index=True)

# ── Resumen de calidad ────────────────────────────────────────────────────────
st.markdown("## Resumen del proceso de calidad y limpieza")

st.markdown("""
El proceso de limpieza aplicó 13 pasos sobre el dataset original, registrados en
`logs/pipeline_log.csv`. Los principales problemas detectados y tratados fueron:
""")

problemas = [
    ("Filas duplicadas exactas", "126", "Eliminación (keep=first)"),
    ("Duplicados por user_id", "34 adicionales", "Eliminación (keep=first)"),
    ("Espacios en variables categóricas", "Múltiples columnas", "str.strip()"),
    ("subscription_plan inconsistente", "14 variantes → 3 categorías", "Mapeo explícito"),
    ("country inconsistente", "Múltiples variantes → 7 países", "Mapeo explícito"),
    ("favorite_genre inconsistente + nulos", "Variantes + 240 nulos", "Mapeo + imputación con moda"),
    ("age fuera de rango (< 0 o > 100)", "74 registros", "Eliminación (valores imposibles)"),
    ("monthly_watch_time_mins negativos y centinela 99999", "69 registros", "Eliminación"),
    ("monthly_watch_time_mins outliers extremos", "119 registros", "Winsorización IQR k=3.0"),
    ("monthly_watch_time_mins nulos", "193 registros", "Imputación con mediana"),
    ("customer_support_tickets negativos", "29 registros", "Eliminación"),
    ("customer_support_tickets outliers extremos", "81 registros", "Winsorización IQR k=3.0"),
    ("last_login_date inválidas y futuras", "784 registros", "Eliminación"),
]

tabla_limpieza = pd.DataFrame(
    problemas,
    columns=["Problema detectado", "Registros afectados", "Acción aplicada"]
)
st.dataframe(tabla_limpieza, use_container_width=True, hide_index=True)

# ── Vista previa ──────────────────────────────────────────────────────────────
st.markdown("## Vista previa del dataset procesado")

n = st.slider("Cantidad de filas a mostrar", min_value=5, max_value=50, value=10, step=5)
st.dataframe(df.head(n), use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown(
    "[github.com/EugeRocha/PI_Mineria_Datos_1](https://github.com/EugeRocha/PI_Mineria_Datos_1)"
)
