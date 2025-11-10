# Housing Price Prediction

Build and evaluate a regression model that predicts home prices from a real data set.
  
## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, eg.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    ├── requirements.txt   <- The pip requirements file for reproducing the environment.
    │
    ├── test               <- Unit and integration tests for the project.
    │   ├── __init__.py
    │   └── test_model.py  <- Example of a test script.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so housing_price_prediction can be imported.
    │
    └── housing_price_prediction   <- Source code for use in this project.
        │
        ├── __init__.py             <- Makes housing_price_prediction a Python module.
        │
        ├── config.py               <- Store useful variables and configuration.
        │
        ├── dataset.py              <- Scripts to download or generate data.
        │
        ├── features.py             <- Code to create features for modeling.
        │
        ├── modeling                
        │   ├── __init__.py 
        │   ├── predict.py          <- Code to run model inference with trained models.
        │   └── train.py            <- Code to train models.
        │
        ├── utils                   <- Scripts to help with common tasks.
        │   └── paths.py            <- Helper functions for relative file referencing across the project.        
        │
        └── plots.py                <- Code to create visualizations.

---
Project based on the [cookiecutter conda data science project template](https://github.com/jvelezmagic/cookiecutter-conda-data-science).

---

# 🏠 Predicción de Precios de Viviendas

**Proyecto de Aspirantes Pre-CIAP 2PAO 2025 Grupo2**

## 📘 Objetivo del Proyecto

El objetivo principal de este proyecto es **construir y evaluar un modelo de regresión** que prediga el precio de una vivienda a partir de un conjunto de datos reales.
El enfoque no está en crear una herramienta comercial, sino en **documentar y comprender cada paso** del proceso de análisis, modelado y evaluación.

---

## 🧩 Descripción General

Se trabajará con un **dataset estándar**, como *Ames Housing* (disponible en Kaggle), el cual contiene distintos tipos de variables y problemas típicos del mundo real, como:

* Datos desordenados
* Valores faltantes
* Formatos inconsistentes

El trabajo incluye:

1. **Limpieza y preparación de los datos (preprocesamiento)**
2. **Aplicación de ingeniería de características**
3. **Entrenamiento de modelos de regresión** (desde uno simple hasta más avanzados)
4. **Evaluación del rendimiento** mediante métricas numéricas
5. **Interpretación de los resultados** y reflexión sobre su significado y limitaciones

> 💡 El entregable final será un **notebook reproducible** (Jupyter o Google Colab) que muestre, de forma clara y lógica, todas las etapas del proyecto.

---

## 🛠️ Herramientas y Recursos Gratuitos

| Categoría             | Herramientas                       |
| --------------------- | ---------------------------------- |
| **Lenguaje**          | Python                             |
| **Entorno**           | Jupyter Notebook / Google Colab    |
| **Análisis de Datos** | Pandas, NumPy                      |
| **Visualización**     | Matplotlib, Seaborn                |
| **Machine Learning**  | Scikit-learn                       |
| **Fuente de Datos**   | Kaggle (por ejemplo, Ames Housing) |

---

## 🧠 Habilidades que Desarrollarás
1. Análisis Exploratorio de Datos (EDA)
2. Limpieza de Datos
3. Ingeniería de Características
4. Fundamentos de Modelado
5. Evaluación de Modelos
6. Interpretación de Coeficientes
---

## 📦 Entregables

### 1. Notebook Final (`.ipynb`)

Debe ser **claro, funcional y ejecutable de principio a fin sin errores.**
Debe incluir:

* Carga, limpieza y preprocesamiento de datos.
* Análisis exploratorio con visualizaciones.
* Entrenamiento y evaluación de modelos.
* Explicaciones en celdas Markdown justificando cada decisión.

---

## ✅ Criterios de Evaluación

| Criterio                 | Descripción                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| **Reproducibilidad**     | El notebook debe ejecutarse sin errores y dar los mismos resultados. |
| **Documentación**        | Uso adecuado de celdas Markdown con explicaciones claras.            |
| **Calidad del Análisis** | Limpieza y EDA bien estructurados.                                   |
| **Modelado**             | Aplicación correcta de algoritmos y evaluación de métricas.          |
| **Reflexión Final**      | Interpretación y análisis crítico de los resultados.                 |

---

## 🌱 Filosofía del Proyecto

Este proyecto busca desarrollar **pensamiento crítico y capacidad analítica**, más allá del resultado numérico.
Un modelo “malo pero bien explicado” enseña más que un modelo “perfecto pero sin contexto”.

> “El objetivo no es predecir precios, sino aprender a pensar como un analista de datos.”

---

## 👥 Créditos y Agradecimientos

Proyecto desarrollado por aspirantes del **Programa Pre-CIAP**,
como parte del proceso de formación en análisis y ciencia de datos.
Inspirado en datasets y notebooks públicos de **Kaggle**.
