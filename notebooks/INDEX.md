# Menorca Optimization - Índice Completo del Proyecto

**Fecha de Actualización:** 29 de octubre de 2025  
**Versión del Proyecto:** 3.0 (Session 3 Completada)  
**Status:** ✅ Multi-session, Progresivo

---

## 📑 Navegación Rápida

### 🔰 Iniciar Aquí

1. **Nuevo en el proyecto?** → [Inicio Rápido](#inicio-rápido)
2. **¿Qué es esto?** → [Descripción General](#descripción-general)
3. **Quiero ver resultados** → [Resultados por Session](#resultados-por-session)
4. **Quiero ejecutar código** → [Instrucciones de Ejecución](#instrucciones-de-ejecución)

---

## Descripción General

### 🎯 Objetivo del Proyecto

Optimizar la adaptación de hábitats para especies en peligro de extinción en Menorca usando:
- **Session 1:** Exploración de datos (EDA)
- **Session 2:** Modelo Greedy baseline (v0)
- **Session 3:** Modelo MILP con conectividad (v1)
- **Session 4:** Análisis de sensibilidad (próximo)

### 🌍 Área de Estudio

**Isla de Menorca, España**
- Malla: 1,401 celdas de 100m×100m
- Especies: 4 endémicas en peligro
- Presupuesto: 500 unidades de coste normalizado

### 📊 Especies Conservadas

| Especie | Nombre Científico | Estado | Prioridad |
|---------|-------------------|--------|-----------|
| Atelerix | Atelerix algirus | Vulnerable | Media |
| Martes | Martes martes | En Peligro | Alta |
| Eliomys | Eliomys quercinus | Rara ⭐ | **Máxima** |
| Oryctolagus | Oryctolagus cuniculus | Común | Baja |

---

## Inicio Rápido

### ⏱️ 5 Minutos: Ver Resultados

```bash
# 1. Abrir archivos de visualización
open notebooks/session1/CONCLUSIONS.md
open notebooks/session2/SESSION2_COMPLETE_REPORT.md
open notebooks/SESSION3_REPORT.md

# 2. Ver imágenes
# Buscar archivos .png en notebooks/
# - optimization_results.png (Session 2)
# - session3_connectivity_results.png (Session 3)
```

### ⏱️ 30 Minutos: Ejecutar una Session

**Para Session 3 (Recomendado):**
```bash
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization
source .venv/bin/activate
jupyter notebook notebooks/session3_connectivity.ipynb
```

### ⏱️ 2 Horas: Ejecutar Todo

```bash
# Activar entorno
source .venv/bin/activate

# Ejecutar Session 1
papermill notebooks/session1/session1_exploration.ipynb \
    notebooks/session1/session1_executed.ipynb

# Ejecutar Session 2
papermill notebooks/session1/session2/session2_modeling.ipynb \
    notebooks/session1/session2/session2_executed.ipynb

# Ejecutar Session 3
papermill notebooks/session3_connectivity.ipynb \
    notebooks/session3_executed.ipynb
```

---

## 📁 Estructura de Archivos

```
menorca-optimization/
│
├── 📋 README.md                    # Descripción general
├── 📋 LICENSE                      # MIT License
├── 📋 requirements.txt             # Dependencias Python
│
├── 📂 data/                        # Datos
│   ├── dataset_processed.geojson  # Malla de 1,401 celdas (input)
│   ├── model_config_v0.json       # Configuración Session 2
│   ├── corridor_adjacency.csv     # Adyacencias espaciales (generado S3)
│   ├── adaptations_detailed.csv   # Resultado Session 2
│   ├── adaptations_detailed_v1.csv # Resultado Session 3
│   ├── corridors_selected.csv     # Corredores S3
│   ├── solution_metadata_v0.json  # Metadatos Session 2
│   └── solution_metadata_v1.json  # Metadatos Session 3
│
├── 📂 notebooks/                   # Notebooks Jupyter
│   ├── README_SESSION1.md         # Guía Session 1
│   ├── README_SESSION2.md         # Guía Session 2
│   ├── README_SESSION3.md         # Guía Session 3 ⭐
│   ├── INDEX.md                   # Este archivo
│   │
│   ├── 📂 session1/
│   │   ├── session1_exploration.ipynb     # Notebook EDA
│   │   ├── CONCLUSIONS.md                 # Conclusiones S1
│   │   ├── TECHNICAL_STATUS.md            # Estatus técnico S1
│   │   │
│   │   └── 📂 session2/
│   │       ├── session2_modeling.ipynb    # Notebook Greedy v0
│   │       ├── SESSION2_COMPLETE_REPORT.md
│   │       ├── README.md
│   │       ├── QUICKSTART.md
│   │       ├── optimization_results.png   # Visualización S2
│   │       └── NOTEBOOK_WITH_OUTPUTS.md
│   │
│   ├── session3_connectivity.ipynb        # Notebook MILP v1 ⭐
│   ├── SESSION3_REPORT.md                 # Reporte técnico S3
│   ├── README_SESSION3.md                 # Guía de uso S3
│   └── session3_connectivity_results.png  # Visualización S3
│
├── 📂 src/                         # Código fuente
│   ├── utils.py                   # Funciones GIS
│   └── model_habitat.py           # Clase de modelo
│
└── 📂 paper/                       # Documentación académica
    ├── ieee_template.tex          # Plantilla LaTeX
    └── references.bib             # Referencias BibTeX
```

---

## Resultados por Session

### 📊 Session 1: Exploración de Datos

**Archivo:** `notebooks/session1/session1_exploration.ipynb`

**Objetivo:** Cargar, validar y explorar dataset

**Resultados Clave:**
- ✅ 1,401 celdas cargadas
- ✅ 13 atributos por celda
- ✅ 100% datos válidos
- ✅ Coordenadas: EPSG:4326 (WGS84)
- ✅ 71 hábitats actuales detectados

**Documentación:**
- `CONCLUSIONS.md` - Resumen y hallazgos principales
- `TECHNICAL_STATUS.md` - Estatus técnico detallado

**Ver Resultados:** [CONCLUSIONS.md](session1/CONCLUSIONS.md)

---

### 🎯 Session 2: Modelo Baseline (v0 - Greedy)

**Archivo:** `notebooks/session1/session2/session2_modeling.ipynb`

**Objetivo:** Implementar heurística Greedy como baseline

**Resultados:**
- **Algoritmo:** Greedy por máxima eficiencia (peso/coste)
- **Objetivo:** 608.90
- **Presupuesto:** 499.80 / 500.0 (99.96%)
- **Adaptaciones:** 407 celdas
- **Corredores:** 0 (sin conectividad)
- **Tiempo:** 0.15 segundos

**Por Especie:**
| Especie | Adaptadas | Total |
|---------|-----------|-------|
| Atelerix | 69 | 93 |
| Martes | 94 | 105 |
| Eliomys | 217 | 237 ⭐ |
| Oryctolagus | 27 | 43 |

**Documentación:**
- `SESSION2_COMPLETE_REPORT.md` - Reporte técnico completo
- `README.md` - Descripción y metodología
- `QUICKSTART.md` - Guía rápida
- `NOTEBOOK_WITH_OUTPUTS.md` - Notebook con outputs visibles

**Visualización:** `optimization_results.png` (4 paneles, 682 KB)

**Ver Resultados:** [SESSION2_COMPLETE_REPORT.md](session1/session2/SESSION2_COMPLETE_REPORT.md)

---

### 🔗 Session 3: Modelo con Conectividad (v1 - MILP)

**Archivo:** `notebooks/session3_connectivity.ipynb` ⭐

**Objetivo:** Optimizar simultáneamente cobertura + conectividad

**Resultados:**
- **Algoritmo:** MILP exacto (HiGHS Solver)
- **Objetivo:** 625.45 (+2.72% vs v0)
- **Presupuesto:** 498.92 / 500.0 (99.78%)
- **Adaptaciones:** 412 celdas (+1.23% vs v0)
- **Corredores:** 187 (NEW!)
- **Conectividad:** 62.5% de celdas interconectadas
- **Tiempo:** 42.3 segundos (×282 más lento)
- **Optimalidad:** ✅ Certificada por solver

**Por Especie (S3):**
| Especie | Adaptadas | Corredores | Total |
|---------|-----------|-----------|-------|
| Atelerix | 71 | 28 | 95 |
| Martes | 96 | 42 | 107 |
| Eliomys | 220 | 101 | 240 ⭐ |
| Oryctolagus | 25 | 16 | 41 |

**Comparación v0 vs v1:**
```
Métrica          v0 (Greedy)    v1 (MILP)     Δ
─────────────────────────────────────────────────
Objetivo         608.90         625.45        +2.72%
Presupuesto      499.80         498.92        -0.18%
Adaptaciones     407            412           +1.23%
Corredores       0              187           +∞
Conectividad     0%             62.5%         +62.5pp
Tiempo (s)       0.15           42.3          ×282
```

**Documentación:**
- `SESSION3_REPORT.md` - Reporte técnico (formulación MILP)
- `README_SESSION3.md` - Guía de ejecución
- `session3_connectivity.ipynb` - Notebook completo con 13 secciones

**Visualización:** `session3_connectivity_results.png` (4 paneles, 850 KB)

**Archivos Generados:**
- `data/corridor_adjacency.csv` - Matriz de adyacencias (8,500 aristas)
- `data/adaptations_detailed_v1.csv` - 412 adaptaciones detalladas
- `data/corridors_selected.csv` - 187 corredores activados
- `data/solution_metadata_v1.json` - Metadatos completos

**Ver Resultados:** [SESSION3_REPORT.md](SESSION3_REPORT.md)

**Ejecutar:** [README_SESSION3.md](README_SESSION3.md)

---

### 🔜 Session 4: Análisis de Sensibilidad (PRÓXIMO)

**Objetivo:** Explorar impacto de parámetros

**Plan:**
- Variar λ (conectividad) ∈ [0.1, 0.3, 0.5]
- Variar B (presupuesto) ∈ [100, 250, 500, 750, 1000]
- Generar matriz 3×5 de soluciones
- Visualizar trade-offs objetivo vs conectividad vs presupuesto
- Identificar puntos óptimos por especie

**Entregables Esperados:**
- `session4_sensitivity_analysis.ipynb`
- `sensitivity_results.csv` (15 soluciones)
- `session4_sensitivity_plots.png` (heatmaps, curvas)
- `SESSION4_ANALYSIS.md` (interpretación)

---

## Instrucciones de Ejecución

### Prerequisitos

```bash
# Verificar Python
python --version  # Debe ser 3.12+

# Verificar dependencias
python -c "import pyomo, geopandas, pandas, numpy; print('✓ OK')"
```

### Opción 1: VS Code con Jupyter

```
1. Abrir: notebooks/session3_connectivity.ipynb
2. Seleccionar Kernel: Python 3.12.3 (.venv)
3. Run All Cells (Ctrl+Alt+Enter)
4. Esperar ~1 minuto
```

### Opción 2: Terminal con Papermill

```bash
cd menorca-optimization
source .venv/bin/activate

# Session 3
papermill notebooks/session3_connectivity.ipynb \
    notebooks/session3_connectivity_executed.ipynb

# Todos
for nb in notebooks/session1/session1_exploration.ipynb \
          notebooks/session1/session2/session2_modeling.ipynb \
          notebooks/session3_connectivity.ipynb; do
    papermill "$nb" "${nb%.ipynb}_executed.ipynb"
done
```

### Opción 3: Jupyter Lab (Interactivo)

```bash
source .venv/bin/activate
jupyter lab notebooks/
# Abrir notebook deseado y ejecutar
```

---

## 📈 Flujo del Proyecto

```
┌─────────────────────────────────────────────────────────┐
│ INPUT: dataset_processed.geojson (1,401 celdas)        │
│        Especie × hábitat, costes normalizados [0,1]   │
└──────────────────┬──────────────────────────────────────┘
                   │
        ┌──────────▼─────────────┐
        │   SESSION 1: EDA       │
        │ • Cargar y validar     │
        │ • Explorar atributos   │
        │ • Visualizar espacial  │
        └──────────┬─────────────┘
                   │
        ┌──────────▼──────────────┐
        │  SESSION 2: v0 GREEDY   │
        │ • Heurística pura       │
        │ • Sin conectividad      │
        │ • Objetivo: 608.90      │
        └──────────┬──────────────┘
                   │
        ┌──────────▼──────────────┐
        │  SESSION 3: v1 MILP ✅   │
        │ • Exacto (HiGHS)        │
        │ • +Conectividad         │
        │ • Objetivo: 625.45      │
        └──────────┬──────────────┘
                   │
        ┌──────────▼──────────────────┐
        │ SESSION 4: SENSIBILIDAD     │
        │ • Variar λ y B             │
        │ • Trade-off plots          │
        │ • Puntos óptimos           │
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │  PAPER IEEE + PRESENTACIÓN  │
        │  • Metodología              │
        │  • Resultados               │
        │  • Conclusiones             │
        └──────────────────────────────┘
```

---

## 🎓 Conceptos Clave

### Términos Usados

| Término | Definición | Ejemplo |
|---------|-----------|---------|
| **Celda** | Unidad de malla 100m×100m | grid_id = 1023 |
| **Hábitat** | Presencia de especie actualmente | h[i,s] ∈ {0,1} |
| **Adaptación** | Crear hábitat nuevo en celda | x[i,s] = 1 |
| **Corredor** | Conexión entre dos celdas | y[i,j,s] = 1 |
| **Presupuesto** | Recurso limitado | B = 500 |
| **Coste** | Inversión requerida | c[i,s] ∈ [0,1] |
| **Objetivo** | Valor a maximizar | Z = cobertura + λ·conectividad |

### Modelos Implementados

1. **v0 (Greedy Heuristic):**
   - Selecciona adaptaciones por máxima eficiencia
   - Rápido (0.15s) pero aproximado
   - No considera conectividad

2. **v1 (MILP Exacto):**
   - Formulación matemática rigurosa en Pyomo
   - Solver: HiGHS (garantiza optimalidad)
   - Incluye corredores con restricciones de integridad

3. **v2 (Futuro - Sensibilidad):**
   - Múltiples configuraciones de parámetros
   - Análisis de robustez

---

## 📊 Indicadores de Éxito

### Session 1: ✅ Completada
- [x] Dataset validado
- [x] EDA ejecutado
- [x] Visualizaciones generadas
- [x] Conclusiones documentadas

### Session 2: ✅ Completada
- [x] Modelo Greedy implementado
- [x] Solución encontrada
- [x] Visualizaciones (4 paneles)
- [x] Documentación técnica

### Session 3: ✅ Completada
- [x] Modelo MILP formulado
- [x] Solver HiGHS integrado
- [x] 187 corredores activados
- [x] Validación de optimalidad
- [x] Comparación v0 vs v1
- [x] Documentación completa

### Session 4: 🔄 En Planificación
- [ ] Matriz sensibilidad 3×5
- [ ] Análisis trade-offs
- [ ] Heatmaps generados
- [ ] Reporte final

---

## 🔗 Recursos Externos

### Documentación Técnica

- [Pyomo Optimization Modeling](https://pyomo.readthedocs.io/)
- [HiGHS Solver Documentation](https://www.maths.ed.ac.uk/~jspencer/highs/)
- [GeoPandas Spatial Analysis](https://geopandas.org/)

### Literatura Académica

- Margules & Pressey (2000) - Systematic Conservation Planning
- Snyder et al. (2015) - Conservation Planning with Optimization
- Taylor et al. (2006) - Landscape Connectivity Concepts

### Datos de Referencia

- Malla: 1,401 celdas × 4 especies
- Zona: Isla de Menorca, España
- Formato: GeoJSON (EPSG:4326)

---

## ❓ Preguntas Frecuentes

### ¿Por qué v1 da mejor objetivo si utiliza menos presupuesto?

R: Porque incluye conectividad en la función objetivo. Aunque presupuesto ≈ igual, el término λ·corredores incrementa el objetivo sin aumentar significativamente el coste de adaptación.

### ¿Qué significa "62.5% conectividad"?

R: El 62.5% de las celdas adaptadas están conectadas via corredores a otras celdas de la misma especie. El 37.5% restante son "islas" aisladas.

### ¿Puedo cambiar los pesos de especies?

R: Sí. En la Sección 4 del notebook v1, modifica el diccionario `weights`. Mayor peso = mayor inversión en esa especie.

### ¿Cuánto tiempo toma ejecutar Session 3?

R: ~1 minuto total (primavez compila solver). Luego ~30-40s por ejecución si cambias parámetros.

### ¿Qué pasa si bajo λ a 0?

R: Se ignora conectividad. La solución sería idéntica a v0 (Greedy).

---

## 📞 Contacto y Soporte

**Responsable del Proyecto:** GitHub Copilot  
**Última Actualización:** 29 de octubre de 2025  
**Versión:** 3.0

Para problemas:
1. Revisar `TECHNICAL_STATUS.md` de la Session correspondiente
2. Consultar logs de ejecución (stdout del notebook)
3. Verificar paths absolutos en terminales
4. Confirmar solver instalado: `python -c "from pyomo.environ import SolverFactory; SolverFactory('highs')"`

---

## 📋 Checklist de Ejecución

```bash
# Antes de ejecutar Session 3

□ Entorno activado:
  source .venv/bin/activate

□ Dependencias verificadas:
  pip list | grep "pyomo\|geopandas\|highs"

□ Datos presentes:
  ls -la data/dataset_processed.geojson
  ls -la data/model_config_v0.json

□ Notebook accesible:
  ls -la notebooks/session3_connectivity.ipynb

□ Directorio de salida disponible:
  mkdir -p data
  mkdir -p notebooks

□ Permisos de escritura:
  touch data/test.txt && rm data/test.txt
```

---

✅ **Proyecto en buen estado - Session 3 completada - Listo para Session 4**
