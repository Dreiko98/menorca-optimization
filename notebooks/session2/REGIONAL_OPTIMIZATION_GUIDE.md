# 🗺️ Guía de Optimización Regional - Session 2

## 🎯 Problema Resuelto

**Síntoma**: El kernel crasheaba al intentar resolver el modelo MILP con todas las celdas (1,401 × 4 especies = 5,604 variables).

**Causa**: Solver HiGHS incompatible con Windows + Jupyter, problemas de memoria en fase de presolve.

**Solución**: **Particionamiento espacial** (sugerencia de Pilar) - dividir Menorca en regiones y optimizar cada una independientemente.

---

## 🚀 Estrategia Implementada

### 1. Particionamiento Espacial

- **Algoritmo**: K-Means clustering en coordenadas geográficas
- **Número de regiones**: 8 (configurable)
- **Distribución**: ~175 celdas por región

### 2. Optimización Independiente

Cada región se resuelve como un **subproblema independiente**:
- Variables por región: ~700 (en vez de 5,604)
- Presupuesto proporcional al tamaño de la región
- Solver: GLPK (más estable que HiGHS en Windows)

### 3. Combinación de Soluciones

Las adaptaciones de todas las regiones se combinan al final:
- Objetivo total = suma de objetivos regionales
- Coste total = suma de costes regionales

---

## 📋 Orden de Ejecución

### Paso 1: Setup Inicial
```
Ejecuta celdas 1-4:
- Importaciones
- Carga de dataset
- Parámetros del modelo
- Funciones auxiliares
```

### Paso 2: Instalación de Dependencias
```
Ejecuta celda 5.1.1:
- Instala GLPK (solver estable)
- Instala scikit-learn (para K-Means)
```

### Paso 3: Particionamiento
```
Ejecuta celda 5.1.2:
- Divide Menorca en 8 regiones
- Asigna cada celda a una región
```

### Paso 4: Visualización (Opcional)
```
Ejecuta celda 5.1.3:
- Visualiza el mapa de regiones
- Verifica la distribución espacial
```

### Paso 5: Optimización 🔥
```
Ejecuta celda 5.2:
- Optimiza cada región secuencialmente
- Tiempo esperado: 40-120 segundos total
- Salida: adaptaciones por región
```

### Paso 6: Análisis y Guardado
```
Ejecuta celdas 6-8:
- Desglose por especie
- Visualización de resultados
- Guardado de archivos CSV/JSON
```

---

## 📊 Comparativa: Antes vs Ahora

| Aspecto | Monolítico (Antes) | Regional (Ahora) |
|---------|-------------------|------------------|
| **Variables** | 5,604 | ~700 por región |
| **Restricciones** | ~11,200 | ~1,400 por región |
| **Tiempo total** | >8 min (crash) | 40-120 seg ✅ |
| **Memoria pico** | Alta (crash) | Baja ✅ |
| **Estabilidad** | Crashea ❌ | Estable ✅ |
| **Solver** | HiGHS (incompatible) | GLPK ✅ |

---

## ⚙️ Parámetros Configurables

### Número de Regiones
```python
N_REGIONS = 8  # Ajusta según necesidad (4, 6, 8, 10...)
```

**Criterios para elegir N**:
- **N pequeño (4-6)**: Regiones grandes, más rápido, menos óptimo
- **N mediano (8)**: Balance entre velocidad y calidad ✅
- **N grande (12-16)**: Regiones pequeñas, más lento, más óptimo

### Presupuesto Total
```python
BUDGET = 500.0  # Ajusta según caso de estudio
```

El presupuesto se distribuye proporcionalmente:
```
budget_region_i = BUDGET × (n_celdas_region_i / n_celdas_total)
```

### Pesos por Especie
```python
weights = {
    'atelerix': 1.0,      # Erizo
    'martes': 1.2,        # Marta (alta prioridad)
    'eliomys': 1.5,       # Lirón (máxima prioridad)
    'oryctolagus': 0.8    # Conejo (baja prioridad)
}
```

### Umbrales de Idoneidad
```python
tau = {
    'atelerix': 0.2,      # Acepta terrenos con q >= 0.2
    'martes': 0.3,        # Más restrictivo
    'eliomys': 0.3,       
    'oryctolagus': 0.2
}
```

---

## 🎯 Resultados Esperados

### Archivos Generados

1. **`adaptations_detailed_v0.csv`**
   - Columnas: `grid_id`, `species`, `cost`, `region`
   - Una fila por cada adaptación planificada

2. **`solution_metadata_v0.json`**
   - Metadatos de la solución
   - Desglose por especie y región
   - Tiempo de ejecución, valor objetivo, etc.

### Métricas Típicas

- **Tiempo total**: 40-120 segundos
- **Adaptaciones totales**: 100-300 celdas
- **Coste utilizado**: 400-500 (cercano al presupuesto)
- **Valor objetivo**: 1,200-1,800 (depende de pesos)

---

## 🔧 Troubleshooting

### Problema: "No module named 'sklearn'"
**Solución**: Ejecuta celda 5.1.1 para instalar scikit-learn

### Problema: "Solver glpk not available"
**Solución**: 
```bash
# Opción 1: pip
pip install glpk

# Opción 2: conda
conda install -c conda-forge glpk
```

### Problema: "Timeout en alguna región"
**Solución**: Aumenta el número de regiones (N_REGIONS = 12 o 16)

### Problema: "Presupuesto no utilizado completamente"
**Causa**: Normal en optimización regional (cada región es independiente)
**Solución**: Ajusta pesos o reduce número de regiones

---

## 🧪 Validación de Resultados

### Chequeos Automáticos

El código valida:
- ✅ Presupuesto no excedido en cada región
- ✅ No hay doble adaptación (natural + adaptado)
- ✅ Solo se adapta en terrenos con idoneidad >= tau
- ✅ Todas las regiones se resuelven exitosamente

### Chequeos Manuales

Verifica que:
- Total de adaptaciones es razonable (100-300)
- Distribución por especie es coherente con pesos
- Regiones no tienen costes desproporcionados
- Cobertura por especie aumenta respecto a baseline

---

## 📈 Extensiones Futuras

### Session 3: Corredores Ecológicos

Aplicar la misma estrategia regional para incluir corredores:
- Cada región optimiza adaptaciones + corredores internos
- Corredores entre regiones se añaden en post-procesamiento

### Optimización Global Post-Regional

Opción avanzada:
1. Resolver regiones independientemente (calentamiento)
2. Usar soluciones regionales como "warm start"
3. Resolver modelo global con restricciones relajadas

---

## 👥 Créditos

- **Estrategia**: Sugerida por Pilar
- **Implementación**: GitHub Copilot + Germán
- **Algoritmo de clustering**: scikit-learn K-Means
- **Solver**: GLPK (GNU Linear Programming Kit)

---

## 📚 Referencias

- Pyomo Documentation: https://pyomo.readthedocs.io/
- GLPK: https://www.gnu.org/software/glpk/
- K-Means Clustering: https://scikit-learn.org/stable/modules/clustering.html#k-means

---

**Última actualización**: 13 de noviembre de 2025
