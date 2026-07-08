import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; }
        h3 { color: #4a6fa5; }
        .interpretacion {
            background-color: #f7f9fc;
            border-left: 4px solid #5b9bd5;
            padding: 0.8rem 1.2rem;
            border-radius: 4px;
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def cargar_datos():
    return pd.read_csv("data/processed/streaming_users_clean.csv")

df = cargar_datos()

st.title("Análisis Exploratorio de Datos")
st.markdown("""
Las visualizaciones responden a las cinco preguntas de análisis definidas al inicio del
proyecto. Cada gráfico incluye una interpretación vinculada a la pregunta correspondiente.
""")
st.markdown("---")

# ── UNIVARIADO ────────────────────────────────────────────────────────────────
st.markdown("## Análisis Univariado")

# Pregunta 1 — age
st.markdown("### Pregunta 1 — ¿Cómo se distribuye la edad de los usuarios?")

media_age = df['age'].mean()
mediana_age = df['age'].median()
std_age = df['age'].std()
skew_age = df['age'].skew()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Media", f"{media_age:.1f} años")
col2.metric("Mediana", f"{mediana_age:.1f} años")
col3.metric("Desvío estándar", f"{std_age:.1f} años")
col4.metric("Asimetría", f"{skew_age:.2f}")

fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df['age'], bins=30, color='#5b9bd5', edgecolor='white', alpha=0.85)
ax.axvline(media_age, color='#c0392b', linestyle='--', linewidth=1.5,
           label=f'Media: {media_age:.1f}')
ax.axvline(mediana_age, color='#e67e22', linestyle='-', linewidth=1.5,
           label=f'Mediana: {mediana_age:.1f}')
ax.set_xlabel('Edad (años)')
ax.set_ylabel('Frecuencia')
ax.set_title('Distribución de edad de los usuarios', fontsize=12, fontweight='bold')
ax.legend()
sns.despine()
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='interpretacion'>
<b>Interpretación:</b> la distribución de edad es aproximadamente simétrica (asimetría = 0.15),
con media y mediana prácticamente coincidentes en torno a los 33 años. No se observa una franja
etaria dominante: los usuarios se distribuyen de forma relativamente uniforme entre los 13 y 55 años,
lo que indica que la plataforma no está concentrada en un segmento de edad particular.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Pregunta 2 — monthly_watch_time_mins
st.markdown("### Pregunta 2 — ¿Cómo se distribuye el tiempo de visualización mensual?")

media_wt = df['monthly_watch_time_mins'].mean()
mediana_wt = df['monthly_watch_time_mins'].median()
std_wt = df['monthly_watch_time_mins'].std()
skew_wt = df['monthly_watch_time_mins'].skew()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Media", f"{media_wt:.0f} min")
col2.metric("Mediana", f"{mediana_wt:.0f} min")
col3.metric("Desvío estándar", f"{std_wt:.0f} min")
col4.metric("Asimetría", f"{skew_wt:.2f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.hist(df['monthly_watch_time_mins'], bins=40, color='#5b9bd5',
         edgecolor='white', alpha=0.85)
ax1.axvline(media_wt, color='#c0392b', linestyle='--', linewidth=1.5,
            label=f'Media: {media_wt:.0f}')
ax1.axvline(mediana_wt, color='#e67e22', linestyle='-', linewidth=1.5,
            label=f'Mediana: {mediana_wt:.0f}')
ax1.set_xlabel('Minutos por mes')
ax1.set_ylabel('Frecuencia')
ax1.set_title('Histograma', fontsize=11, fontweight='bold')
ax1.legend()

ax2.boxplot(df['monthly_watch_time_mins'], patch_artist=True,
            boxprops=dict(facecolor='#5b9bd5', alpha=0.6))
ax2.set_ylabel('Minutos por mes')
ax2.set_title('Boxplot', fontsize=11, fontweight='bold')
ax2.set_xticks([])

sns.despine()
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='interpretacion'>
<b>Interpretación:</b> la distribución presenta asimetría positiva (skew = 1.25): la mayoría
de los usuarios consume entre 400 y 1200 minutos mensuales, con una minoría que concentra
valores más altos. La brecha entre media (787 min) y mediana (759 min) confirma que la media
está siendo arrastrada hacia arriba por esos valores altos. El usuario típico consume
aproximadamente 759 minutos mensuales (~12.6 horas).
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── BIVARIADO ─────────────────────────────────────────────────────────────────
st.markdown("## Análisis Bivariado")

# Pregunta 3 — watch_time por plan
st.markdown("### Pregunta 3 — ¿El tiempo de visualización varía según el plan de suscripción?")

orden_plan = ['Básico', 'Estándar', 'Premium']
stats_plan = df.groupby('subscription_plan')['monthly_watch_time_mins'].agg(
    ['mean', 'median']
).round(1).reindex(orden_plan)
stats_plan.columns = ['Media (min)', 'Mediana (min)']
st.dataframe(stats_plan, use_container_width=False)

colores = ['#5b9bd5', '#ed7d31', '#70ad47']
fig, ax = plt.subplots(figsize=(8, 4))
grupos = [df[df['subscription_plan'] == p]['monthly_watch_time_mins'].values
          for p in orden_plan]
bp = ax.boxplot(grupos, labels=orden_plan, patch_artist=True)
for patch, color in zip(bp['boxes'], colores):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax.set_xlabel('Plan de suscripción')
ax.set_ylabel('Minutos por mes')
ax.set_title('Tiempo de visualización por plan', fontsize=12, fontweight='bold')
sns.despine()
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='interpretacion'>
<b>Interpretación:</b> existe una diferencia clara y consistente entre planes: los usuarios
Premium consumen en promedio 1091 min/mes, casi el doble que los de plan Básico (593 min/mes).
Los boxplots confirman que esta diferencia no es producto de valores extremos: las cajas apenas
se superponen, lo que indica una separación robusta entre grupos. El plan de suscripción está
fuertemente asociado al nivel de consumo.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Pregunta 4 — age vs tickets
st.markdown("### Pregunta 4 — ¿Existe relación entre la edad y los tickets de soporte?")

r = df['age'].corr(df['customer_support_tickets'])
st.metric("Correlación de Pearson (r)", f"{r:.4f}")

fig, ax = plt.subplots(figsize=(9, 4))

# Muestra para no saturar el gráfico
muestra = df.sample(n=1000, random_state=42)
ax.scatter(muestra['age'], muestra['customer_support_tickets'],
           alpha=0.3, color='#5b9bd5', s=15)

m, b = np.polyfit(df['age'], df['customer_support_tickets'], 1)
x_range = np.linspace(df['age'].min(), df['age'].max(), 100)
ax.plot(x_range, m * x_range + b, color='#c0392b', linewidth=2,
        label=f'Tendencia (r = {r:.4f})')

ax.set_xlabel('Edad (años)')
ax.set_ylabel('Tickets de soporte')
ax.set_title('Edad vs. tickets de soporte', fontsize=12, fontweight='bold')
ax.legend()
sns.despine()
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='interpretacion'>
<b>Interpretación:</b> el coeficiente de Pearson r = 0.0054 es prácticamente cero, lo que
indica que no existe relación lineal entre la edad y la cantidad de tickets de soporte.
La línea de tendencia es casi horizontal y los puntos se distribuyen de forma uniforme
en todo el rango de edades. Este resultado descarta hipótesis como "los usuarios mayores
generan más tickets" o "los más jóvenes usan más el soporte".
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ── MULTIVARIADO ──────────────────────────────────────────────────────────────
st.markdown("## Análisis Multivariado")

st.markdown("### Pregunta 5 — ¿El perfil de consumo por plan es consistente entre países?")

pivot = df.pivot_table(
    values='monthly_watch_time_mins',
    index='country',
    columns='subscription_plan',
    aggfunc='mean'
)[orden_plan].round(1)

# Filtro interactivo por país
paises = sorted(df['country'].unique())
seleccion = st.multiselect(
    "Filtrar países",
    options=paises,
    default=paises
)

if seleccion:
    pivot_filtrado = pivot.loc[pivot.index.isin(seleccion)]
else:
    pivot_filtrado = pivot

fig, ax = plt.subplots(figsize=(9, max(3, len(pivot_filtrado) * 0.6 + 1)))
sns.heatmap(
    pivot_filtrado,
    annot=True,
    fmt='.0f',
    cmap='Blues',
    linewidths=0.5,
    ax=ax,
    cbar_kws={'label': 'Minutos promedio / mes'}
)
ax.set_title('Promedio de tiempo de visualización por país y plan',
             fontsize=12, fontweight='bold')
ax.set_xlabel('Plan de suscripción')
ax.set_ylabel('País')
plt.tight_layout()
st.pyplot(fig)
plt.close()

st.markdown("""
<div class='interpretacion'>
<b>Interpretación:</b> la jerarquía Premium > Estándar > Básico se mantiene sin excepciones
en todos los países del dataset. La variación entre países dentro de cada plan es menor al 10%,
mientras que la diferencia entre planes dentro de un mismo país es de casi el doble entre
Básico y Premium. El plan de suscripción es el factor dominante en el nivel de consumo,
independientemente de la ubicación geográfica del usuario.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "📁 [github.com/EugeRocha/PI_Mineria_Datos_1](https://github.com/EugeRocha/PI_Mineria_Datos_1)"
)
