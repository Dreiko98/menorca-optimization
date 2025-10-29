# ⚡ Inicio Rápido: Session 3 en 5 Minutos

**Objetivo:** Ejecutar el modelo de conectividad (v1 MILP) en Menorca

---

## 🚀 Inicio Rápido (5 minutos)

### Paso 1: Preparar Entorno (1 min)

```bash
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization

# Activar venv
source .venv/bin/activate

# Verificar Python
python --version  # Debe ser 3.12.x
```

### Paso 2: Ejecutar Notebook (4 minutos)

**Opción A: Terminal (Recomendado)**

```bash
# Ejecutar directamente
jupyter notebook notebooks/session3_connectivity.ipynb
# Se abre en navegador automáticamente
# Ir a: Run → Run All Cells
# Esperar ~60 segundos
```

**Opción B: VS Code**

```
1. Abrir archivo: notebooks/session3_connectivity.ipynb
2. Seleccionar Kernel: Python 3.12.3 (.venv)
3. Tecla: Ctrl+Alt+Enter (Run All Cells)
4. Esperar resultado
```

**Opción C: Automatizado (Con Papermill)**

```bash
papermill \
  notebooks/session3_connectivity.ipynb \
  notebooks/session3_connectivity_executed.ipynb
```

### Paso 3: Ver Resultados (1 min)

```bash
# Ver tabla comparativa
cat data/solution_metadata_v1.json | python -m json.tool

# Ver imagen de resultados
open notebooks/session3_connectivity_results.png

# Ver reporte técnico
cat notebooks/SESSION3_REPORT.md
```

---

## 📊 ¿Qué Esperar?

### Progreso de Ejecución

```
✓ Librerías importadas (2s)
✓ Dataset cargado: 1,401 celdas (3s)
✓ Adyacencias: 8,500 aristas (5s)
✓ Parámetros preparados (2s)
✓ Modelo Pyomo definido (1s)
⏳ RESOLVER MILP... (40-50s)  <-- ESPERA AQUÍ
✓ Solución extraída (3s)
✓ Validación: CORRECTA (1s)
✓ Comparación v0 vs v1 (1s)
✓ Visualización generada (8s)
✓ Metadatos exportados (1s)
✅ COMPLETADO - Tiempo total: ~75s
```

---

## 💾 Archivos Generados

```
✓ adaptations_detailed_v1.csv    # 412 adaptaciones
✓ corridors_selected.csv          # 187 corredores
✓ solution_metadata_v1.json       # Metadatos
✓ session3_connectivity_results.png  # Visualización
```

---

## 📈 Resultados Esperados

```
╔═══════════════════════════════════════════════════╗
║  MODELO v1 - CONECTIVIDAD ECOLÓGICA              ║
╠═══════════════════════════════════════════════════╣
║  Objetivo:              625.45                    ║
║  Presupuesto usado:     498.92 / 500.0 (99.78%)  ║
║  Adaptaciones:          412 celdas                ║
║  Corredores:            187 activados             ║
║  Conectividad:          62.5% de celdas           ║
║  Tiempo:                42.3 segundos             ║
╠═══════════════════════════════════════════════════╣
║  vs Session 2 (v0):     +2.72% objetivo          ║
║  Conectividad nuevo:    0% → 62.5%               ║
╚═══════════════════════════════════════════════════╝
```

---

## ⚙️ Personalizar (Opcional)

**Archivo:** `notebooks/session3_connectivity.ipynb` → Sección 4

```python
# Cambiar presupuesto
BUDGET = 750  # [100, 250, 500, 750, 1000]

# Cambiar importancia de conectividad
LAMBDA_CONNECTIVITY = 0.5  # [0.1, 0.3, 0.5]

# Cambiar pesos de especies
weights = {
    'eliomys': 2.0,       # Aumentar importancia
    'martes': 1.0,
    'atelerix': 1.0,
    'oryctolagus': 0.5
}
```

Luego re-ejecutar: **Run All Cells**

---

## 🔧 Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| "Solver 'highs' not found" | `pip install highspy` |
| "dataset_processed.geojson not found" | Ejecutar Session 1 primero |
| Ejecución muy lenta | Usar `BUDGET = 250` (más rápido) |
| Kernel no encontrado | Seleccionar manualmente: Python 3.12.3 (.venv) |
| Error de memoria | Reducir `cells` a 700: `cells = gdf['grid_id'].tolist()[:700]` |

---

## 📚 Próximo Paso

Después de ejecutar, leer:

1. **[SESSION3_REPORT.md](SESSION3_REPORT.md)** - Análisis técnico detallado
2. **[README_SESSION3.md](README_SESSION3.md)** - Guía completa
3. **[INDEX.md](INDEX.md)** - Navegación del proyecto

---

## ✅ Validar Ejecución

```bash
# Verificar que los archivos se generaron
ls -lh data/solution_metadata_v1.json
ls -lh data/adaptations_detailed_v1.csv
ls -lh data/corridors_selected.csv
file notebooks/session3_connectivity_results.png

# Ver resumen de solución
python -c "import json; print(json.load(open('data/solution_metadata_v1.json')))['results']"
```

---

## 🎯 En Caso de Éxito ✅

```
1. ✓ Modelo MILP exacto ejecutado
2. ✓ 187 corredores identificados
3. ✓ Conectividad ecológica cuantificada
4. ✓ Comparación v0 vs v1 documentada
5. ✓ Listo para Session 4 (Sensibilidad)
```

---

**Tiempo total estimado:** 5 minutos  
**Complejidad:** Baja (todo automatizado)  
**Resultado:** Modelo de optimización completo  

🚀 **¡Inicia ahora!**
