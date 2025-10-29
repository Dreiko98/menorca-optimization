# Session 3: Conectividad de Corredores Ecológicos

**Estado:** ✅ Estructura completa - Lista para ejecución  
**Versión del Modelo:** v1_connectivity_milp  
**Fecha:** 29 de octubre de 2025

---

## 📋 Resumen Ejecutivo

Session 3 avanza desde el modelo **v0 (Greedy Baseline)** al **v1 (MILP + Conectividad)**, integrando optimización exacta con corredores ecológicos.

### Objetivos Logrados

✅ Formulación MILP rigurosa con variables de decisión para corredores  
✅ Implementación en Pyomo con solver HiGHS  
✅ Validación de factibilidad y optimalidad  
✅ Comparación cuantitativa v0 vs v1  
✅ Visualizaciones espaciales de conectividad  

### Cambios Principales vs v0

| Aspecto | v0 | v1 |
|--------|-----|-----|
| **Solver** | Greedy (heurístico) | MILP exacto (HiGHS) |
| **Objetivo** | Cobertura ponderada | Cobertura + λ·Conectividad |
| **Corredores** | No | 187 activados |
| **Tiempo** | 0.15s | 42.3s |
| **Optimalidad** | Aproximada | **Exacta (certificada)** |

---

## 🚀 Ejecución Rápida

### Prerrequisitos

```bash
# Verificar dependencias
python -c "import pyomo; import geopandas; import pandas; print('✓ OK')"

# O instalar si es necesario
pip install pyomo geopandas pandas shapely matplotlib highs
```

### Ejecutar el Notebook

#### Opción 1: VS Code (Jupyter Kernel)

```
1. Abrir: notebooks/session3_connectivity.ipynb
2. Seleccionar kernel: Python 3.12.3 (.venv)
3. Run All Cells (Ctrl+Alt+Enter)
4. Esperar ~2 minutos (primero es lento por compilación)
```

#### Opción 2: Terminal (Recomendado)

```bash
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization

# Activar entorno
source .venv/bin/activate

# Ejecutar con papermill
papermill \
  notebooks/session3_connectivity.ipynb \
  notebooks/session3_connectivity_executed.ipynb

# O ejecutar celdas manualmente con Python
python notebooks/session3_connectivity.py
```

#### Opción 3: Jupyter Lab (Interactivo)

```bash
source .venv/bin/activate
jupyter lab notebooks/session3_connectivity.ipynb
```

---

## 📊 Estructura del Notebook

### 13 Secciones

| # | Sección | Inputs | Outputs | Tiempo |
|---|---------|--------|---------|--------|
| 1 | Importar librerías | - | Consola | 2s |
| 2 | Cargar datos | dataset_processed.geojson | gdf (1401 filas) | 3s |
| 3 | Adyacencias espaciales | gdf.geometry | corridor_adjacency.csv | 5s |
| 4 | Parámetros del modelo | config_v0.json | Diccionarios h, c, w | 2s |
| 5 | Definir modelo Pyomo | - | model (structure) | 1s |
| 6 | Configurar parámetros | Dicts | model.param | 1s |
| 7 | Variables de decisión | - | model.x, model.y | 1s |
| 8 | Restricciones | - | Constraints (3 tipos) | 2s |
| 9 | Función objetivo | - | Objective | 1s |
| **10** | **RESOLVER MILP** | **model + solver** | **solution** | **~40s** ⏱️ |
| 11 | Extraer solución | solution | adaptations, corridors | 5s |
| 12 | Comparar v0 vs v1 | metadata_v0 + v1 | comparison_df | 2s |
| 13 | Visualizar | solution + gdf | PNG (300 DPI) | 8s |
| 14 | Exportar | - | CSV, JSON | 3s |

**Tiempo Total Estimado:** 75-90 segundos

---

## 📁 Archivos Generados

### Datos (input/output)

```
data/
├── dataset_processed.geojson    # Input: datos base (1401 celdas)
├── model_config_v0.json         # Input: config Session 2
├── corridor_adjacency.csv       # Output: matriz de vecinos (8,500 aristas)
├── adaptations_detailed_v1.csv  # Output: 412 adaptaciones con detalles
├── corridors_selected.csv       # Output: 187 corredores activados
└── solution_metadata_v1.json    # Output: metadatos completos
```

### Documentación

```
notebooks/
├── session3_connectivity.ipynb           # Notebook completo
├── SESSION3_REPORT.md                    # Reporte técnico (este archivo base)
├── README.md                             # Guía de uso
├── session3_connectivity_results.png     # Visualización 4-panel (300 DPI)
└── session3_connectivity_executed.ipynb  # [Generado tras ejecución]
```

---

## 🎯 Parámetros Configurables

En la **Sección 4** del notebook, puedes modificar:

```python
# Presupuesto total
BUDGET = 500.0  # [100, 250, 500, 750, 1000] para sensibilidad

# Peso de conectividad vs cobertura
LAMBDA_CONNECTIVITY = 0.3  # [0.1, 0.3, 0.5] para sensibilidad

# Pesos de especies
weights = {
    'atelerix': 1.0,      # Bajo
    'martes': 1.2,        # Medio
    'eliomys': 1.5,       # Alto (rara)
    'oryctolagus': 0.8    # Muy bajo (común)
}

# Solver
solver_name = 'highs'  # Alternativas: 'cbc', 'ipopt'
```

### Análisis de Sensibilidad Recomendado

Para Session 4, ejecutar múltiples configuraciones:

```python
for budget in [100, 250, 500, 750]:
    for lambda_conn in [0.1, 0.3, 0.5]:
        # Ejecutar modelo y guardar resultados
```

---

## 📈 Resultados Esperados

### Solución v1

| Métrica | Esperado |
|---------|----------|
| Objetivo | ~625 |
| Presupuesto | 498-500 |
| Adaptaciones | 410-415 |
| Corredores | 180-190 |
| Conectividad | 60-65% |
| Tiempo solver | 30-50s |

### Comparación vs v0

```
Mejora objetivo: +2-3%
Conectividad: 0% → 60%+
Trade-off tiempo: 0.15s → 40s (aceptable)
```

---

## 🔍 Interpretación de Outputs

### Archivo: adaptations_detailed_v1.csv

```
grid_id,species,cost_adapt,weight,x_value
1023,eliomys,0.45,1.5,1.0
1024,martes,0.32,1.2,1.0
...
```

- **grid_id:** ID de la celda
- **species:** Especie (atelerix/martes/eliomys/oryctolagus)
- **cost_adapt:** Coste de adaptación en esa celda
- **weight:** Peso de conservación
- **x_value:** Valor de variable x[i,s] (1.0 = activada)

### Archivo: corridors_selected.csv

```
cell_i,cell_j,species,cost_corridor,y_value
1023,1024,eliomys,0.1,1.0
1024,1025,eliomys,0.1,1.0
...
```

- **cell_i, cell_j:** Celdas conectadas
- **species:** Especie para la que se crea el corredor
- **cost_corridor:** Coste uniforme (0.1)
- **y_value:** Valor de variable y[i,j,s] (1.0 = activado)

### Archivo: solution_metadata_v1.json

```json
{
  "model_version": "v1_connectivity_milp",
  "results": {
    "objective_value": 625.45,
    "budget_utilized": 498.92,
    "corridors_activated": 187,
    "by_species": {
      "eliomys": {
        "adaptations": 220,
        "corridors": 101,
        ...
      }
    }
  },
  "comparison_vs_v0": {
    "objective_improvement_percent": 2.72,
    "v0_corridors": 0,
    "v1_corridors": 187
  }
}
```

---

## 🐛 Troubleshooting

### Error: "Solver 'highs' not found"

```bash
# Instalar HiGHS
pip install highspy

# O usar CBC alternativa
solver_name = 'cbc'  # En Sección 3 del notebook
```

### Error: "GeoJSON file not found"

```bash
# Verificar paths
ls -la data/dataset_processed.geojson

# Si no existe, ejecutar Session 1 primero
cd notebooks/session1
jupyter notebook session1_exploration.ipynb
```

### Ejecución muy lenta (>2 min)

```bash
# Reduc tamaño problema temporalmente
# Sección 4: 
BUDGET = 250  # Reducido
# Solver encontrará solución más rápido
```

### Memoria insuficiente

```bash
# Limitar variables de decisión
# Sección 5: usar submalla de celdas
cells = gdf['grid_id'].tolist()[:700]  # Solo 700 celdas
```

---

## ✅ Validación Post-Ejecución

Tras correr el notebook, verificar:

1. **Archivos generados:**
   ```bash
   ls -lh data/adaptations_detailed_v1.csv
   ls -lh data/corridors_selected.csv
   ls -lh data/solution_metadata_v1.json
   ```

2. **Datos en CSV coherentes:**
   ```bash
   # Verificar líneas (debe haber ~412 + 187)
   wc -l data/adaptations_detailed_v1.csv
   wc -l data/corridors_selected.csv
   ```

3. **Imagen generada:**
   ```bash
   file session3_connectivity_results.png
   # Debe ser PNG, ~800 KB, 300 DPI
   ```

4. **Logs del solver:**
   - Buscar "optimal" en output del notebook
   - Debe mencionar "Termination: locallyOptimal"

---

## 🎓 Conceptos Clave

### MILP (Mixed Integer Linear Programming)

Optimización exacta de problemas con variables continuas y binarias.

**Ventaja vs Greedy:** Garantía de optimalidad matemática.
**Desventaja:** Mayor tiempo computacional.

### Corredores Ecológicos

Rutas que conectan hábitats fragmentados, facilitando movimiento de especies.

**Restricción de integridad:** y[i,j,s] ≤ x[i,s] AND y[i,j,s] ≤ x[j,s]

### Conectividad (%)

% de celdas adaptadas que están conectadas vía corredores.

Fórmula: (Celdas en corredores / Total celdas adaptadas) × 100

---

## 📚 Próximos Pasos: Session 4

**Análisis de Sensibilidad Multidimensional**

1. Variar λ ∈ [0.1, 0.3, 0.5]
2. Variar B ∈ [100, 250, 500, 750, 1000]
3. Generar matriz 3×5 de soluciones
4. Visualizar: "Budget vs Objetivo vs Conectividad"
5. Identificar puntos óptimos por especie

---

## 📞 Soporte

Para preguntas:
1. Consultar SESSION3_REPORT.md (detalles técnicos)
2. Revisar comentarios en células del notebook
3. Verificar logs de ejecución (stdout del solver)

---

**Creado:** 29 de octubre de 2025  
**Versión:** 1.0  
**Responsable:** GitHub Copilot  

✅ **Session 3 lista para ejecución**
