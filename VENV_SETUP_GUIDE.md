# 🔧 Virtual Environment Setup - Guía de Uso

**Fecha:** 18 de noviembre de 2025  
**Estado:** ✅ COMPLETADO Y VERIFICADO

---

## ✅ Qué se hizo

1. ✅ Creado virtual environment (`.venv`)
2. ✅ Instaladas todas las dependencias de `requirements.txt`
3. ✅ Instaladas librerías adicionales útiles (PuLP, scikit-learn)
4. ✅ Verificado que todos los imports funcionan correctamente

---

## 📦 Librerías Instaladas

### Análisis de Datos
- **pandas** - Manipulación de datos tabulares
- **numpy** - Cálculos numéricos
- **scipy** - Computación científica

### Datos Geoespaciales
- **geopandas** - Datos vectoriales geográficos
- **shapely** - Geometría espacial y operaciones
- **pyproj** - Proyecciones geográficas
- **pyogrio** - Lectura/escritura de formatos GIS

### Visualización
- **matplotlib** - Gráficos estáticos (publicación)
- **plotly** - Gráficos interactivos
- **folium** - Mapas interactivos con Leaflet

### Optimización
- **pyomo** - Modelado de optimización (MILP, LP)
- **pulp** - Programación lineal con solvers integrados (CBC)

### Machine Learning
- **scikit-learn** - Clustering (K-Means), preprocesamiento

### Notebooks
- **jupyter** - Interfaz de notebooks
- **ipykernel** - Kernel Python para Jupyter
- **jupyterlab** - IDE avanzado para notebooks
- **ipywidgets** - Widgets interactivos

### Otras
- **requests** - Cliente HTTP
- **plotly** - Visualización
- **ortools** - Herramientas de optimización de Google

---

## 🚀 Cómo Usar

### Activar Virtual Environment

```bash
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization
source .venv/bin/activate
```

Verificarás que está activo cuando la terminal muestre `(.venv)` al inicio de la línea.

### Desactivar Virtual Environment

```bash
deactivate
```

---

## 🎯 Usando Jupyter Notebooks

Con el venv **activado**:

```bash
# Opción 1: Jupyter Notebook (interfaz clásica)
jupyter notebook

# Opción 2: JupyterLab (interfaz moderna)
jupyter lab
```

Luego abre:
- Session 2: `notebooks/session2/session2_modeling_executed.ipynb`
- Session 3: `notebooks/session3_connectivity.ipynb`

---

## 📊 Verificación

Para verificar que todo está instalado correctamente:

```bash
source .venv/bin/activate
python3 -c "import pandas, geopandas, pyomo, pulp, sklearn; print('✅ Todas las librerías importan correctamente')"
```

---

## 📁 Ubicación del venv

```
/home/ayuda137/Escritorio/asuntos internos/menorca-optimization/
└── .venv/
    ├── bin/
    │   ├── python3
    │   ├── pip
    │   ├── jupyter
    │   └── ...
    ├── lib/
    │   └── python3.12/site-packages/  (todas las librerías)
    └── ...
```

---

## 🔧 Si Necesitas Instalar Otra Librería

Con el venv **activado**:

```bash
pip install nombre-de-libreria
```

Para guardar las nuevas dependencias:

```bash
pip freeze > requirements.txt
```

---

## ⚠️ Posibles Problemas

### El venv no se activa
Intenta:
```bash
bash
source .venv/bin/activate
```

### Jupyter no encuentra el kernel
Instala el kernel de nuevo:
```bash
source .venv/bin/activate
python3 -m ipykernel install --user --name menorca --display-name "Python (Menorca)"
```

### ImportError en alguna librería
Reinstala todo desde cero:
```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ✨ Resumen

```
✅ Virtual environment creado: .venv/
✅ Python 3.12.3 activo
✅ Todas las librerías instaladas
✅ Imports verificados
✅ Listo para Session 2 y Session 3
```

---

**Próximos pasos:**

1. Activar venv: `source .venv/bin/activate`
2. Ejecutar Session 2: `jupyter notebook notebooks/session2/session2_modeling_executed.ipynb`
3. Ejecutar Session 3: `jupyter notebook notebooks/session3_connectivity.ipynb`

---

Preparado por: GitHub Copilot  
Fecha: 18 de noviembre de 2025

