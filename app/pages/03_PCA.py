import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="PCA", page_icon="🔍", layout="wide")

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; }
        .info-box {
            background-color: #f7f9fc;
            border-left: 4px solid #5b9bd5;
            padding: 0.8rem 1.2rem;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def cargar_y_calcular():
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    variables = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
    X = df[variables]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)
    return df, X_pca, pca, variables

df, X_pca, pca, variables = cargar_y_calcular()

st.title("Análisis de Componentes Principales (PCA)")
st.markdown("---")

# ── Variables y escalamiento ──────────────────────────────────────────────────
st.markdown("## Variables utilizadas y escalamiento")

st.markdown("""
PCA opera exclusivamente sobre variables numéricas. Se seleccionaron las tres variables
numéricas disponibles en el dataset procesado:
""")

tabla_vars = pd.DataFrame({
    "Variable": variables,
    "Descripción": [
        "Edad del usuario (años)",
        "Minutos de visualización mensual",
        "Cantidad de tickets de soporte"
    ],
    "Escalamiento aplicado": ["StandardScaler (Z-score)"] * 3
})
st.dataframe(tabla_vars, use_container_width=False, hide_index=True)

st.markdown("""
<div class='info-box'>
<b>¿Por qué escalar?</b> Las tres variables tienen magnitudes muy distintas
(age: 0–100, watch_time: 0–2700, tickets: 0–4). Sin escalamiento, la variable con mayor
magnitud dominaría los componentes independientemente de su relevancia real. StandardScaler
transforma cada variable para que tenga media = 0 y desvío estándar = 1, poniendo todas
en la misma escala.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Varianza explicada ────────────────────────────────────────────────────────
st.markdown("## Varianza explicada")

varianza = pca.explained_variance_ratio_
varianza_acumulada = np.cumsum(varianza)
componentes = [f'PC{i+1}' for i in range(len(varianza))]

col1, col2, col3 = st.columns(3)
col1.metric("PC1", f"{varianza[0]*100:.1f}%", "varianza explicada")
col2.metric("PC2", f"{varianza[1]*100:.1f}%", "varianza explicada")
col3.metric("PC3", f"{varianza[2]*100:.1f}%", "varianza explicada")

# Scree plot
fig, ax1 = plt.subplots(figsize=(7, 4))

ax1.bar(componentes, varianza * 100, color='#5b9bd5', alpha=0.8,
        label='Varianza por componente')
ax1.set_ylabel('Varianza explicada (%)', color='#2c3e50')
ax1.set_ylim(0, 110)

ax2 = ax1.twinx()
ax2.plot(componentes, varianza_acumulada * 100, color='#c0392b',
         marker='o', linewidth=2, markersize=7, label='Varianza acumulada')
ax2.axhline(80, color='#aaaaaa', linestyle='--', linewidth=1, label='Umbral 80%')
ax2.axhline(95, color='#cccccc', linestyle=':', linewidth=1, label='Umbral 95%')
ax2.set_ylabel('Varianza acumulada (%)', color='#c0392b')
ax2.set_ylim(0, 110)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='center right', fontsize=9)
ax1.set_title('Scree Plot — Varianza por componente principal',
              fontsize=11, fontweight='bold')
sns.despine()
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='info-box'>
<b>Interpretación:</b> la varianza se distribuye casi uniformemente entre los tres componentes
(33.6%, 33.3%, 33.1%). Para alcanzar el 80% de varianza acumulada se necesitan los 3 componentes.
Esto indica que PCA no logra reducir dimensionalidad de forma significativa, lo que ocurre cuando
las variables son en gran medida independientes entre sí — resultado coherente con la correlación
prácticamente nula observada en el análisis exploratorio.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── Loadings ──────────────────────────────────────────────────────────────────
st.markdown("## Loadings — contribución de variables a cada componente")

loadings = pd.DataFrame(
    pca.components_.T,
    index=variables,
    columns=componentes
).round(3)

st.dataframe(loadings, use_container_width=False)

fig, ax = plt.subplots(figsize=(7, 3))
sns.heatmap(
    loadings,
    annot=True,
    fmt='.3f',
    cmap='RdBu_r',
    center=0,
    linewidths=0.5,
    ax=ax,
    vmin=-1, vmax=1,
    cbar_kws={'label': 'Loading'}
)
ax.set_title('Heatmap de loadings', fontsize=11, fontweight='bold')
ax.set_xlabel('Componente principal')
ax.set_ylabel('Variable original')
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='info-box'>
<b>Interpretación:</b>
<ul>
<li><b>PC1</b> tiene loadings positivos similares en las tres variables — refleja una intensidad
general de uso, sin variable dominante.</li>
<li><b>PC2</b> opone el consumo de contenido (watch_time: +0.747) a los tickets de soporte
(tickets: -0.664) — usuarios que ven mucho pero generan pocos tickets vs. los que generan
muchos tickets pero consumen menos.</li>
<li><b>PC3</b> está dominado por la edad (age: +0.742) de forma independiente al consumo
y a los tickets.</li>
</ul>
El hecho de que cada componente esté dominado por una variable distinta confirma la independencia
entre ellas.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "[github.com/EugeRocha/PI_Mineria_Datos_1](https://github.com/EugeRocha/PI_Mineria_Datos_1)"
)
