# Proyecto Integrador - Minería de Datos 1

**Curso:** Minería de Datos 1 - Tarde  
**Integrante:** Maria Eugenia Rocha  
**Fecha:** 28 de junio de 2026  

---

## Información general

Este repositorio contiene el desarrollo completo del Proyecto Integrador de la asignatura Minería de Datos 1. El trabajo consiste en un análisis de datos reproducible y comunicable sobre un dataset de usuarios de una plataforma de streaming. Se aplican técnicas de inspección, limpieza, análisis exploratorio (EDA), escalamiento y reducción de dimensionalidad (PCA), y se comunican los resultados mediante una aplicación interactiva en Streamlit y un informe breve en PDF.

## Objetivo del proyecto

Aplicar los contenidos de la materia para construir un proyecto de análisis de datos con decisiones justificadas, trazabilidad del proceso y comunicación clara de los resultados. Se busca comprender la estructura y calidad del dataset, preparar los datos con evidencia observada, realizar análisis univariado, bivariado y multivariado, aplicar escalamiento y PCA, y comunicar los hallazgos mediante una aplicación pública y un informe final.

## Dataset

El dataset utilizado es `streaming_users_dirty.json`, que contiene 8160 registros de usuarios de una plataforma de streaming. Cada fila representa un usuario con las siguientes variables: identificador (`user_id`), edad (`age`), plan de suscripción (`subscription_plan`), tiempo de visualización mensual en minutos (`monthly_watch_time_mins`), país (`country`), género favorito (`favorite_genre`), fecha del último inicio de sesión (`last_login_date`) y cantidad de tickets de soporte (`customer_support_tickets`). El dataset presenta problemas de calidad como valores faltantes, duplicados, valores atípicos e inconsistencias en categorías, que son abordados en la etapa de limpieza. El dataset procesado final contiene 7064 registros y está disponible en `data/processed/streaming_users_clean.csv`.

## Estructura del repositorio
PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/
│ ├── raw/
│ │ └── streaming_users_dirty.json
│ └── processed/
│ └── streaming_users_clean.csv
├── notebooks/
│ ├── 01_inspeccion_inicial.ipynb
│ ├── 02_calidad_y_limpieza.ipynb
│ ├── 03_eda.ipynb
│ ├── 04_pca.ipynb
│ └── 05_conclusiones.ipynb
├── app/
│ ├── Home.py
│ └── pages/
│ ├── 01_Dataset.py
│ ├── 02_EDA.py
│ ├── 03_PCA.py
│ └── 04_Conclusiones.py
├── reports/
│ └── informe_final.pdf
└── logs/
└── pipeline_log.csv

## Preparación y calidad de datos

La limpieza se documenta en el notebook `02_calidad_y_limpieza.ipynb` y se registra en `logs/pipeline_log.csv`. Se eliminaron 126 filas completamente duplicadas y 34 duplicados por `user_id`. Se normalizaron las variables categóricas (`subscription_plan`, `country`, `favorite_genre`) para unificar variantes de escritura. Se imputaron los valores nulos de `favorite_genre` con la moda y los de `monthly_watch_time_mins` con la mediana. Se eliminaron valores imposibles en `age`, `monthly_watch_time_mins` y `customer_support_tickets`. Se aplicó winsorización a outliers extremos de estas dos últimas variables. Se limpió `last_login_date` convirtiendo a tipo fecha y descartando registros con fechas no parseables o futuras. El dataset final pasó de 8160 a 7064 filas (retención del 86.6%), sin valores nulos y con tipos de datos consistentes.

## Resumen del análisis exploratorio

El EDA, desarrollado en `03_eda.ipynb`, responde a cinco preguntas de análisis. La distribución de edad es simétrica, sin franja etaria dominante (media ~33 años). El tiempo de visualización mensual presenta asimetría positiva, con un usuario típico consumiendo alrededor de 758 minutos (mediana). El plan de suscripción está fuertemente asociado al consumo: Premium > Estándar > Básico, con diferencias de hasta 500 minutos entre planes. No existe relación lineal entre edad y tickets de soporte (r ≈ 0.005). El patrón de consumo por plan es consistente en todos los países, con poca variación geográfica dentro de cada plan. Estos hallazgos se visualizan con histogramas, boxplots, scatter plots y heatmaps, todos acompañados de interpretaciones vinculadas a los objetivos del proyecto.

## Reducción de dimensionalidad

El PCA, aplicado en `04_pca.ipynb`, se realizó sobre las variables numéricas `age`, `monthly_watch_time_mins` y `customer_support_tickets`, previa estandarización con StandardScaler. La varianza se distribuye casi uniformemente entre los tres componentes (PC1: 33.6%, PC2: 33.3%, PC3: 33.1%), lo que indica que no se logra una reducción dimensional significativa; se necesitan las tres componentes para superar el 80% de varianza acumulada. Los loadings muestran que cada componente está dominado por una variable distinta, confirmando la independencia entre ellas. El biplot revela una separación parcial de los usuarios por plan de suscripción en el eje PC1, pero con considerable superposición.

## Visualización interactiva

La aplicación Streamlit, disponible en [enlace a Streamlit Cloud](https://tu-app.streamlit.app), permite explorar los resultados de forma interactiva. Incluye páginas para el dataset y su calidad, el EDA con visualizaciones dinámicas, el análisis de PCA y las conclusiones finales. La aplicación está diseñada para público general y complementa la evidencia técnica de los notebooks y el informe.

## Cómo ejecutar localmente

1. Clonar el repositorio y navegar a la carpeta raíz.
2. Instalar las dependencias: `pip install -r requirements.txt`.
3. Ejecutar la aplicación: `streamlit run app/Home.py`.
4. La aplicación se abrirá en el navegador en `http://localhost:8501`.

## Conclusiones

El plan de suscripción es el factor más influyente en el consumo mensual, con diferencias significativas y consistentes entre planes y países. La edad no muestra relación con el uso de soporte ni con el consumo, y el PCA confirma la independencia de las variables numéricas. El proceso de limpieza fue riguroso y documentado, aunque la eliminación de registros introduce un posible sesgo. Los resultados sugieren que la plataforma atrae a un público heterogéneo y que el comportamiento de consumo está más ligado al plan elegido que a características demográficas o geográficas. Las limitaciones incluyen la falta de variables contextuales y la imposibilidad de establecer causalidad. Mejoras futuras podrían incorporar datos longitudinales y técnicas de clustering para segmentar usuarios.