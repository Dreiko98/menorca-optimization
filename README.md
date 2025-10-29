# Menorca Optimization

## Descripción

Este proyecto implementa un modelo de optimización para la conservación de hábitats en Menorca, combinando análisis espacial y técnicas de investigación operativa.

## Estructura del Proyecto

```
menorca-optimization/
│
├── data/
│   ├── dataset.geojson        # Datos geoespaciales
│
├── notebooks/
│   ├── session1_exploration.ipynb   # Exploración de datos
│
├── src/
│   ├── utils.py                # Funciones auxiliares
│   ├── model_habitat.py        # Modelo de optimización
│
├── paper/
│   ├── ieee_template.tex       # Plantilla IEEE
│   ├── figures/                # Figuras del paper
│   └── references.bib          # Referencias bibliográficas
│
├── README.md                   # Este archivo
├── requirements.txt            # Dependencias
└── LICENSE                     # Licencia MIT
```

## Requisitos

- Python 3.8+
- GeoPandas
- Pyomo u ORTools (para optimización)
- Jupyter Notebook

## Instalación

1. Clona el repositorio
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Coloca los datos GeoJSON en `data/`
2. Abre `notebooks/session1_exploration.ipynb` para explorar
3. Ejecuta el modelo de optimización desde `src/model_habitat.py`

## Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias, contacta a [Tu Información]
