# ---------------------------------------------------------
# COMPAÑÍA DE SEGUROS - ANÁLISIS EXPLORATORIO DE DATOS
# Caso de Estudio N°3
#
# Autor: Williams Michael Rupailla Ruiz
#
# Este proyecto consiste en desarrollar una aplicación
# interactiva utilizando Streamlit para realizar un
# Análisis Exploratorio de Datos (EDA) sobre un dataset
# de una compañía de seguros.
#
# Durante el desarrollo del proyecto se aplican conceptos
# de análisis de datos utilizando las siguientes librerías:
#
# - Pandas (manipulación de datos)
# - NumPy (cálculo numérico)
# - Matplotlib (visualización)
# - Seaborn (visualización estadística)
# - Streamlit (aplicación interactiva)
#
# ---------------------------------------------------------

# Importación de librerías necesarias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# CONFIGURACIÓN DE LA APLICACIÓN
# ---------------------------------------------------------
# st.set_page_config permite configurar la página web
# generada por Streamlit.

st.set_page_config(
    page_title="Insurance Company - EDA",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR - MENÚ DE NAVEGACIÓN
# ---------------------------------------------------------
# El sidebar permite al usuario navegar entre
# las diferentes secciones de la aplicación.

st.sidebar.title("📊 Navegación")

menu = st.sidebar.radio(
    "Seleccionar sección",
    [
        "Home",
        "Dataset Overview",
        "Exploratory Data Analysis",
        "Conclusions"
    ]
)



# ---------------------------------------------------------
# 🏠 SECCIÓN HOME
# ---------------------------------------------------------
# Esta sección presenta la información general del proyecto
# y sirve como introducción para el usuario que abre la app.

if menu == "Home":

    st.title("🏦📊 Compañía de Seguros")
    st.subheader("🔎 Análisis Exploratorio de Datos (EDA)")

    st.markdown("---")


    st.markdown("## 📌 Descripción del Proyecto")

    st.info("""
    Este proyecto tiene como objetivo realizar un **Análisis Exploratorio de Datos (EDA)**  
    utilizando el dataset **InsuranceCompany.csv**.

    A través del análisis se busca:
    
    ✔ Comprender la **estructura del dataset**  
    ✔ Identificar **patrones en los datos**  
    ✔ Detectar **relaciones entre variables**  
    """)

    st.markdown("---")

    st.markdown("## 🧰 Tecnologías Utilizadas")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        🐍 **Python**  
        📊 **Pandas**  
        🔢 **NumPy**
        """)

    with col2:
        st.markdown("""
        📈 **Matplotlib**  
        🎨 **Seaborn**  
        🌐 **Streamlit**
        """)

    st.markdown("---")

    st.markdown("## 🎯 Objetivo del Análisis")

    st.success("""
    El objetivo principal es explorar el dataset para descubrir información relevante sobre:

    📊 Clientes de la compañía  
    💰 Variables relacionadas con seguros  
    📉 Comportamientos y tendencias dentro de los datos  
    """)

    st.markdown("---")

    st.markdown("## 👨‍💻 Autor")

    st.markdown("""
    **Ing. Williams Michael Rupailla Ruiz**

    🎓 *Especialización en Python for Analytics*  
    📚 **Edición 55 — 2026**
    """)

    st.markdown("---")

    st.caption("📊 Proyecto académico desarrollado con Streamlit para análisis exploratorio de datos.")


# ---------------------------------------------------------
# 📂 DATASET OVERVIEW
# ---------------------------------------------------------
# En esta sección el usuario deberá cargar el dataset CSV.
# Mientras el archivo no sea cargado, la aplicación
# mostrará un mensaje indicando que es necesario subirlo.

elif menu == "Dataset Overview":

    st.title("📂 Vista General del Dataset")

    st.markdown("---")

    # ---------------------------------------------------------
    # CARGA DEL DATASET
    # ---------------------------------------------------------
    # Se permite al usuario cargar el archivo CSV manualmente.
    # Esto evita errores si el archivo no existe en la carpeta
    # del proyecto o si la app se ejecuta en Streamlit Cloud.

    archivo = st.file_uploader(
        "📤 Cargue el archivo InsuranceCompany.csv para continuar",
        type=["csv"]
    )

    # ---------------------------------------------------------
    # SI EL ARCHIVO NO SE HA CARGADO
    # ---------------------------------------------------------
    if archivo is None:

        st.warning("⚠️ Cargue el archivo CSV para poder continuar con el análisis.")

    # ---------------------------------------------------------
    # SI EL ARCHIVO YA FUE CARGADO
    # ---------------------------------------------------------
    else:

        # Leer dataset
        df = pd.read_csv(archivo)

        # Guardar dataset en memoria
        st.session_state["dataset"] = df

        # Usar dataset desde memoria
        df = st.session_state["dataset"]

        st.success("✅ Archivo cargado correctamente")

        st.markdown("---")

        # ---------------------------------------------------------
        # VISTA PREVIA DEL DATASET
        # ---------------------------------------------------------
        st.markdown("### 🔎 Primeras filas del dataset")

        st.dataframe(df.head())

        st.markdown("---")

        # ---------------------------------------------------------
        # DIMENSIONES DEL DATASET
        # ---------------------------------------------------------
        st.markdown("### 📏 Dimensiones del dataset")

        filas, columnas = df.shape

        col1, col2 = st.columns(2)

        col1.metric("📄 Número de filas", filas)
        col2.metric("📊 Número de columnas", columnas)


# ---------------------------------------------------------
# 📊 EXPLORATORY DATA ANALYTICS (EDA)
# ---------------------------------------------------------
# En esta sección realizaremos un análisis exploratorio del 
# dataset para comprender mejor la información disponible. 
# Se analizarán estadísticas, tipos de datos, valores nulos 
# y se generarán algunas visualizaciones iniciales.

elif menu == "Exploratory Data Analysis":

    st.title("📊 Exploratory Data Analysis")

    st.markdown("---")

    if "dataset" not in st.session_state:

        st.warning("⚠️ Primero debe cargar el archivo CSV en la sección **Dataset Overview**.")

    else:

        df = st.session_state["dataset"]

        st.success("✅ Dataset cargado correctamente")

        # Identificación de variables
        num_cols = df.select_dtypes(include=['int64','float64']).columns
        cat_cols = df.select_dtypes(include=['object']).columns
    
        # ---------------------------------------------------------
        # CREACIÓN DE PESTAÑAS
        # ---------------------------------------------------------
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
            "📋 Información del Dataset",
            "🧩 Clasificación Variables",
            "📊 Estadísticas Descriptivas",
            "⚠️ Valores Faltantes",
            "📈 Variables Numéricas",
            "🏷️ Variables Categóricas",
            "📊 Numérica vs Categórica",
            "🔗 Categórica vs Categórica",
            "🎛️ Análisis Dinámico",
            "💡 Hallazgos"
        ])

        # =====================================================
        # 📊 EDA 1 — Información del Dataset
        # =====================================================
        with tab1:

            st.subheader("📋 Información general del dataset")

            # -------------------------------------------------
            # CÁLCULOS GENERALES
            # -------------------------------------------------
            total_registros = df.shape[0]
            total_variables = df.shape[1]
            total_nulos = df.isnull().sum().sum()
            filas = df.shape[0]
            columnas = df.shape[1]

            # -------------------------------------------------
            # RESUMEN GENERAL
             # -------------------------------------------------
            st.markdown("### 📌 Resumen del dataset")

            col1, col2, col3 = st.columns(3)

            col1.metric("**📄 Total de registros**", total_registros)
            col2.metric("**📊 Total de variables**", total_variables)
            col3.metric("**⚠️ Total de valores nulos**", total_nulos)

            col4, col5 = st.columns(2)

            col4.metric("**📑 Filas**", filas)
            col5.metric("**🧾 Columnas**", columnas)

            st.markdown("---")

            # -------------------------------------------------
            # TIPOS DE DATOS
            # -------------------------------------------------
            st.markdown("### 🧾 Tipo de dato de las variables")

            tipos_datos = df.dtypes.reset_index()
            tipos_datos.columns = ["Variable", "Tipo de dato"]

            st.dataframe(tipos_datos, use_container_width=True)

            st.markdown("---")

            # -------------------------------------------------
            # VALORES NULOS POR VARIABLE
            # -------------------------------------------------
            st.markdown("### ⚠️ Valores nulos por variable")

            nulos = df.isnull().sum().reset_index()
            nulos.columns = ["Variable", "Valores nulos"]

            nulos["Porcentaje %"] = (nulos["Valores nulos"] / len(df)) * 100
            nulos["Porcentaje %"] = nulos["Porcentaje %"].round(2)

            st.dataframe(nulos, use_container_width=True)

            import io

            # -------------------------------------------------
            # INFO DEL DATASET ()
            # -------------------------------------------------
            st.markdown("### 🧠 Información estructural del dataset (.info())")

            buffer = io.StringIO()
            df.info(buf=buffer)

            info_str = buffer.getvalue()

            st.text(info_str)

            st.markdown("---")

        # =====================================================
        # 📊 EDA 2 — Clasificación de Variables
        # =====================================================
        with tab2:

            st.subheader("🧩 Clasificación de variables")

            # -------------------------------------------------
            # FUNCIÓN PERSONALIZADA PARA CLASIFICAR VARIABLES
            # -------------------------------------------------
            def clasificar_variables(df):

                # Identificación de variables
                num_cols = df.select_dtypes(include=['int64','float64']).columns
                cat_cols = df.select_dtypes(include=['object']).columns

                return num_cols, cat_cols
            
            # Obtener variables usando función personalizada
            num_cols, cat_cols = clasificar_variables(df)

            # -------------------------------------------------
            # RESUMEN DE VARIABLES
            # -------------------------------------------------
            col1, col2 = st.columns(2)

            col1.metric("🔢 Variables numéricas", len(num_cols))
            col2.metric("🏷️ Variables categóricas", len(cat_cols))

            st.markdown("---")

            # -------------------------------------------------
            # VARIABLES NUMÉRICAS
            # -------------------------------------------------
            st.markdown("### 🔢 Variables numéricas")

            df_num = pd.DataFrame(num_cols, columns=["Variable Numérica"])

            st.dataframe(df_num, use_container_width=True)

            st.markdown("---")

            # -------------------------------------------------
            # VARIABLES CATEGÓRICAS
            # -------------------------------------------------
            st.markdown("### 🏷️ Variables categóricas")

            df_cat = pd.DataFrame(cat_cols, columns=["Variable Categórica"])

            st.dataframe(df_cat, use_container_width=True)

            st.markdown("---")

            # -------------------------------------------------
            # CONTEO DE CATEGORÍAS
            # -------------------------------------------------
            st.markdown("### 📊 Conteo de valores por variable categórica")

            if len(cat_cols) > 0:

                variable_cat = st.selectbox(
                    "Seleccione una variable categórica",
                    cat_cols
                )

                conteo = df[variable_cat].value_counts().reset_index()
                conteo.columns = ["Categoría", "Frecuencia"]

                st.dataframe(conteo, use_container_width=True)

            else:
                st.info("No se encontraron variables categóricas en el dataset.")

            # -------------------------------------------------
            # GRÁFICO DE DISTRIBUCIÓN
            # -------------------------------------------------
            fig, ax = plt.subplots()

            df[variable_cat].value_counts().plot(
                kind="bar",
                ax=ax
            )

            ax.set_title(f"Distribución de {variable_cat}")
            ax.set_ylabel("Frecuencia")
            ax.set_xlabel("Categoría")

            st.pyplot(fig)


            # -------------------------------------------------
            # SUGERENCIA ANALÍTICA
            # -------------------------------------------------
            st.info("""

                - Las **variables numéricas** permiten realizar análisis estadísticos,
                  correlaciones y distribuciones.

                - Las **variables categóricas** ayudan a segmentar los datos
                  y analizar comportamientos entre grupos.
             """)

            st.markdown("---")

            # -------------------------------------------------
            # 📊 GRÁFICO DE PROPORCIÓN DE VARIABLES
            # -------------------------------------------------
            st.markdown("### 🥧 Proporción de tipos de variables")

            labels = ["Variables Numéricas", "Variables Categóricas"]
            valores = [len(num_cols), len(cat_cols)]

            fig, ax = plt.subplots()

            ax.pie(
            valores,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
            )

            ax.set_title("Distribución de tipos de variables")

            st.pyplot(fig)

        # =====================================================
        # 📊 EDA 3 — Estadísticas Descriptivas
        # =====================================================
        with tab3:

            st.subheader("📊 Estadísticas descriptivas de las variables numéricas")

            # -------------------------------------------------
            # TABLA GENERAL DE ESTADÍSTICAS
            # -------------------------------------------------
            st.markdown("### 📋 Resumen estadístico general")

            st.dataframe(df.describe(), use_container_width=True)

            st.markdown("---")

            # -------------------------------------------------
            # ANÁLISIS INDIVIDUAL DE VARIABLE NUMÉRICA
            # -------------------------------------------------
            st.markdown("### 🔎 Análisis de una variable numérica")

            if len(num_cols) > 0:

                variable = st.selectbox(
                "📊 Seleccione una variable numérica para analizar",
                num_cols
                )

                media = df[variable].mean()
                mediana = df[variable].median()
                minimo = df[variable].min()
                maximo = df[variable].max()
                desviacion = df[variable].std()

                col1, col2, col3, col4, col5 = st.columns(5)

                col1.metric("📈 Media", round(media, 2))
                col2.metric("📍 Mediana", round(mediana, 2))
                col3.metric("⬇️ Mínimo", minimo)
                col4.metric("⬆️ Máximo", maximo)
                col5.metric("📉 Desv. Estándar", round(desviacion, 2))

                st.markdown("---")

                # -------------------------------------------------
                # GRÁFICO DE DISTRIBUCIÓN
                # -------------------------------------------------
                st.markdown("### 📉 Distribución de la variable seleccionada")

                fig, ax = plt.subplots()

                sns.histplot(df[variable], kde=True, ax=ax)

                ax.set_title(f"Distribución de {variable}")
                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")

                st.pyplot(fig)

                st.markdown("### 🧠 Interpretación básica")

                if media > mediana:
                    interpretacion = "La media es mayor que la mediana, lo que sugiere una posible **asimetría hacia la derecha** en la distribución."
                elif media < mediana:
                    interpretacion = "La media es menor que la mediana, lo que sugiere una posible **asimetría hacia la izquierda** en la distribución."
                else:
                    interpretacion = "La media y la mediana son similares, lo que indica una **distribución relativamente simétrica**."

                st.info(f"""
                📊 **Media:** {round(media,2)}  
                📍 **Mediana:** {round(mediana,2)}  
                📉 **Desviación estándar:** {round(desviacion,2)}

                {interpretacion}
                """)

            else:

                st.warning("⚠️ No se encontraron variables numéricas en el dataset.")

        # =====================================================
        # ⚠️ EDA 4 — Valores Faltantes
        # =====================================================
        with tab4:

            st.subheader("⚠️ Análisis de valores faltantes")

            # -------------------------------------------------
            # CÁLCULO DE VALORES NULOS
            # -------------------------------------------------
            missing = df.isnull().sum()
            porcentaje_nulos = (df.isnull().sum() / len(df)) * 100

            tabla_nulos = pd.DataFrame({
                "📌 Variable": missing.index,
                "⚠️ Valores nulos": missing.values,
                "📊 % de valores nulos": porcentaje_nulos.values.round(2)
            })

            st.markdown("### 📋 Resumen de valores faltantes")

            st.dataframe(tabla_nulos, use_container_width=True)

            st.markdown("---")

            # -------------------------------------------------
            # RESUMEN GENERAL
            # -------------------------------------------------
            total_nulos = missing.sum()

            col1, col2 = st.columns(2)

            col1.metric("⚠️ Total valores nulos", total_nulos)
            col2.metric("📊 % total de nulos", round((total_nulos / df.size) * 100, 2))

            st.markdown("---")

            # -------------------------------------------------
            # GRÁFICO DE VALORES NULOS
            # -------------------------------------------------
            st.markdown("### 📊 Visualización de valores faltantes por variable")

            fig, ax = plt.subplots(figsize=(10,5))

            missing.plot(kind="bar", ax=ax)

            ax.set_title("Valores faltantes por variable")
            ax.set_xlabel("Variables")
            ax.set_ylabel("Cantidad de valores nulos")

            plt.xticks(rotation=45)

            st.pyplot(fig)

            st.markdown("---")

            # -------------------------------------------------
            # MENSAJE DE CALIDAD DE DATOS
            # -------------------------------------------------
            st.markdown("### 🧠 Interpretación del análisis")

            if total_nulos == 0:

                st.info("""
                El análisis muestra que el dataset **no presenta valores faltantes**, lo cual indica
                una **buena calidad de los datos** y permite realizar análisis estadísticos
                sin necesidad de aplicar técnicas de imputación o limpieza adicional.
                """)

            else:

                variable_mas_nulos = missing.idxmax()
                cantidad_mas_nulos = missing.max()
                porcentaje_max = porcentaje_nulos.max()

                st.info(f"""
                Se identificaron **{total_nulos} valores faltantes en el dataset**.

                La variable con mayor cantidad de datos faltantes es **{variable_mas_nulos}**
                con **{cantidad_mas_nulos} valores nulos ({porcentaje_max:.2f}%)**.

                Esto sugiere que podría ser necesario aplicar **estrategias de limpieza o imputación**
                de datos antes de realizar análisis más avanzados o modelos predictivos.
                """)

        # =====================================================
        # 📈 EDA 5 — Distribución de Variables Numéricas
        # =====================================================
        with tab5:

            st.subheader("📈 Distribución de variables numéricas")

            if len(num_cols) > 0:

                # -------------------------------------------------
                # SELECCIÓN DE VARIABLE
                # -------------------------------------------------
                variable = st.selectbox(
                    "📊 Seleccione una variable numérica para analizar",
                    num_cols,
                    key="eda5_variable_numerica"
                )
                # -------------------------------------------------
                # MÉTRICAS RÁPIDAS
                # -------------------------------------------------
                media = df[variable].mean()
                mediana = df[variable].median()
                minimo = df[variable].min()
                maximo = df[variable].max()

                col1, col2, col3, col4 = st.columns(4)

                col1.metric("📈 Media", round(media,2))
                col2.metric("📊 Mediana", round(mediana,2))
                col3.metric("⬇️ Mínimo", minimo)
                col4.metric("⬆️ Máximo", maximo)

                st.markdown("---")

                # -------------------------------------------------
                # HISTOGRAMA
                # -------------------------------------------------
                st.markdown("### 📊 Histograma de la variable")

                fig, ax = plt.subplots()

                sns.histplot(df[variable], kde=True, ax=ax)

                ax.set_title(f"Distribución de {variable}")
                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")

                st.pyplot(fig)

                st.markdown("---")

                # -------------------------------------------------
                # BOXPLOT PARA OUTLIERS
                # -------------------------------------------------
                st.markdown("### 📦 Detección de valores atípicos (Outliers)")

                fig2, ax2 = plt.subplots()

                sns.boxplot(x=df[variable], ax=ax2)

                ax2.set_title(f"Boxplot de {variable}")

                st.pyplot(fig2)
                # -------------------------------------------------
                # INTERPRETACIÓN VISUAL
                # -------------------------------------------------
                st.markdown("### 🧠 Interpretación de la distribución")

                # Evaluar simetría básica
                if media > mediana:
                    forma = "asimetría hacia la derecha (cola larga hacia valores altos)"
                elif media < mediana:
                    forma = "asimetría hacia la izquierda (cola larga hacia valores bajos)"
                else:
                    forma = "una distribución aproximadamente simétrica"

                # Detección simple de outliers usando IQR
                Q1 = df[variable].quantile(0.25)
                Q3 = df[variable].quantile(0.75)
                IQR = Q3 - Q1

                limite_inferior = Q1 - 1.5 * IQR
                limite_superior = Q3 + 1.5 * IQR

                outliers = df[(df[variable] < limite_inferior) | (df[variable] > limite_superior)]

                st.info(f"""
                📊 La variable **{variable}** presenta {forma} según la comparación entre la media ({round(media,2)}) y la mediana ({round(mediana,2)}).

                📦 El boxplot permite identificar **posibles valores atípicos (outliers)** fuera del rango esperado.

                🔎 Se detectaron aproximadamente **{len(outliers)} posibles valores atípicos** en esta variable.

                Esto indica que la distribución de los datos puede presentar **variabilidad o casos extremos** que podrían influir en análisis estadísticos posteriores.
                """)

            else:

                st.warning("⚠️ No se encontraron variables numéricas en el dataset.")

        # =====================================================
        # EDA 6 — Variables Categóricas
        # =====================================================
        with tab6:

            st.subheader("📊 Análisis de Variables Categóricas")

            st.markdown("Explora la distribución de las variables categóricas del dataset 🧠")

            if len(cat_cols) > 0:

                variable = st.selectbox(
                    "🏷️ Seleccione una variable categórica",
                    cat_cols,
                    key="eda6_variable_categorica"
                )

                st.markdown(f"### 📌 Distribución de **{variable}**")

                # Conteo de valores
                counts = df[variable].value_counts(dropna=False)

                # Tabla de frecuencias
                freq_table = counts.reset_index()
                freq_table.columns = [variable, "Conteo"]
                freq_table["Porcentaje (%)"] = (freq_table["Conteo"] / len(df) * 100).round(2)

                st.markdown("#### 📋 Tabla de frecuencias")
                st.dataframe(freq_table)

                # Gráfico
                fig, ax = plt.subplots()

                sns.countplot(
                    x=df[variable],
                    order=counts.index,
                    ax=ax
                )

                plt.xticks(rotation=45)

                ax.set_title(f"📊 Distribución de {variable}")
                ax.set_xlabel(variable)
                ax.set_ylabel("Frecuencia")

                st.pyplot(fig)
                
                st.markdown("### 🥧 Proporción de categorías")

                fig2, ax2 = plt.subplots()

                ax2.pie(
                    freq_table["Conteo"],
                    labels=freq_table[variable],
                    autopct='%1.1f%%',
                    startangle=90
                )

                ax2.set_title(f"Proporción de {variable}")

                st.pyplot(fig2)

                # -------------------------------------------------
                # INTERPRETACIÓN BÁSICA
                # -------------------------------------------------
                st.markdown("### 🧠 Interpretación del análisis")

                categoria_principal = counts.idxmax()
                valor_principal = counts.max()
                porcentaje_principal = (valor_principal / len(df)) * 100

                st.info(f"""
                📊 La categoría más frecuente en **{variable}** es **{categoria_principal}**, 
                con **{valor_principal} registros**, lo que representa aproximadamente 
                **{porcentaje_principal:.2f}% del dataset**.

                Esto sugiere que esta categoría tiene **mayor representación dentro de los datos**, 
                lo que puede indicar un patrón predominante en la variable analizada.
                """)

                # Información adicional
                st.markdown("### 📈 Información rápida")
                col1, col2 = st.columns(2)

                col1.metric("🔢 Categorías únicas", df[variable].nunique())
                col2.metric("⚠️ Valores faltantes", df[variable].isnull().sum())

            else:
                st.warning("⚠️ No se encontraron variables categóricas en el dataset.")

        # =====================================================
        # EDA 7 — Numérica vs Categórica
        # =====================================================
        with tab7:

            st.subheader("📊 Relación entre Variable Numérica y Categórica")

            st.markdown("Explora cómo cambia una variable numérica según cada categoría 🔎")

            if len(num_cols) > 0 and len(cat_cols) > 0:

                col1, col2 = st.columns(2)

                with col1:
                    num_var = st.selectbox(
                        "📈 Variable numérica",
                        num_cols,
                        key="eda7_num_variable"
                    )

                with col2:
                    cat_var = st.selectbox(
                        "🏷️ Variable categórica",
                        cat_cols,
                        key="eda7_cat_variable"
                    )

                # eliminar nulos
                temp_df = df[[num_var, cat_var]].dropna()

                st.markdown(f"### 📌 Análisis de **{num_var}** por **{cat_var}**")

                # =====================================================
                # Estadísticas por categoría
                # =====================================================
                st.markdown("#### 📋 Estadísticas por categoría")

                summary = temp_df.groupby(cat_var)[num_var].describe()

                st.dataframe(summary)

                # =====================================================
                # Gráfico
                # =====================================================
                st.markdown("#### 📊 Distribución visual")

                order = temp_df.groupby(cat_var)[num_var].median().sort_values().index

                fig, ax = plt.subplots(figsize=(9,5))

                sns.boxplot(
                    x=temp_df[cat_var],
                    y=temp_df[num_var],
                    order=order,
                    ax=ax
                )

                sns.stripplot(
                    x=temp_df[cat_var],
                    y=temp_df[num_var],
                    order=order,
                    color="black",
                    alpha=0.4,
                    ax=ax
                )

                plt.xticks(rotation=45)

                ax.set_title(f"📊 Distribución de {num_var} según {cat_var}")
                ax.set_xlabel(cat_var)
                ax.set_ylabel(num_var)

                st.pyplot(fig)

                # =====================================================
                # Métricas rápidas
                # =====================================================
                st.markdown("### ⚡ Información rápida")

                col1, col2, col3 = st.columns(3)

                col1.metric("🔢 Categorías", temp_df[cat_var].nunique())
                col2.metric("📊 Media global", round(temp_df[num_var].mean(),2))
                col3.metric("📉 Desviación estándar", round(temp_df[num_var].std(),2))

                # =====================================================
                # Tabla final para análisis
                # =====================================================
                st.markdown("### 📋 Tabla resumen final")

                final_table = (
                    temp_df
                    .groupby(cat_var)[num_var]
                    .agg(["count", "mean", "median", "min", "max", "std"])
                    .sort_values("mean", ascending=False)
                    .reset_index()
                )

                st.dataframe(final_table)

                # =====================================================
                # INTERPRETACIÓN DEL ANÁLISIS
                # =====================================================
                st.markdown("### 🧠 Interpretación del análisis")

                categoria_top = final_table.iloc[0][cat_var]
                media_top = final_table.iloc[0]["mean"]

                categoria_baja = final_table.iloc[-1][cat_var]
                media_baja = final_table.iloc[-1]["mean"]

                diferencia = media_top - media_baja

                st.info(f"""
                📊 Al analizar la variable **{num_var}** según **{cat_var}**, se observa que:

                • La categoría **{categoria_top}** presenta el **mayor valor promedio** de {num_var} con aproximadamente **{media_top:.2f}**.

                • La categoría **{categoria_baja}** presenta el **menor valor promedio** con aproximadamente **{media_baja:.2f}**.

                📈 La diferencia entre ambas categorías es de aproximadamente **{diferencia:.2f}**, lo que sugiere que el comportamiento de **{num_var}** puede variar significativamente entre las categorías de **{cat_var}**.

                Esto permite identificar **posibles patrones o segmentos dentro del dataset**, lo cual es útil para comprender mejor el comportamiento de los datos.
                """)

            else:
                st.warning("⚠️ No hay suficientes variables numéricas y categóricas para este análisis.")


        # =====================================================
        # EDA 8 — Categórica vs Categórica
        # =====================================================
        with tab8:

            st.subheader("📊 Relación entre Variables Categóricas")

            st.markdown("Analiza la relación entre dos variables categóricas mediante tablas y mapas de calor 🔍")

            if len(cat_cols) >= 2:

                col1, col2 = st.columns(2)

                with col1:
                    cat1 = st.selectbox(
                        "🏷️ Primera variable categórica",
                        cat_cols,
                        key="eda8_cat1"
                    )

                with col2:
                    cat2 = st.selectbox(
                        "🏷️ Segunda variable categórica",
                        cat_cols,
                        index=1,
                        key="eda8_cat2"
                    )
                if cat1 == cat2:
                    st.warning("⚠️ Debes seleccionar **dos variables diferentes** para crear la tabla de contingencia.")
                else:

                    temp_df = df[[cat1, cat2]].dropna()

                    tabla = pd.crosstab(temp_df[cat1], temp_df[cat2])

                    st.dataframe(tabla)              

                # eliminar nulos
                temp_df = df[[cat1, cat2]].dropna()

                st.markdown(f"### 📋 Tabla de contingencia: **{cat1} vs {cat2}**")

                tabla = pd.crosstab(temp_df[cat1], temp_df[cat2])

                st.dataframe(tabla)

                # =====================================================
                # Heatmap
                # =====================================================
                st.markdown("### 🔥 Mapa de calor de frecuencias")

                fig, ax = plt.subplots(figsize=(8,5))

                sns.heatmap(
                    tabla,
                    annot=True,
                    cmap="Blues",
                    fmt="d",
                    linewidths=0.5,
                    ax=ax
                )

                ax.set_title(f"Relación entre {cat1} y {cat2}")

                st.pyplot(fig)

                # =====================================================
                # Tabla de porcentajes
                # =====================================================
                st.markdown("### 📊 Tabla de porcentajes (%)")

                tabla_pct = tabla.div(tabla.sum(axis=1), axis=0) * 100
                tabla_pct = tabla_pct.round(2)

                st.dataframe(tabla_pct)

                # =====================================================
                # Métricas rápidas
                # =====================================================
                st.markdown("### ⚡ Información rápida")

                col1, col2, col3 = st.columns(3)

                col1.metric("🔢 Categorías en variable 1", temp_df[cat1].nunique())
                col2.metric("🔢 Categorías en variable 2", temp_df[cat2].nunique())
                col3.metric("📊 Total observaciones", len(temp_df))

                # =====================================================
                # INTERPRETACIÓN DEL ANÁLISIS
                # =====================================================
                st.markdown("### 🧠 Interpretación del análisis")

                max_val = tabla.values.max()
                pos = np.where(tabla == max_val)

                categoria1 = tabla.index[pos[0][0]]
                categoria2 = tabla.columns[pos[1][0]]

                st.info(f"""
                📊 La combinación más frecuente entre **{cat1}** y **{cat2}** es:

                **{categoria1} — {categoria2}**

                con aproximadamente **{max_val} registros**.

                Esto sugiere que existe una posible **relación o patrón predominante**
                entre estas dos categorías dentro del dataset.
                """)

            else:
                st.warning("⚠️ Se necesitan al menos dos variables categóricas para este análisis.")

        # =====================================================
        # EDA 9 — Análisis Dinámico
        # =====================================================
        with tab9:

            st.subheader("🔎 EDA Dinámico del Dataset")

            st.markdown("Utiliza los controles interactivos para explorar las variables del dataset 📊")

            # =====================================================
            # Selectbox
            # =====================================================
            variable = st.selectbox(
                "📌 Seleccione una variable",
                df.columns,
                key="eda9_variable"
            )

            data = df[variable].dropna()

            st.markdown(f"### 📊 Distribución de **{variable}**")

            if pd.api.types.is_numeric_dtype(df[variable]):

                bins = st.slider(
                    "🔧 Número de bins del histograma",
                    5,
                    50,
                    20
                )

                fig, ax = plt.subplots()

                sns.histplot(data, kde=True, bins=bins, ax=ax)

                st.pyplot(fig)

            else:

                st.bar_chart(data.value_counts())

            # =====================================================
            # Checkbox
            # =====================================================
            if st.checkbox("📋 Mostrar tabla de valores"):

                st.dataframe(df[[variable]].value_counts())

            # =====================================================
            # Multiselect
            # =====================================================
            st.markdown("## 🔥 Correlation Explorer")

            num_vars = df.select_dtypes(include="number").columns

            selected_vars = st.multiselect(
                "Seleccione variables numéricas",
                num_vars,
                default=list(num_vars[:4])
            )

            if len(selected_vars) >= 2:

                corr = df[selected_vars].corr()

                st.markdown("### 🔥 Heatmap de correlación")

                fig, ax = plt.subplots(figsize=(8,6))

                sns.heatmap(
                    corr,
                    annot=True,
                    cmap="coolwarm",
                    ax=ax
                )

                st.pyplot(fig)

                # =====================================================
                # Top correlaciones
                # =====================================================
                st.markdown("### 📊 Top correlaciones")

                corr_pairs = (
                    corr.abs()
                    .unstack()
                    .sort_values(ascending=False)
                )

                corr_pairs = corr_pairs[corr_pairs < 1].drop_duplicates()

                st.dataframe(corr_pairs.head(10))

                # =====================================================
                # Scatter dinámico
                # =====================================================
                st.markdown("### 🎯 Scatter interactivo")

                col1, col2 = st.columns(2)

                with col1:
                    x_var = st.selectbox(
                        "Variable X",
                        selected_vars,
                        key="scatter_x"
                    )

                with col2:
                    y_var = st.selectbox(
                        "Variable Y",
                        selected_vars,
                        key="scatter_y"
                    )

                if x_var != y_var:

                    fig, ax = plt.subplots()

                    sns.scatterplot(
                        x=df[x_var],
                        y=df[y_var],
                        ax=ax
                    )

                    ax.set_title(f"Relación entre {x_var} y {y_var}")

                    st.pyplot(fig)

                else:
                    st.info("Seleccione dos variables diferentes para el gráfico de dispersión.")

                st.dataframe(corr_pairs.head(10))

                # =====================================================
                # INTERPRETACIÓN DE CORRELACIÓN
                # =====================================================
                st.markdown("### 🧠 Interpretación de correlación")

                top_pair = corr_pairs.index[0]
                top_value = corr_pairs.iloc[0]

                var1, var2 = top_pair

                if top_value > 0.7:
                    nivel = "una **correlación fuerte**"
                elif top_value > 0.4:
                    nivel = "una **correlación moderada**"
                else:
                    nivel = "una **correlación débil**"

                st.info(f"""
                🔗 La relación más destacada es entre **{var1}** y **{var2}** con un valor de correlación de **{top_value:.2f}**.

                Esto indica {nivel} entre ambas variables, lo que sugiere que los cambios en una variable pueden estar asociados con cambios en la otra.
                """)

            else:
                st.info("Seleccione al menos dos variables numéricas para calcular correlación.")

        # =====================================================
        # EDA 10 — Hallazgos Clave
        # =====================================================
        with tab10:

            st.subheader("🔎 Hallazgos Clave del Análisis Exploratorio")

            # =====================================================
            # Información general
            # =====================================================
            st.markdown("### 📊 Información general del dataset")

            # =====================================================
            # Visualización resumen
            # =====================================================

            st.markdown("### 📊 Visualización resumen")

            if len(num_cols) > 0:

                import seaborn as sns
                import matplotlib.pyplot as plt

                fig, ax = plt.subplots(figsize=(10,5))

                df[num_cols].hist(ax=ax)
                plt.tight_layout()

                st.pyplot(fig)

                st.markdown("📌 Distribución general de las variables numéricas del dataset.")

            col1, col2, col3 = st.columns(3)

            col1.metric("📄 Registros", df.shape[0])
            col2.metric("📊 Variables", df.shape[1])
            col3.metric("⚠️ Valores faltantes", df.isnull().sum().sum())

            # =====================================================
            # Variables numéricas
            # =====================================================
            num_cols = df.select_dtypes(include="number").columns

            if len(num_cols) > 1:

                st.markdown("### 🔥 Correlaciones detectadas")

                corr = df[num_cols].corr().abs()

                # Heatmap de correlación

                fig, ax = plt.subplots(figsize=(8,6))

                sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)

                st.pyplot(fig)

                st.markdown("📌 El mapa de calor muestra la relación entre las variables numéricas.")

                corr_pairs = (
                    corr.unstack()
                    .sort_values(ascending=False)
                )

                corr_pairs = corr_pairs[corr_pairs < 1]

                top_corr = corr_pairs.drop_duplicates().head(5)

                st.dataframe(top_corr)

                st.markdown(
                    "📌 Estas son las **variables con mayor relación estadística** en el dataset."
                )

            # =====================================================
            # Variables categóricas
            # =====================================================
            cat_cols = df.select_dtypes(include="object").columns

            if len(cat_cols) > 0:

                st.markdown("### 🏷️ Variables categóricas destacadas")

                cat_summary = pd.DataFrame({
                    "Variable": cat_cols,
                    "Categorías únicas": [df[c].nunique() for c in cat_cols],
                    "Valores faltantes": [df[c].isnull().sum() for c in cat_cols]
                })

                st.dataframe(cat_summary)

            # =====================================================
            # Variables con mayor variabilidad
            # =====================================================
            if len(num_cols) > 0:

                st.markdown("### 📈 Variables con mayor variabilidad")

                variability = (
                    df[num_cols]
                    .std()
                    .sort_values(ascending=False)
                    .head(5)
                )

                st.dataframe(variability)

                st.markdown(
                    "📌 Estas variables presentan **mayor dispersión**, lo que puede indicar mayor variabilidad en los datos."
                )
            
            # =====================================================
            # Insights automáticos del análisis
            # =====================================================

            st.markdown("### 💡 Insights principales del EDA")

            insights = []

            # Insight correlación
            if len(num_cols) > 1:
                top_pair = top_corr.index[0]
                insights.append(
                    f"🔗 Existe una fuerte relación entre **{top_pair[0]}** y **{top_pair[1]}**."
                )

            # Insight variabilidad
            if len(num_cols) > 0:
                var_max = variability.index[0]
                insights.append(
                    f"📈 La variable **{var_max}** presenta la mayor variabilidad en los datos."
                )

            # Insight categórico
            if len(cat_cols) > 0:
                max_cat = cat_summary.sort_values("Categorías únicas", ascending=False).iloc[0]
                insights.append(
                    f"🏷️ La variable categórica **{max_cat['Variable']}** tiene la mayor diversidad de categorías."
                )

            # Mostrar insights
            for i in insights:
                st.info(i)

# ---------------------------------------------------------
# Aquí se presentarán los hallazgos obtenidos
# a partir del análisis exploratorio de datos.

elif menu == "Conclusions":

    st.title("📑 Conclusiones del Análisis")

    # =====================================================
    # Recuperar dataset desde memoria
    # =====================================================

    if "dataset" not in st.session_state:

        st.warning("⚠️ No se encontró ningún dataset cargado.")
        st.info("📂 Por favor cargue un archivo CSV para visualizar las conclusiones.")
        st.stop()

    df = st.session_state["dataset"]

    st.markdown("""
    🧠 En esta sección se presentan las **conclusiones finales**
    obtenidas a partir del análisis exploratorio de datos (EDA).

    El objetivo es **transformar los datos analizados en información útil**
    para comprender mejor a los **clientes, variables relacionadas con seguros
    y patrones presentes en el dataset**.
    """)

    st.divider()

    # =====================================================
    # Métricas generales del dataset
    # =====================================================

    total_registros = df.shape[0]
    total_variables = df.shape[1]
    valores_faltantes = int(df.isnull().sum().sum())

    num_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(include="object").columns

    col1, col2, col3 = st.columns(3)

    col1.metric("📄 Registros", total_registros)
    col2.metric("📊 Variables", total_variables)
    col3.metric("⚠️ Valores faltantes", valores_faltantes)

    st.divider()

    # =====================================================
    # Correlación más fuerte
    # =====================================================

    correlacion_texto = "No se identificaron correlaciones relevantes."

    if len(num_cols) > 1:

        corr = df[num_cols].corr().abs()

        corr_pairs = (
            corr.unstack()
            .sort_values(ascending=False)
        )

        corr_pairs = corr_pairs[corr_pairs < 1]

        if len(corr_pairs) > 0:

            var1, var2 = corr_pairs.index[0]
            corr_val = corr_pairs.iloc[0]

            correlacion_texto = f"Las variables **{var1}** y **{var2}** presentan una correlación aproximada de **{corr_val:.2f}**, lo que indica que tienden a variar de forma similar dentro del dataset."

    # =====================================================
    # Variable con mayor variabilidad
    # =====================================================

    variabilidad_texto = "No se identificaron variables numéricas suficientes."

    if len(num_cols) > 0:

        std_vals = df[num_cols].std().sort_values(ascending=False)

        var_max = std_vals.index[0]
        std_max = std_vals.iloc[0]

        variabilidad_texto = f"La variable **{var_max}** muestra la mayor dispersión con una desviación estándar de **{std_max:.2f}**, lo que indica una alta variabilidad entre los registros."

    # =====================================================
    # Variable categórica dominante
    # =====================================================

    categoria_texto = "No se encontraron variables categóricas relevantes."

    if len(cat_cols) > 0:

        col = cat_cols[0]

        top_cat = df[col].value_counts().idxmax()
        top_freq = df[col].value_counts().max()

        categoria_texto = f"En la variable **{col}**, la categoría más frecuente es **{top_cat}**, con **{top_freq} registros**, lo que indica que este grupo representa una proporción importante del dataset."

    st.divider()

    # =====================================================
    # Interpretación general del análisis
    # =====================================================

    st.markdown("## 🔎 Interpretación general del análisis")

    st.markdown(f"""
Durante el análisis exploratorio se pudieron identificar **patrones relevantes en los datos**, tanto en variables numéricas como categóricas.

🔗 **Relaciones entre variables**  
{correlacion_texto}

📈 **Variabilidad en los datos**  
{variabilidad_texto}

🏷️ **Segmentación de clientes**  
{categoria_texto}

📉 Las visualizaciones utilizadas durante el EDA, como **histogramas, boxplots y matrices de correlación**, permitieron identificar **tendencias, dispersión de valores y diferencias entre grupos**, lo cual facilita comprender mejor la estructura del dataset.
""")

    st.divider()

    # =====================================================
    # 5 CONCLUSIONES CLARAS DEL PROYECTO
    # =====================================================

    st.markdown("## 🧾 Conclusiones finales del proyecto")

    st.markdown(f"""
### 1️⃣ Comprensión de la estructura de los datos
El dataset analizado contiene **{total_registros} registros y {total_variables} variables**, con **{valores_faltantes} valores faltantes**, lo que indica que la base de datos presenta una **estructura adecuada para realizar análisis exploratorios confiables**.

### 2️⃣ Identificación de relaciones entre variables
El análisis de correlación permitió detectar que **{correlacion_texto.lower()}**, lo que sugiere que ciertas variables pueden estar asociadas entre sí dentro del contexto del análisis de datos de clientes y seguros.

### 3️⃣ Variabilidad en variables clave del dataset
El estudio de la dispersión de los datos mostró que **{variabilidad_texto.lower()}**, lo que indica que existen **diferencias significativas entre los registros** analizados.

### 4️⃣ Segmentación de clientes mediante variables categóricas
El análisis de variables categóricas permitió identificar que **{categoria_texto.lower()}**, lo que facilita reconocer **segmentos predominantes de clientes dentro del dataset**.

### 5️⃣ Utilidad del análisis para la toma de decisiones
En conjunto, el análisis exploratorio permitió **identificar patrones, tendencias y relaciones relevantes dentro de los datos**, lo que puede servir como base para **apoyar la toma de decisiones estratégicas relacionadas con la gestión de clientes, segmentación de mercado y análisis de productos de seguros**.
""")

    st.divider()

    st.success(
        "✅ El análisis exploratorio permitió transformar los datos en información útil para comprender el comportamiento de los clientes y apoyar la toma de decisiones basada en datos."
    )