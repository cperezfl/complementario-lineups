import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="SLR: Éxito de Lineups en Festivales", layout="wide")

# --- NAVEGACIÓN LATERAL ---
try:
    # CORRECCIÓN: use_column_width en lugar de use_container_width
    st.sidebar.image("logo_UTEM.png", use_column_width=True)
except Exception:
    st.sidebar.warning("Imagen 'logo_UTEM.png' no encontrada.")

st.sidebar.title("Navegación")
opciones = [
    "1. Inicio y Problema", 
    "2. Metodología PRISMA", 
    "3. Estado del Arte", 
    "4. Resultados y Visualizaciones", 
    "5. Discusión y Conclusiones"
]
pagina = st.sidebar.radio("Seleccione una sección:", opciones)

# --- PÁGINA 1: INICIO Y PROBLEMA ---
if pagina == "1. Inicio y Problema":
    
    st.markdown("""
    <div style="display:flex; justify-content:center; margin-bottom: 30px;">
        <img src="https://images.unsplash.com/photo-1507874457470-272b3c8d8ee2"
             style="width:100%; max-height:400px; object-fit:cover; border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    </div>
    """, unsafe_allow_html=True)

    st.title("Revisión Sistemática: ¿Qué hace exitoso un lineup?")
    st.subheader("Análisis de la composición de carteles en festivales de música y su influencia en la intención de compra")
    
    st.markdown("---")
    st.markdown("**Autor:** Christian Elías Isaías Pérez Flores")
    st.markdown("**Carrera:** Ingeniería Civil en Ciencia de Datos | Universidad Tecnológica Metropolitana (UTEM), Chile")
    st.markdown("---")

    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.header("Problema de Investigación")
        st.write("""
        La industria de la música en vivo ha consolidado a los festivales masivos como su principal fuente de ingresos. 
        En este escenario de alta incertidumbre y competencia, el núcleo del éxito comercial reside indiscutiblemente en su **lineup** (cartelera de artistas).
        
        Tradicionalmente, las decisiones de contratación se basaban en la intuición de los promotores, creando asimetrías de 
        información y altos riesgos financieros. Actualmente, la Ciencia de Datos provee herramientas computacionales 
        (NLP, grafos, redes neuronales) para predecir la demanda basándose en la huella digital del consumidor.
        """)
        
        st.info("**Pregunta de Investigación:** ¿Qué factores técnicos y compositivos hacen exitoso a un lineup y cómo influye su estructura (balance entre headliners y bajada de cartel) en la decisión de compra del consumidor?")

        st.markdown("### Documento de Investigación")
        st.write("Puede acceder al manuscrito completo en formato PDF a continuación:")
        
        try:
            with open("manuscrito.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(label="Descargar Informe Completo (PDF)",
                               data=PDFbyte,
                               file_name="Perez_Christian_Lineups_SLR.pdf",
                               mime='application/octet-stream')
        except FileNotFoundError:
            st.warning("El archivo 'manuscrito.pdf' no se encuentra en el directorio actual. Añádalo para habilitar la descarga.")

    with col2:
        st.header("Clasificación del Estudio")
        st.write("**Área OCDE:** 1.02 Ciencias de la Computación e Información (IA y Ciencia de Datos).")
        st.write("**Objetivos de Desarrollo Sostenible (ODS):**")
        
        col_ods1, col_ods2 = st.columns(2)
        with col_ods1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Sustainable_Development_Goal-es-10.jpg/1280px-Sustainable_Development_Goal-es-10.jpg", caption="ODS 8", use_column_width=True)
        with col_ods2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sustainable_Development_Goal-es-09.jpg/1280px-Sustainable_Development_Goal-es-09.jpg", caption="ODS 9", use_column_width=True)

# --- PÁGINA 2: METODOLOGÍA PRISMA ---
elif pagina == "2. Metodología PRISMA":
    st.title("Metodología de Revisión Sistemática")
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.header("Estrategia de Búsqueda")
        st.write("**Bases de datos consultadas:** Google Scholar, Web of Science, Scopus, ScienceDirect.")
        st.write("**Fecha de búsqueda:** 22 de abril de 2026.")
        st.markdown("**Cadena de búsqueda (Booleana):**")
        st.code("""
"music festivals" AND 
("consumer behavior" OR "purchase intention" OR "ticket sales" OR demand) AND 
("machine learning" OR "predictive modeling" OR "Sentiment analysis")
        """, language="sql")
        
        st.header("Declaración de Uso de Inteligencia Artificial")
        st.write("""
        En alineación con los estándares éticos, se declara un enfoque de integración Humano-IA:
        *   **ChatGPT:** Asistente de programación para generar código Python destinado al preprocesamiento bibliográfico.
        *   **Gemini:** Traducción técnica masiva y extracción de resúmenes estructurados de los 78 abstracts cribados.
        *   **NotebookLM:** Soporte de lectura profunda para contrastar métricas y formateo en LaTeX.
        *   **Supervisión Humana:** Todas las decisiones heurísticas, criterios de exclusión y validación empírica de los modelos fueron realizadas íntegramente por el autor.
        """)
        
    with col2:
        st.header("Diagrama PRISMA 2020")
        try:
            st.image("PRISMA.png", caption="Figura 1: Flujo PRISMA ilustrando el proceso de identificación, cribado e inclusión de estudios.", use_column_width=True)
        except Exception:
            st.warning("No se encontró 'PRISMA.png'")

# --- PÁGINA 3: ESTADO DEL ARTE ---
elif pagina == "3. Estado del Arte":
    st.title("Estado del Arte y Artículos Seleccionados")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Tendencia Temporal de Publicaciones")
        try:
            st.image("tendencia.png", caption="Figura 2: Evolución de publicaciones sobre Ciencia de Datos y Festivales.", use_column_width=True)
        except Exception:
            st.warning("No se encontró 'tendencia.png'")
            
    with col2:
        st.header("Trabajos Relacionados (Related Work)")
        st.write("""
        *   **Contexto Histórico Nacional:** Se evidencia la opacidad y el desarrollo empírico de la industria en Chile (Calderón & Montecinos, 2016; Ojeda Medina, 2024).
        *   **State-of-the-Art Global:** La literatura de vanguardia utiliza LLMs para predecir flujos de visitantes con R² > 0.85 (Wang et al., 2026) y Regresión Discontinua para probar cómo los conciertos en vivo disparan el consumo de streaming digital (Montoro-Pons et al., 2023).
        """)

    st.markdown("---")
    st.header("Artículos Técnicos Incluidos (Matriz Final)")
    
    with st.expander("1. Hiller (2016) - The importance of quality: How music festivals achieved commercial success."):
        st.write("**Metodología:** Logit de Efectos Fijos Condicionales y Mínimos Cuadrados (OLS).")
        st.write("**Aporte:** Modeló matemáticamente el dilema entre popularidad y calidad crítica. Demostró que un artista con prestigio crítico es una inversión a largo plazo para la demanda del festival.")
    with st.expander("2. Montoro-Pons (2021) - Analyzing online search patterns of music festival tourists."):
        st.write("**Metodología:** Modelos de Grafos Aleatorios Exponenciales (ERGM y STERGM).")
        st.write("**Aporte:** Utilizó Google Trends para probar que festivales con lineups diversos actúan como nodos hiperconectados en la red de búsqueda, anticipando la intención de viaje.")
    with st.expander("3. de Lira et al. (2019) - Event attendance classification in social media."):
        st.write("**Metodología:** Procesamiento de Lenguaje Natural (NLP), Word Embeddings y Gradient Boosting.")
        st.write("**Aporte:** Clasificó la asistencia real analizando Twitter. Logró un 91.3% de exactitud analizando el sentimiento y las interacciones previas al evento.")
    with st.expander("4. Quan et al. (2025) - Improving competitiveness of live music venues based on hybrid probabilistic information..."):
        st.write("**Metodología:** Topic Modeling (LDA) + Deep Learning (BERT-BiLSTM).")
        st.write("**Aporte:** Comprobó semánticamente que el atributo 'Performance' (la calidad del lineup y el show) domina estadísticamente sobre factores logísticos en la intención de compra.")

# --- PÁGINA 4: RESULTADOS Y VISUALIZACIONES ---
elif pagina == "4. Resultados y Visualizaciones":
    st.title("Análisis de Datos y Resultados de la Literatura")
    st.write("Esta sección contrasta las tablas y figuras de los artículos originales con los gráficos interactivos generados para esta investigación.")
    
    st.markdown("---")
    
    # ---------------- SECCIÓN HILLER ----------------
    st.header("1. Impacto de Popularidad vs. Calidad Crítica (Hiller, 2016)")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Evidencia del Artículo Original:**")
        try:
            st.image("tabla_hiller.png", caption="Tabla 5 de Hiller (2016). Efectos marginales mediante Logit Condicional.", use_column_width=True)
        except Exception:
            st.warning("No se encontró 'tabla_hiller.png'")
    with col2:
        st.write("**Análisis de Datos:**")
        df_hiller = pd.DataFrame({
            "Atributo del Artista": ["Álbum Popular (Año 1)", "Álbum Popular (Año 2)", "Calidad Crítica (Año 1)", "Calidad Crítica (Año 2)"],
            "Aumento de Probabilidad": [27.5, 6.3, 17.1, 26.2],
            "Tipo de Tracción": ["Fama Comercial", "Fama Comercial", "Prestigio Crítico", "Prestigio Crítico"]
        })
        fig1 = px.bar(df_hiller, x="Atributo del Artista", y="Aumento de Probabilidad", color="Tipo de Tracción",
                      text="Aumento de Probabilidad", title="Aumento en Probabilidad de Contratación (%)",
                      color_discrete_sequence=["#1f77b4", "#ff7f0e"])
        fig1.update_traces(texttemplate='%{text}%', textposition='outside')
        fig1.update_layout(yaxis_range=[0, 35], margin=dict(t=40, b=0, l=0, r=0))
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("Explicación: Este gráfico demuestra matemáticamente que la fama comercial (Top Album) es volátil y decae el segundo año. En contraste, la 'calidad crítica' de la bajada de cartel es una inversión que aumenta sostenidamente la probabilidad de éxito a largo plazo.")

    st.markdown("---")

    # ---------------- SECCIÓN DE LIRA ----------------
    st.header("2. Exactitud Predictiva y Distribución Espacial (de Lira et al., 2019)")
    col3, col4 = st.columns(2)
    with col3:
        st.write("**Evidencia del Artículo Original:**")
        try:
            st.image("mapa_delira.png", caption="Mapa de asistentes inferidos vía NLP. Fuente: de Lira et al. (2019).", use_column_width=True)
        except Exception:
            st.warning("No se encontró 'mapa_delira.png'")
    with col4:
        st.write("**Análisis de Datos:**")
        df_delira = pd.DataFrame({
            "Modelo Computacional": ["Naive Bayes", "SVM", "Logistic Regression (BoW)", "Gradient Boosting (BoW+W2V)"],
            "Exactitud (Accuracy)": [58.7, 60.7, 86.8, 91.3]
        })
        fig2 = px.line(df_delira, x="Modelo Computacional", y="Exactitud (Accuracy)", markers=True, 
                       title="Rendimiento de Modelos NLP en Predicción de Asistencia",
                       color_discrete_sequence=["#2ca02c"])
        fig2.update_traces(marker=dict(size=12), line=dict(width=3))
        fig2.update_layout(yaxis_range=[50, 100], margin=dict(t=40, b=0, l=0, r=0))
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("Explicación: El gráfico evidencia cómo la transición de modelos simples a arquitecturas complejas con incrustación semántica (Word2Vec) permite mapear la intención de compra con más de un 91% de exactitud, generando los datos geoespaciales vistos en el mapa.")

    st.markdown("---")

    # ---------------- SECCIÓN QUAN & MONTORO ----------------
    st.header("3. Extracción de Tópicos Latentes y Análisis de Redes")
    col5, col6 = st.columns(2)
    with col5:
        st.write("**Atributos más discutidos (Quan et al., 2025):**")
        df_atributos = pd.DataFrame({
            "Atributo": ["Performance (Lineup)", "Service (Servicio)", "Environment (Entorno)", 
                         "Atmosphere (Atmósfera)", "Flavour (Sabor)", "Traffic (Accesos)", 
                         "Beverage (Bebidas)", "Price quality (Precio)"],
            "Menciones (LDA)": [5516, 4188, 3459, 3244, 2285, 2215, 2172, 2083]
        }).sort_values(by="Menciones (LDA)", ascending=True)
        
        fig3 = px.bar(df_atributos, x="Menciones (LDA)", y="Atributo", orientation='h',
                      title="Frecuencia Latente en Reseñas (Modelo LDA)", color="Menciones (LDA)", color_continuous_scale="Teal")
        fig3.update_layout(margin=dict(t=40, b=0, l=0, r=0))
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("Explicación: A través del modelo Latent Dirichlet Allocation (LDA), se comprueba que el 'Performance' (el lineup y los artistas) domina absolutamente la conversación orgánica, refutando la idea de que el precio o la logística son los factores de decisión primarios.")
        try:
            st.image("tabla_quan.png", caption="Tabla 4 de Quan et al. (2025) confirmando los datos.", use_column_width=True)
        except Exception:
            st.warning("No se encontró 'tabla_quan.png'")

    with col6:
        st.write("**Red de Búsquedas (Montoro-Pons, 2021):**")
        try:
            st.image("grafo_montoro.png", caption="Grafo ERGM. Fuente: Montoro-Pons (2021).", use_column_width=True)
            st.caption("Explicación: El Modelo de Grafos Aleatorios Exponenciales demuestra visualmente cómo un evento con diversidad de géneros actúa como un nodo 'hub'. La presencia del festival interconecta intenciones de búsqueda paralelas como 'Viajes' y 'Planificación', impulsando la economía local.")
        except Exception:
            st.warning("No se encontró 'grafo_montoro.png'")

# --- PÁGINA 5: DISCUSIÓN Y CONCLUSIONES ---
elif pagina == "5. Discusión y Conclusiones":
    st.title("Discusión, Conclusiones y Referencias")
    
    st.header("Anatomía de un Lineup Exitoso")
    st.write("""
    La evidencia sistematizada responde a la pregunta de investigación de manera concluyente:
    
    *   **¿Headliners masivos o bajada de cartel (Mid-card) fuerte?** 
        Los algoritmos predictivos demuestran que la intención de asistencia real y el volumen sostenido de conversación (eWOM) provienen de la densidad de la bajada del cartel. Los headliners masivos funcionan como marketing de tracción, pero una bajada de cartel de alta "calidad crítica" es la que asegura la venta sostenida (sold-out).
    *   **El Atributo Dominante:** 
        La extracción semántica (LDA) prueba empíricamente que el Performance (el cartel artístico) es el requisito top-of-mind fundamental del cliente para que ocurra la transacción, por sobre el precio o la infraestructura.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Vacíos de Investigación (Gaps)")
        st.write("""
        1. **Dinámica Inversa Causal:** Faltan modelos de Regresión Discontinua (RDD) que enlacen cómo los conciertos físicos impactan el consumo de streaming a largo plazo.
        2. **Integración en Tiempo Real:** Carencia de frameworks con Modelos de Lenguaje Grandes (LLMs) para evaluar el sentimiento de los fans en tiempo real ante cancelaciones de artistas.
        3. **Transparencia y Blockchain:** Necesidad de descentralizar la información de taquilla utilizando contratos inteligentes para unificar la captura de datos (Ojeda Medina, 2024).
        """)

    with col2:
        st.header("Referencias Principales")
        st.markdown("""
        1. Calderón, J., & Montecinos, C. (2016). *Arriba del escenario: El negocio de la música en vivo en Chile 1989-2016.* Universidad de Chile.
        2. de Lira, V. M., et al. (2019). Event attendance classification in social media. *Information Processing & Management*, 56(2), 687-703.
        3. Hiller, R. S. (2016). The importance of quality: How music festivals achieved commercial success. *Journal of Cultural Economics*, 40(3), 309-334.
        4. Montoro-Pons, J. D., & Cuadrado-García, M. (2021). Analyzing online search patterns of music festival tourists. *Tourism Economics*, 27(1).
        5. Ojeda Medina, J. J. (2024). *La contratación musical en la era digital: análisis comparado y desafíos para Chile.* Universidad de Chile.
        6. Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372(n71).
        7. Quan, F., et al. (2025). Research on improving the competitiveness of live music venues based on hybrid probabilistic information... *Entertainment Computing*, 52.
        """)