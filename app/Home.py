import streamlit as st

st.set_page_config(
    page_title="Análisis de Usuarios de Streaming",
    page_icon="📊",
    layout="wide"
)

# ── Estilos ───────────────────────────────────────────────────────────────────
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

# ── Encabezado ────────────────────────────────────────────────────────────────
st.title("Análisis de Usuarios de una Plataforma de Streaming")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='info-box'>
    <b>Proyecto Integrador — Minería de Datos 1</b><br>
    Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial<br>
    ITSE — Santiago del Estero
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='info-box'>
    <b>Integrante:</b> Rocha, María Eugenia<br>
    <b>Comisión:</b> Tarde — 2026<br>
    <b>Fecha:</b> 7 de Julio 2026
    </div>
    """, unsafe_allow_html=True)

# ── Contexto ──────────────────────────────────────────────────────────────────
st.markdown("## Contexto del proyecto")

st.markdown("""
Este proyecto analiza un dataset de usuarios de una plataforma de streaming
con el objetivo de comprender el comportamiento de consumo según el plan de suscripción,
la distribución etaria y la relación entre variables de uso.

El análisis cubre las etapas de inspección inicial, limpieza y preparación de datos,
exploración univariada, bivariada y multivariada, y reducción de dimensionalidad mediante PCA.
""")

st.markdown("## Preguntas de análisis")

preguntas = [
    ("Univariado", "¿Cómo se distribuye la edad de los usuarios?"),
    ("Univariado", "¿Cómo se distribuye el tiempo de visualización mensual?"),
    ("Bivariado", "¿El tiempo de visualización varía según el plan de suscripción?"),
    ("Bivariado", "¿Existe relación entre la edad y la cantidad de tickets de soporte?"),
    ("Multivariado", "¿El perfil de consumo por plan es consistente entre países?"),
]

for tipo, pregunta in preguntas:
    st.markdown(f"- **{tipo}:** {pregunta}")

# ── Navegación ────────────────────────────────────────────────────────────────
st.markdown("## Navegación")

st.markdown("""
Usá el menú de la izquierda para navegar entre las secciones:

- **Dataset** — descripción del dataset y resumen del proceso de limpieza
- **EDA** — análisis exploratorio con visualizaciones interactivas
- **PCA** — análisis de componentes principales
- **Conclusiones** — hallazgos, limitaciones y próximos pasos
""")

# ── Enlace al repo ────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "Repositorio: "
    "[github.com/EugeRocha/PI_Mineria_Datos_1](https://github.com/EugeRocha/PI_Mineria_Datos_1)"
)
