# 🗺️ MAPA DE DECISIÓN - ¿Qué Hacer Ahora?

**Fecha:** 18 de noviembre de 2025

---

## 🎯 DECIDE EN 3 CLICS

```
                    ¿QUÉ NECESITAS HACER?
                            │
            ┌───────────────┼───────────────┐
            │               │               │
      ENTENDER      EJECUTAR        MEJORAR
      Proyecto        Código         Código
            │               │               │
            ▼               ▼               ▼
```

---

## 📖 OPCIÓN 1: ENTENDER EL PROYECTO

### "Necesito orientarme"
```
⏱️ TIEMPO: 30 minutos

RUTA:
1. Lee: README.md (5 min)
   → ¿Qué es el proyecto?
   
2. Lee: EXECUTIVE_SUMMARY.md (10 min)
   → ¿Cuál es el estado?
   
3. Ve: PROJECT_STATUS_DASHBOARD.md (15 min)
   → ¿Qué hay de cada session?

RESULTADO: Entiendes todo del proyecto
SIGUIENTE: Ve a "EJECUTAR CÓDIGO"
```

### "Necesito aprender la matemática"
```
⏱️ TIEMPO: 1 hora

RUTA:
1. Lee: README.md - "Resultados" (5 min)
2. Lee: notebooks/SESSION3_REPORT.md - "Mathematical" (30 min)
3. Ve: notebooks/session3_connectivity.ipynb - celdas 5-10 (20 min)
4. Lee: SESSION3_COMPLETE.md - "Innovaciones" (5 min)

RESULTADO: Entiendes MILP y corredores
SIGUIENTE: Ve a "EJECUTAR CÓDIGO" o "MEJORAR CÓDIGO"
```

### "Necesito ver resultados"
```
⏱️ TIEMPO: 15 minutos

RUTA:
1. Ve: notebooks/session2/optimization_results.png (2 min)
   → Resultados Session 2 visuales
   
2. Lee: RESUMEN_EJECUTIVO_ORGANIZACION.md (5 min)
   → Números clave
   
3. Lee: PROJECT_STATUS_DASHBOARD.md - "COMPARATIVA" (8 min)
   → Session 2 vs 3

RESULTADO: Ves números y gráficos
SIGUIENTE: Ve a "EJECUTAR CÓDIGO"
```

---

## 🚀 OPCIÓN 2: EJECUTAR CÓDIGO

### "Quiero ver Session 2 (ya funciona)"
```
⏱️ TIEMPO: 20 minutos

RUTA:
1. Abre: VS Code o Jupyter
2. Ve: notebooks/session2/session2_modeling_executed.ipynb
3. Lee las celdas con outputs
4. Ve: notebooks/session2/optimization_results.png

RESULTADO: Ves modelo Greedy funcionando
SIGUIENTE: Ve a "Ejecutar Session 3"
```

### 🔴 "QUIERO EJECUTAR SESSION 3 (CRÍTICO)"
```
⏱️ TIEMPO: 70 minutos

RUTA:

PASO 1 - PREPARAR (5 min):
  $ cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization
  $ source .venv/bin/activate
  
PASO 2 - EJECUTAR (60 min):
  $ jupyter notebook notebooks/session3_connectivity.ipynb
  
  Luego en notebook:
  Kernel → Restart Kernel and Run All Cells
  (espera ~60 segundos)
  
PASO 3 - GUARDAR (automático):
  El notebook se guarda con outputs

PASO 4 - VALIDAR (5 min):
  En la última celda verifica:
  ✓ Objetivo ≈ 625.45
  ✓ Adaptaciones ≈ 412
  ✓ Corredores ≈ 187
  ✓ Conectividad ≈ 62.5%

ARCHIVOS GENERADOS:
  ✓ data/adaptations_detailed_v1.csv
  ✓ data/corridors_selected.csv
  ✓ data/solution_metadata_v1.json
  ✓ notebooks/session3_connectivity_results.png

RESULTADO: Session 3 ejecutada y validada
SIGUIENTE: Ve a "Crear versión ejecutada" o "MEJORAR CÓDIGO"
```

### "Quiero crear versión ejecutada de Session 3"
```
⏱️ TIEMPO: 5 minutos + 60 min ejecución

RUTA:

OPCIÓN A - Automático (papermill):
  $ papermill notebooks/session3_connectivity.ipynb \
      notebooks/session3_connectivity_executed.ipynb
  (espera ~70 minutos)

OPCIÓN B - Manual:
  Session 3 ya tiene outputs tras ejecutar
  Solo guarda como: session3_connectivity_executed.ipynb
  (Ctrl+S o File → Save As)

RESULTADO: Archivo session3_connectivity_executed.ipynb creado
SIGUIENTE: Documentar resultados o ir a "MEJORAR CÓDIGO"
```

### "Quiero ejecutar TODO"
```
⏱️ TIEMPO: 2 horas

RUTA:
  $ source .venv/bin/activate
  
  $ papermill notebooks/session1/session1_exploration.ipynb \
      notebooks/session1/session1_executed.ipynb
  (espera 30 min)
  
  $ papermill notebooks/session2/session2_modeling.ipynb \
      notebooks/session2/session2_executed.ipynb
  (espera 20 min)
  
  $ papermill notebooks/session3_connectivity.ipynb \
      notebooks/session3_executed.ipynb
  (espera 70 min)

RESULTADO: Todas las sessions ejecutadas
SIGUIENTE: Ve a "MEJORAR CÓDIGO"
```

---

## 💻 OPCIÓN 3: MEJORAR CÓDIGO

### "Quiero modularizar el código"
```
⏱️ TIEMPO: 4-6 horas

VER: TODO_LIST.md → "Refactorizar código"

PASOS PRINCIPALES:
1. Lee TODO_LIST.md sección completa (30 min)
2. Crea src/model_greedy.py (1 h)
   → Extrae funciones de Session 2
3. Crea src/model_milp.py (1 h)
   → Extrae funciones de Session 3
4. Crea src/visualization.py (1 h)
   → Funciones gráficas
5. Actualiza src/utils.py (30 min)
6. Modifica notebooks para importar desde src/
7. Agrega docstrings y comentarios (30 min)

RESULTADO: Código modularizado y reutilizable
SIGUIENTE: Tests (opcional) o Paper
```

### "Quiero crear Session 4"
```
⏱️ TIEMPO: 3-5 horas

VER: TODO_LIST.md → "Preparar Session 4"

PASOS PRINCIPALES:
1. Lee TODO_LIST.md sección completa (15 min)
2. Crea notebook: notebooks/session4_sensitivity.ipynb
3. Define 15 escenarios (λ × presupuesto)
4. Implementa loop de soluciones (2 h)
5. Genera tablas comparativas
6. Visualiza resultados (heatmap, surface)
7. Escribe análisis y recomendaciones

RESULTADO: Session 4 completada con sensibilidad
SIGUIENTE: Paper o Dashboard final
```

### "Quiero agregar tests"
```
⏱️ TIEMPO: 4-6 horas

PASOS:
1. Crea directorio: tests/
2. Crea: tests/test_models.py
3. Escribe 6-8 tests unitarios
4. Ejecuta: pytest tests/
5. Integra CI/CD (opcional)

RESULTADO: Código testeable
SIGUIENTE: Documentación o Paper
```

---

## 📝 OPCIÓN 4: ESCRIBIR PAPER

### "Quiero escribir el paper IEEE"
```
⏱️ TIEMPO: 8-10 horas

VER: TODO_LIST.md → "Iniciar Paper IEEE"

PASOS:
1. Lee plantilla: paper/ieee_template.tex (5 min)
2. Lee contenido de referencia:
   • EXECUTIVE_SUMMARY.md (10 min)
   • notebooks/SESSION3_REPORT.md (30 min)
3. Escribir secciones en LaTeX (6-8 h):
   • Abstract
   • Introduction
   • Methods
   • Results
   • Discussion
   • Conclusion
4. Copiar ecuaciones de SESSION3_REPORT.md
5. Agregar figuras y referencias
6. Compilar PDF

RESULTADO: Paper IEEE completado
SIGUIENTE: Presentación o envío
```

---

## 📊 OPCIÓN 5: CREAR DASHBOARD FINAL

### "Quiero dashboard comparativo"
```
⏱️ TIEMPO: 3-4 horas

PASOS:
1. Lee: PROJECT_STATUS_DASHBOARD.md (10 min)
2. Crea: PROJECT_COMPARISON_SUMMARY.md
3. Tablas:
   • KPIs por session
   • Matriz sensibilidad (3×5)
   • Mejoras alcanzadas
4. Gráficos:
   • Barras: Objetivo por session
   • Heatmap: Matriz sensibilidad
   • Radar: Comparativa métricas
5. Recomendaciones finales

RESULTADO: Dashboard ejecutivo completo
SIGUIENTE: Presentación
```

---

## 🎯 ÁRBOL DE DECISIÓN

```
                   ¿DÓNDE ESTOY?
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    PRINCIPIANTE    INTERMEDIO      AVANZADO
        │                 │                 │
        ▼                 ▼                 ▼
   
   1. Lee README         1. Ejecuta S3      1. Modulariza
   2. Lee EXECUTIVE      2. Crea S4         2. Tests
   3. Ve DASHBOARD       3. Escribe Paper   3. Dashboard
   
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                   ▼ SIGUIENTE:
            EJECUTAR SESSION 3
```

---

## 🚨 CHECKLIST RÁPIDO

### Necesito hacer HOY:
- [ ] Ejecutar Session 3 (70 min) ← CRÍTICO
- [ ] Validar resultados (5 min)
- [ ] Guardar notebook ejecutado (automático)

### Necesito hacer ESTA SEMANA:
- [ ] Crear Session 4 (3-5 h)
- [ ] Refactorizar código (4-6 h)
- [ ] Elegir: ¿Prioritario Session 4 o refactorizar?

### Necesito hacer EN 2 SEMANAS:
- [ ] Escribir Paper IEEE (8-10 h)
- [ ] Dashboard final (3-4 h)
- [ ] Polish y presentación (2-3 h)

---

## ⏱️ ESTIMADOR DE TIEMPO

| Tarea | Tiempo | Prioridad |
|-------|--------|-----------|
| Ejecutar Session 3 | 70 min | 🔴 AHORA |
| Refactorizar código | 4-6 h | 🟠 Esta semana |
| Crear Session 4 | 3-5 h | 🟠 Esta semana |
| Escribir Paper | 8-10 h | 🟡 2 semanas |
| Dashboard final | 3-4 h | 🟡 2 semanas |
| Tests unitarios | 4-6 h | 🟢 Opcional |
| CI/CD | 2-3 h | 🟢 Opcional |

**TOTAL PROYECTO:** ~25-35 horas

---

## 💡 RECOMENDACIÓN FINAL

### Para Gestor:
```
👤 TÚ: "¿Qué debe hacerse?"
💻 RESPUESTA: Ejecutar Session 3 HOY (1 h) → Validar
            Luego Session 4 (3 h) → Paper (8 h)
⏱️ TOTAL: ~25 horas, ~2 semanas
```

### Para Técnico:
```
👤 TÚ: "¿Cómo mejoro el código?"
💻 RESPUESTA: Modulariza a src/ (4-6 h)
            Agrega tests (4-6 h, opcional)
            Mantén notebooks como orquestadores
⏱️ TOTAL: ~8-12 horas, ~1 semana
```

### Para Científico:
```
👤 TÚ: "¿Cómo publico esto?"
💻 RESPUESTA: Escribe paper IEEE (8-10 h)
            Basado en SESSION3_REPORT.md
            Agrega resultados Session 4
⏱️ TOTAL: ~12-15 horas, ~1 semana
```

---

## 🎓 PRÓXIMO PASO

### ¿Qué DEBO hacer en los próximos 5 minutos?

```
1. Abre: TODO_LIST.md
2. Scroll a: "TAREAS CRÍTICAS"
3. Lee la Tarea 1 completa
4. Sigue los 4 PASOS
5. Espera ~60 segundos
```

**LISTO. Eso es todo lo que necesitas ahora.**

---

**Generado por:** GitHub Copilot  
**Fecha:** 18 de noviembre de 2025  
**Propósito:** Mapa de decisión visual para saber qué hacer ahora
