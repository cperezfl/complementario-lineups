# SLR: Éxito de Lineups en Festivales de Música

Este repositorio contiene el código fuente de una aplicación interactiva desarrollada en **Streamlit**. La aplicación funciona como el Producto 2 (Presentación Interactiva) para la asignatura de Metodología de Investigación en Ciencia de Datos, presentando los resultados de una Revisión Sistemática de Literatura (SLR) basada en la declaración PRISMA 2020.

## Información del Autor
* **Autor:** Christian Elías Isaías Pérez Flores
* **Carrera:** Ingeniería Civil en Ciencia de Datos
* **Institución:** Universidad Tecnológica Metropolitana (UTEM), Chile
* **Fecha:** Mayo, 2026

## Descripción del Proyecto
La aplicación comunica los hallazgos empíricos de 4 artículos científicos de alta densidad técnica (Hiller 2016, Montoro-Pons 2021, de Lira 2019, Quan 2025). Su objetivo es responder a la pregunta de investigación: *¿Qué factores técnicos y compositivos hacen exitoso a un lineup y cómo influye su estructura en la decisión de compra del consumidor?*

## Requisitos Previos e Instalación

Para ejecutar esta aplicación en su entorno local, es necesario contar con Python 3.8 o superior. Se recomienda el uso de un entorno virtual (Anaconda o venv).

1. Abra su terminal o consola de comandos.
2. Navegue hasta el directorio exacto donde se encuentran los archivos del proyecto:
   ```bash
   cd "ruta/hacia/esta/carpeta"
3. Instale las dependencias necesarias ejecutando el siguiente comando:
   pip install -r requirements.txt

## Ejecución de la Aplicación
Una vez instaladas las dependencias, asegúrese de seguir ubicado en el directorio del proyecto y ejecute:
   streamlit run app.py

Esto abrirá automáticamente una nueva pestaña en su navegador web predeterminado (típicamente en http://localhost:8501) con la aplicación en funcionamiento.

Estructura de Archivos Requerida
Para que la aplicación funcione correctamente y renderice todos los recursos visuales y descargables, el directorio debe contener exactamente los siguientes archivos con estos nombres (respetando mayúsculas y minúsculas):

* app.py: Script principal de la aplicación Streamlit.
* requirements.txt: Archivo de dependencias de Python.
* manuscrito.pdf: Informe completo de la investigación habilitado para descarga.
* logo_UTEM.png: Logo institucional para la barra de navegación.
* PRISMA.png: Diagrama de flujo metodológico.
* tendencia.png: Gráfico de análisis bibliométrico temporal.
* tabla_hiller.png: Captura de resultados del artículo de Hiller (2016).
* mapa_delira.png: Captura del mapa de calor del artículo de de Lira et al. (2019).
* tabla_quan.png: Captura de la tabla de extracción LDA de Quan et al. (2025).
* grafo_montoro.png: Captura del grafo ERGM de Montoro-Pons (2021).

## Stack Tecnológico
* Lenguaje: Python 3
* Framework Web: Streamlit
* Análisis de Datos: Pandas
* Visualización Interactiva: Plotly (Express)