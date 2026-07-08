import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; }
        h3 { color: #4a6fa5; }
        .hallazgo {
            background-color: #f7f9fc;
            border-left: 4px solid #70ad47;
            padding: 0.8rem 1.2rem;
            border-radius: 4px;
            margin-bottom: 0.8rem;
        }
        .limitacion {
            background-color: #fdfaf4;
            border-left: 4px solid #ed7d31;
            padding: 0.8rem 1.2rem;
            border-radius: 4px;
            margin-bottom: 0.8rem;
        }
        .mejora {
            background-color: #f4f8fd;
            border-left: 4px solid #5b9bd5;
            padding: 0.8rem 1.2rem;
            border-radius: 4px;
            margin-bottom: 0.8rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Conclusiones")
st.markdown("---")

# ── Hallazgos ─────────────────────────────────────────────────────────────────
st.markdown("## Hallazgos principales")

st.markdown("""
<div class='hallazgo'>
<b>1. El plan de suscripción es el factor dominante en el nivel de consumo.</b><br>
Los usuarios con plan Premium consumen en promedio 1091 minutos mensuales, casi el doble
que los de plan Básico (593 min). Esta diferencia es robusta y consistente en todos los países
del dataset (variación entre países menor al 10% dentro de cada plan).
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hallazgo'>
<b>2. La base de usuarios es heterogénea en términos de edad.</b><br>
La distribución de edad es aproximadamente simétrica, con media y mediana en torno a los
33 años y usuarios distribuidos entre los 13 y 55 años. No existe una franja etaria dominante.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hallazgo'>
<b>3. La edad no está relacionada con el uso del soporte técnico.</b><br>
La correlación de Pearson entre edad y cantidad de tickets de soporte es r = 0.0054,
prácticamente nula. El perfil etario del usuario no predice su comportamiento respecto
al soporte técnico.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hallazgo'>
<b>4. Las variables numéricas son independientes entre sí.</b><br>
El PCA confirmó la baja correlación entre age, monthly_watch_time_mins y
customer_support_tickets: la varianza se distribuye casi uniformemente entre los tres
componentes (33.6%, 33.3%, 33.1%), lo que indica que PCA no logra comprimir la información
sin pérdida significativa. Cada variable aporta una dimensión de información propia.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Limitaciones ──────────────────────────────────────────────────────────────
st.markdown("## Limitaciones")

st.markdown("""
<div class='limitacion'>
<b>Causalidad no verificable.</b><br>
Las asociaciones observadas (especialmente entre plan y consumo) no permiten establecer
relaciones causales con los datos disponibles. No puede determinarse si el plan determina
el consumo o si los usuarios que más consumen tienden a elegir planes superiores.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='limitacion'>
<b>Alcance del dataset.</b><br>
El dataset no incluye variables de contexto como tipo de dispositivo, hora de uso o
historial de contenido, que podrían enriquecer el análisis del perfil de usuario.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='limitacion'>
<b>Sesgo de selección por limpieza.</b><br>
El proceso de limpieza eliminó el 13.4% de los registros originales. Si bien cada
decisión fue justificada con evidencia, los registros eliminados podrían no ser
aleatorios respecto al comportamiento de los usuarios.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='limitacion'>
<b>Independencia entre variables numéricas.</b><br>
La baja correlación entre las tres variables numéricas limitó la capacidad de reducción
de dimensionalidad del PCA. El análisis no pudo resumirse en menos de 3 componentes
sin pérdida importante de información.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Mejoras futuras ───────────────────────────────────────────────────────────
st.markdown("## Próximos pasos")

st.markdown("""
<div class='mejora'>
<b>Segmentación de usuarios mediante clustering.</b><br>
Una mejora futura podría consistir en aplicar técnicas de clustering (como K-Means)
para identificar grupos de usuarios con comportamiento similar, complementando los
hallazgos del EDA con una agrupación basada en múltiples variables simultáneamente.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='mejora'>
<b>Incorporación de variables adicionales.</b><br>
Incorporar variables como tipo de dispositivo, género de contenido más consumido
o frecuencia de acceso permitiría ampliar el alcance del análisis y enriquecer
el perfil de usuario.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='mejora'>
<b>Análisis longitudinal.</b><br>
Contar con múltiples registros por usuario a lo largo del tiempo permitiría analizar
la evolución del consumo y abordar preguntas sobre retención y abandono de la plataforma.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "[github.com/EugeRocha/PI_Mineria_Datos_1](https://github.com/EugeRocha/PI_Mineria_Datos_1)"
)
