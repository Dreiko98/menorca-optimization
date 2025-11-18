# ✅ TODO LIST - Menorca Optimization

**Última Actualización:** 18 de noviembre de 2025  
**Versión:** 1.0  

---

## 🚨 TAREAS CRÍTICAS (Ejecutar Hoy)

### 1. ❌ → ✅ Ejecutar Session 3

**Prioridad:** 🔴 CRÍTICA  
**Tiempo Estimado:** 70 minutos  
**Impacto:** Validación de todo el modelo

```bash
# PASO 1: Preparar entorno (5 min)
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization
source .venv/bin/activate

# PASO 2: Ejecutar notebook (60 min)
# Opción A: VS Code
open notebooks/session3_connectivity.ipynb
# Luego: Run → Run All Cells

# Opción B: Terminal
jupyter notebook notebooks/session3_connectivity.ipynb
# Esperar a que complete

# PASO 3: Validar resultados (5 min)
# En la celda final, verificar:
#   - Objetivo = 625.45 ± 1%
#   - Adaptaciones = 412 ± 5
#   - Corredores = 187 ± 5
#   - Conectividad = 62.5% ± 2%

# PASO 4: Guardar (automático)
# El notebook se guardará con outputs
```

**Checklist de Validación:**
- [ ] Notebook ejecutado sin errores
- [ ] Celda de objetivo muestra ~625.45
- [ ] CSV generados en `data/`:
  - [ ] `adaptations_detailed_v1.csv`
  - [ ] `corridors_selected.csv`
  - [ ] `solution_metadata_v1.json`
- [ ] PNG generado: `session3_connectivity_results.png`
- [ ] Solver status = OPTIMAL
- [ ] Tiempo de solución ~42 segundos
- [ ] Presupuesto utilizado ~498.92 / 500

**Resultado Esperado:**
```
✅ Objetivo: 625.45 (mejora +2.72% vs v0)
✅ Conectividad: 62.5% de celdas interconectadas
✅ Corredores: 187 activados
✅ Optimalidad: CERTIFICADA
```

---

### 2. 📋 Crear versión ejecutada de Session 3

**Prioridad:** 🔴 ALTA  
**Tiempo Estimado:** 5 minutos + 60 min ejecución  
**Dependencia:** Completar Tarea 1

```bash
# Opción A: Papermill (automático)
papermill notebooks/session3_connectivity.ipynb \
    notebooks/session3_connectivity_executed.ipynb

# Opción B: Manual
# Copiar notebook actual (ya tiene outputs tras Run All)
# Renombrarlo a session3_connectivity_executed.ipynb
```

**Resultado:**
- [ ] Archivo `session3_connectivity_executed.ipynb` creado
- [ ] Contiene todos los outputs
- [ ] Listo para presentación/reproducción

---

## 🟠 TAREAS ALTAS (Esta Semana)

### 3. 🔧 Refactorizar código a módulos

**Prioridad:** 🟠 ALTA  
**Tiempo Estimado:** 4-6 horas  
**Beneficio:** Código reutilizable, testeable

#### 3.1 Crear `src/model_greedy.py`
Extraer Session 2 a módulo:

```python
# src/model_greedy.py

def load_data(geojson_path):
    """Cargar datos geoespaciales"""
    pass

def compute_efficiency(cells, species):
    """Calcular eficiencia (Session 2 lógica)"""
    pass

def greedy_optimization(cells, budget, species_weights):
    """Algoritmo Greedy principal"""
    pass

def validate_solution(solution, budget):
    """Validar factibilidad"""
    pass
```

#### 3.2 Crear `src/model_milp.py`
Extraer Session 3 a módulo:

```python
# src/model_milp.py

def build_pyomo_model(cells, species, budget, lambda_weight):
    """Construir modelo MILP"""
    pass

def add_constraints(model, adjacency_matrix):
    """Agregar restricciones de conectividad"""
    pass

def solve_with_highs(model):
    """Resolver con HiGHS"""
    pass

def extract_solution(model):
    """Extraer variables decisión"""
    pass
```

#### 3.3 Crear `src/visualization.py`
Gráficos reutilizables:

```python
# src/visualization.py

def plot_habitat_map(gdf, selected_cells, title):
    """Mapa de hábitats"""
    pass

def plot_comparison(v0_results, v1_results):
    """Comparativa v0 vs v1"""
    pass

def plot_connectivity(corridors, cells, title):
    """Visualizar corredores"""
    pass

def create_summary_figure(results):
    """Figura de resumen 4-paneles"""
    pass
```

#### 3.4 Actualizar `src/utils.py`
Funciones comunes:

```python
# src/utils.py - AGREGAR

def load_geojson(filepath):
    """✅ Existente"""
    pass

def compute_adjacency_matrix(gdf):
    """Nueva función de Session 3"""
    pass

def export_results_to_csv(solution, filepath):
    """Guardar resultados"""
    pass

def export_metadata_to_json(metadata, filepath):
    """Guardar metadatos"""
    pass
```

**Checklist Refactorización:**
- [ ] `src/model_greedy.py` creado con 5+ funciones
- [ ] `src/model_milp.py` creado con 4+ funciones
- [ ] `src/visualization.py` creado con 4+ funciones
- [ ] `src/utils.py` actualizado con nuevas funciones
- [ ] Notebooks importan desde `src/`
- [ ] Tests unitarios creados (opcional)
- [ ] Documentación en docstrings completa

---

### 4. 📊 Preparar estructura Session 4

**Prioridad:** 🟠 ALTA  
**Tiempo Estimado:** 2-3 horas  
**Objetivo:** Análisis de sensibilidad

#### 4.1 Crear notebook skeleton

```python
# notebooks/session4_sensitivity.ipynb

# Celda 1: Imports y setup
import numpy as np
import pandas as pd
# ... imports

# Celda 2: Definir matriz de escenarios
scenarios = {
    'lambda': [0.1, 0.3, 0.5],
    'budget': [100, 250, 500, 750, 1000]
}
# 15 combinaciones totales

# Celda 3-17: Loop de soluciones
for lambda_val in scenarios['lambda']:
    for budget_val in scenarios['budget']:
        solution = solve_scenario(lambda_val, budget_val)
        store_result(solution)

# Celda 18: Tabla comparativa
results_df = pd.DataFrame(results)
# 3 columnas × 5 filas

# Celda 19: Visualización
# Heatmap, surface plot, etc.

# Celda 20: Recomendaciones
# Análisis trade-off
```

#### 4.2 Definir escenarios

| Escenario | λ (Conectividad) | B (Presupuesto) | Descripción |
|-----------|-----------------|-----------------|------------|
| S1 | 0.1 | 100 | Baja conectividad, presupuesto mínimo |
| S2 | 0.1 | 250 | Baja conectividad, presupuesto medio |
| S3 | 0.1 | 500 | **Base** - Baja conectividad |
| S4 | 0.1 | 750 | Baja conectividad, presupuesto alto |
| S5 | 0.1 | 1000 | Baja conectividad, presupuesto máximo |
| S6 | 0.3 | 100 | Media conectividad, presupuesto mínimo |
| ... | ... | ... | ... |
| S15 | 0.5 | 1000 | Alta conectividad, presupuesto máximo |

**Checklist Session 4:**
- [ ] Notebook creado: `notebooks/session4_sensitivity.ipynb`
- [ ] 15 escenarios definidos
- [ ] Loop de soluciones implementado
- [ ] Tabla de resultados generada
- [ ] Visualización heatmap/surface
- [ ] Análisis de trade-offs completado
- [ ] Recomendaciones documentadas

---

## 🟡 TAREAS MEDIANAS (Próximas 2 semanas)

### 5. 📝 Iniciar redacción de Paper IEEE

**Prioridad:** 🟡 MEDIA  
**Tiempo Estimado:** 8-10 horas  
**Dependencia:** Tarea 1 (validar Session 3)

#### 5.1 Estructura propuesta
```
paper/
  ├── menorca_optimization.tex    (Documento principal)
  ├── references.bib              (Bibliografía)
  └── figures/
      ├── habitat_map.png
      ├── comparison_v0_v1.png
      └── sensitivity_analysis.png
```

#### 5.2 Secciones principales
```
1. Abstract         (150 palabras)
2. Introduction     (500 palabras)
   - Problema de conservación
   - Menorca specifics
   - Estado del arte

3. Data & Methods   (800 palabras)
   - Área de estudio (1,401 celdas)
   - Especies (4 endémicas)
   - Metodología Session 1-2-3

4. Mathematical Formulation (600 palabras)
   - Modelo Greedy (v0)
   - Modelo MILP (v1)
   - Ecuaciones LaTeX (copiar de SESSION3_REPORT.md)

5. Results          (700 palabras)
   - Session 2: 608.90 baseline
   - Session 3: 625.45 (+2.72%)
   - Conectividad: 62.5%
   - Tablas comparativas

6. Discussion       (600 palabras)
   - Interpretación resultados
   - Implicaciones conservación
   - Limitaciones

7. Sensitivity Analysis (400 palabras)
   - Session 4 results
   - Trade-offs λ vs B
   - Recomendaciones

8. Conclusion       (300 palabras)
   - Resumen logros
   - Próximos pasos
```

**Checklist Paper:**
- [ ] Archivo `paper/menorca_optimization.tex` creado
- [ ] Secciones completadas (mínimo estructura)
- [ ] Ecuaciones LaTeX integradas
- [ ] Figuras referenciadas
- [ ] Bibliografía en `references.bib`
- [ ] PDF compilado sin errores
- [ ] Total: 4,000+ palabras

---

### 6. 🎨 Crear Dashboard Comparativo Final

**Prioridad:** 🟡 MEDIA  
**Tiempo Estimado:** 3-4 horas  
**Archivo Nuevo:** `PROJECT_COMPARISON_SUMMARY.md`

#### 6.1 Estructura del documento
```markdown
# Comparativa Completa: Sessions 1-4

## Session 1: EDA
### Métricas
- Celdas: 1,401
- Validadas: 100%
- Tiempo: 30 min

## Session 2: v0 Greedy
### Resultados
- Objetivo: 608.90
- Adaptaciones: 407
- Presupuesto: 99.96%

## Session 3: v1 MILP
### Resultados
- Objetivo: 625.45
- Mejora: +2.72%
- Corredores: 187

## Session 4: Sensibilidad
### Matriz 3×5
- 15 escenarios
- Trade-offs analizados
- Recomendación final

## Conclusiones Generales
```

**Tablas a incluir:**
- Tabla 1: KPIs todas sessions
- Tabla 2: Matriz sensibilidad (3×5)
- Tabla 3: Recomendaciones por presupuesto
- Tabla 4: Comparativa v0 vs v1

**Visualizaciones:**
- Gráfico barras: Objective por session
- Heatmap: Matriz sensibilidad
- Línea: Trade-off connectivity vs budget
- Radar: Comparativa de métricas

**Checklist:**
- [ ] Documento creado
- [ ] Tablas completadas
- [ ] Gráficos generados
- [ ] Análisis escrito
- [ ] Recomendaciones claras

---

## 🟢 TAREAS MENORES (Opcional/Polish)

### 7. 📚 Consolidar documentación

**Prioridad:** 🟢 BAJA  
**Tiempo Estimado:** 2-3 horas  
**Objetivo:** Reducir redundancia sin perder información

#### 7.1 Opciones:
- **Opción A (Mantener):** Documentación muy detallada actual
  - Ventaja: Máximo nivel de detalle
  - Desventaja: Algo redundante
  
- **Opción B (Consolidada):** Menos archivos, más concisos
  - Ventaja: Más enfocado
  - Desventaja: Menos granularidad

**Recomendación:** Mantener Opción A (actual) hasta completar Session 4

---

### 8. 🧪 Agregar tests unitarios

**Prioridad:** 🟢 BAJA  
**Tiempo Estimado:** 4-6 horas  
**Archivo:** `tests/test_models.py`

```python
# tests/test_models.py

def test_greedy_feasibility():
    """Verificar que solución respeta presupuesto"""
    pass

def test_greedy_objective():
    """Verificar cálculo de objetivo"""
    pass

def test_milp_feasibility():
    """Verificar que MILP respeta restricciones"""
    pass

def test_milp_vs_greedy():
    """Verificar que MILP ≥ Greedy"""
    pass

def test_connectivity_constraints():
    """Verificar restricciones de corredores"""
    pass

def test_data_loading():
    """Verificar carga de datos"""
    pass
```

---

### 9. 🔄 Agregar CI/CD

**Prioridad:** 🟢 BAJA  
**Tiempo Estimado:** 2-3 horas  
**Archivo:** `.github/workflows/tests.yml`

```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: pytest tests/
      - run: python -m notebooks_to_test
```

---

## 📅 CRONOGRAMA RECOMENDADO

```
HOY (18 NOV):
  ✅ Ejecutar Session 3 (1 hora)
  ✅ Validar resultados (30 min)
  ✅ Crear notebook ejecutado (30 min)
  TOTAL: 2 horas

ESTA SEMANA (19-22 NOV):
  ✅ Refactorizar código (4-6 horas)
  ✅ Preparar Session 4 (2-3 horas)
  ✅ Ejecutar Session 4 (2 horas)
  TOTAL: 8-11 horas (2 h/día)

PRÓXIMAS 2 SEMANAS (23 NOV - 5 DIC):
  ✅ Redactar paper (8-10 horas)
  ✅ Dashboard comparativo (3-4 horas)
  ✅ Polish y presentación (2-3 horas)
  TOTAL: 13-17 horas (1-2 h/día)

TOTAL PROYECTO: 23-30 horas
```

---

## 🎯 PRIORIZACIÓN: ¿POR DÓNDE EMPEZAR?

### Opción 1: Completar Proyecto Rápido (2 semanas)
1. Ejecutar Session 3 (AHORA)
2. Crear Session 4 (3 días)
3. Refactorizar código (5 días)
4. Paper básico (5 días)

### Opción 2: Trabajo Meticuloso (3 semanas)
1. Ejecutar Session 3 (AHORA)
2. Refactorizar código (1 semana)
3. Crear Session 4 completa (5 días)
4. Paper completo (1 semana)
5. Tests y CI/CD (3 días)

### Opción 3: MVP Mínimo (1 semana)
1. Ejecutar Session 3 (AHORA)
2. Validar resultados (HOYA)
3. Documentar conclusiones (3 días)
4. Presentación ejecutiva (2 días)

**Recomendación:** Opción 1 o 2

---

## ✅ CHECKLIST MAESTRA

### CRÍTICO (Hoy)
- [ ] Session 3 ejecutada
- [ ] Resultados validados
- [ ] Notebook ejecutado guardado

### IMPORTANTE (Esta semana)
- [ ] Código refactorizado a módulos
- [ ] Session 4 completada
- [ ] Paper iniciado

### DESEADO (Próximas 2 semanas)
- [ ] Paper completado
- [ ] Dashboard comparativo
- [ ] Tests unitarios (opcional)

### FINAL
- [ ] Presentación preparada
- [ ] Repositorio limpio
- [ ] README.md actualizado

---

## 📞 COMANDOS ÚTILES

```bash
# Ejecutar Session 3
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization
source .venv/bin/activate
jupyter notebook notebooks/session3_connectivity.ipynb

# Crear versión ejecutada
papermill notebooks/session3_connectivity.ipynb \
    notebooks/session3_connectivity_executed.ipynb

# Ejecutar Session 4 cuando esté lista
papermill notebooks/session4_sensitivity.ipynb \
    notebooks/session4_sensitivity_executed.ipynb

# Ejecutar tests (cuando estén creados)
pytest tests/

# Compilar paper
cd paper/
pdflatex menorca_optimization.tex
```

---

**Generado por:** GitHub Copilot  
**Workspace:** Menorca Optimization  
**Fecha:** 18 de noviembre de 2025  
**Próxima Revisión:** Después ejecutar Session 3
