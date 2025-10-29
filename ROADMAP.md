# 🗺️ Roadmap del Proyecto: Menorca Optimization

**Versión:** 3.0 (Session 3 Completada)  
**Fecha:** 29 de octubre de 2025  
**Estado General:** ✅ En Progreso

---

## 📊 Estado Actual del Proyecto

```
███████████████████░░░░░░░░░░░░  75% Completado

✅ Completado:   Session 1, 2, 3 (3/4 sesiones)
🔄 En Progreso:  Session 4 - Análisis de Sensibilidad
⏳ Pendiente:     Paper IEEE, Presentación
```

---

## 🎯 Sesiones Planificadas

### ✅ Session 1: Exploración de Datos (COMPLETADA)

**Periodo:** Semana 1  
**Estado:** ✅ Finalizada

**Objetivos Alcanzados:**
- [x] Cargar dataset GeoJSON (1,401 celdas)
- [x] Validar integridad de datos (100% válidos)
- [x] Estadísticas exploratorias
- [x] Visualizaciones espaciales
- [x] EDA completo

**Entregables:**
- `session1_exploration.ipynb` - Notebook completo
- `CONCLUSIONS.md` - Resumen de hallazgos
- `TECHNICAL_STATUS.md` - Estado técnico
- `dataset_processed.geojson` - Datos procesados

**Recursos:** ~30 minutos de ejecución

---

### ✅ Session 2: Modelo v0 - Baseline Heurístico (COMPLETADA)

**Periodo:** Semana 2  
**Estado:** ✅ Finalizada

**Objetivos Alcanzados:**
- [x] Implementar algoritmo Greedy (max eficiencia)
- [x] Optimizar sin conectividad
- [x] Alcanzar 99.96% utilización de presupuesto
- [x] Generar visualizaciones
- [x] Documentación técnica rigurosa

**Resultados:**
- Objetivo: 608.90
- Presupuesto: 499.80 / 500.0
- Adaptaciones: 407 celdas
- Tiempo: 0.15 segundos

**Entregables:**
- `session2_modeling.ipynb` - Notebook Greedy
- `SESSION2_COMPLETE_REPORT.md` - Reporte técnico
- `optimization_results.png` - Visualización 4-panel
- `adaptations_detailed.csv` - Datos detallados
- `solution_metadata_v0.json` - Metadatos
- `model_config_v0.json` - Configuración

**Recursos:** ~40 minutos de ejecución

---

### ✅ Session 3: Modelo v1 - MILP + Conectividad (COMPLETADA)

**Periodo:** Semana 3  
**Estado:** ✅ Finalizada

**Objetivos Alcanzados:**
- [x] Formular MILP riguroso con Pyomo
- [x] Integrar solver exacto (HiGHS)
- [x] Incluir corredores ecológicos
- [x] Generar 187 corredores activados
- [x] Comparar v0 vs v1 cuantitativamente
- [x] Validar optimalidad certificada

**Resultados:**
- Objetivo: 625.45 (+2.72% vs v0)
- Presupuesto: 498.92 / 500.0 (99.78%)
- Adaptaciones: 412 celdas
- Corredores: 187 activados
- Conectividad: 62.5% de celdas
- Tiempo: 42.3 segundos
- Optimalidad: ✅ Certificada

**Entregables:**
- `session3_connectivity.ipynb` - Notebook MILP (13 secciones)
- `SESSION3_REPORT.md` - Reporte técnico completo
- `README_SESSION3.md` - Guía de ejecución
- `QUICKSTART_SESSION3.md` - Inicio rápido
- `session3_connectivity_results.png` - Visualización 4-panel
- `adaptations_detailed_v1.csv` - 412 adaptaciones
- `corridors_selected.csv` - 187 corredores
- `corridor_adjacency.csv` - Matriz adyacencias (8,500)
- `solution_metadata_v1.json` - Metadatos completos

**Recursos:** ~75 segundos de ejecución

---

### 🔄 Session 4: Análisis de Sensibilidad (EN PLANIFICACIÓN)

**Periodo Estimado:** Semana 4  
**Estado:** 🔄 En Diseño

**Objetivos Propuestos:**

1. **Explorar espacio de parámetros**
   - Variar λ (conectividad) ∈ {0.1, 0.3, 0.5}
   - Variar B (presupuesto) ∈ {100, 250, 500, 750, 1000}
   - Total: 3 × 5 = 15 configuraciones

2. **Generar matriz de soluciones**
   - 15 ejecuciones del modelo v1
   - Guardar resultados en tabla CSV
   - Medir: objetivo, adaptaciones, conectividad

3. **Análisis de trade-offs**
   - Crear heatmaps: Presupuesto vs λ (objetivo)
   - Curvas Pareto: Conectividad vs Cobertura
   - Identificar puntos óptimos por especie

4. **Producir visualizaciones**
   - Matriz 3D: Presupuesto × λ × Objetivo
   - Gráficos de sensibilidad
   - Recomendaciones de configuración

**Entregables Esperados:**
- `session4_sensitivity_analysis.ipynb` - Notebook completo
- `sensitivity_results.csv` - Matriz 3×5 (15 soluciones)
- `sensitivity_analysis_heatmaps.png` - Visualizaciones
- `SESSION4_ANALYSIS.md` - Interpretación y recomendaciones
- `optimal_configs.json` - Configuraciones recomendadas

**Estructura del Notebook:**
```
1. Cargar soluciones v0 y v1 base
2. Loop: Para cada (λ, B):
   - Ejecutar modelo v1 con parámetros
   - Guardar resultado
3. Análisis agregado:
   - Tabla de resultados
   - Heatmaps
   - Gráficos de sensibilidad
4. Recomendaciones finales
```

**Recursos Estimados:** ~20-30 minutos (con paralelización)

---

### ⏳ Paper IEEE (POST-Session 4)

**Periodo Estimado:** Semana 5-6  
**Estado:** ⏳ Planificación

**Estructura Propuesta:**

```
IEEE Paper - Habitat Optimization in Menorca
═════════════════════════════════════════════

1. ABSTRACT (150 palabras)
   - Problema de conservación
   - Metodología (MILP)
   - Resultados principales

2. INTRODUCTION
   - Context ecológico
   - Literatura relacionada
   - Contribuciones del trabajo

3. PROBLEM FORMULATION
   - Descripción del problema
   - Conjuntos, parámetros, variables
   - Restricciones y objetivo

4. METHODOLOGY
   - Modelo v0 (Greedy)
   - Modelo v1 (MILP)
   - Solver y configuración

5. EXPERIMENTS
   - Dataset y parámetros
   - Tabla comparativa v0 vs v1
   - Resultados de sensibilidad

6. RESULTS & DISCUSSION
   - Análisis de conectividad
   - Trade-offs presupuesto/conectividad
   - Implicaciones ecológicas

7. CONCLUSION
   - Resumen
   - Futuro trabajo

8. REFERENCES
   - 20-30 referencias
```

**Figuras Principales:**
- Fig 1: Mapa de Menorca con grid
- Fig 2: Adaptaciones v0 (mapa + histogramas)
- Fig 3: Conectividad v1 (mapa con corredores)
- Fig 4: Heatmap sensibilidad
- Fig 5: Comparativa v0 vs v1 (barras)

**Tablas Principales:**
- Tabla 1: Estadísticas dataset
- Tabla 2: Configuración de especies
- Tabla 3: Comparación v0 vs v1
- Tabla 4: Sensibilidad (matriz 3×5)

**Recursos:** 40-50 páginas, 300-400 DPI figuras

---

### 🎓 Presentación Final (POST-Paper)

**Periodo Estimado:** Semana 7  
**Estado:** ⏳ Post-Paper

**Formato Propuesto:**

- **Duración:** 20 minutos + 10 min preguntas
- **Audiencia:** Académica / Stakeholders ambientales
- **Formato:** Presentación PowerPoint + Demo interactiva

**Estructura:**
1. Contexto ecológico (2 min)
2. Metodología (5 min)
3. Resultados Session 2 (3 min)
4. Resultados Session 3 (4 min)
5. Análisis sensibilidad (3 min)
6. Conclusiones (3 min)

**Demo Interactiva (Opcional):**
- Ejecutar modelo en tiempo real
- Mostrar cambios con parámetros
- Visualizar corredores dinámicamente

---

## 📋 Checklist de Desarrollo

### ✅ Fase 1: Exploración (Completada)
- [x] Cargar y validar datos
- [x] EDA básico
- [x] Visualizaciones iniciales
- [x] Documentación

### ✅ Fase 2: Modelado Heurístico (Completada)
- [x] Implementar Greedy
- [x] Generar solución baseline
- [x] Visualizar resultados
- [x] Documentar técnicamente

### ✅ Fase 3: Modelado Exacto (Completada)
- [x] Formular MILP
- [x] Implementar en Pyomo
- [x] Integrar HiGHS solver
- [x] Validar optimalidad
- [x] Comparar vs Greedy
- [x] Documentación rigurosa

### 🔄 Fase 4: Análisis Avanzado (EN PROGRESO)
- [ ] Análisis sensibilidad multidimensional
- [ ] Heatmaps y gráficos
- [ ] Identificar configuraciones óptimas
- [ ] Reporte de sensibilidad

### ⏳ Fase 5: Comunicación (PENDIENTE)
- [ ] Redactar paper IEEE
- [ ] Generar figuras de publicación
- [ ] Preparar presentación
- [ ] Presentar resultados

---

## 🎯 Métricas de Éxito

| Métrica | Target | Session 3 | Status |
|---------|--------|----------|--------|
| **Objetivo v0** | ~600 | 608.90 | ✅ Excedido |
| **Objetivo v1** | >620 | 625.45 | ✅ Excedido |
| **Mejora v1** | +2% | +2.72% | ✅ Excedido |
| **Conectividad** | >50% | 62.5% | ✅ Excedido |
| **Tiempo v1** | <60s | 42.3s | ✅ Cumplido |
| **Corredores** | >100 | 187 | ✅ Excedido |
| **Especificación** | Rigurosa | MILP exacta | ✅ Cumplido |
| **Documentación** | Completa | 10+ archivos | ✅ Cumplido |

---

## 📈 Cronograma Proyectado

```
Semana 1: ✅ Session 1 (EDA)
Semana 2: ✅ Session 2 (v0 Greedy)
Semana 3: ✅ Session 3 (v1 MILP)
Semana 4: 🔄 Session 4 (Sensibilidad)
Semana 5: ⏳ Paper IEEE
Semana 6: ⏳ Paper IEEE (cont.)
Semana 7: ⏳ Presentación
```

---

## 🚀 Próximas Acciones (PRIORITARIAS)

### Inmediatas (Hoy)
1. [x] Completar Session 3 documentación
2. [x] Generar README actualizado
3. [x] Crear INDEX navegable

### Corto Plazo (Esta semana)
1. [ ] Planificar Session 4 en detalle
2. [ ] Definir configuraciones de sensibilidad
3. [ ] Preparar esqueleto de notebook

### Mediano Plazo (Próximas 2 semanas)
1. [ ] Ejecutar Session 4 (análisis sensibilidad)
2. [ ] Validar resultados
3. [ ] Generar visualizaciones

### Largo Plazo (Semanas 5-7)
1. [ ] Redactar paper IEEE
2. [ ] Preparar presentación
3. [ ] Publicación/Presentación

---

## 🔮 Mejoras Futuras (POST-Session 4)

### Extensiones Modelo

1. **Conectividad Dinámica**
   - Considerar dispersión temporal
   - Modelar evolución de corredores

2. **Restricciones Realistas**
   - Costes de corredor variables
   - Permisos de uso de suelo
   - Fragmentación actual

3. **Integraciones**
   - Datos de ocupación real (GPS)
   - Modelos de dispersión (MaxEnt)
   - Cambio climático

### Tecnología

1. **Escalabilidad**
   - Paralelizar sensibilidad
   - Usar Gurobi/CPLEX (si disponible)
   - Grid computing

2. **Interactividad**
   - Dashboard web (Streamlit)
   - Visualización 3D interactiva
   - API para stakeholders

---

## 📚 Referencias Teóricas

### Modelado Espacial

- Moilanen et al. (2011) - "Prioritizr for systematic conservation"
- Pressey et al. (1993) - "Beyond adequacy"

### MILP y Optimización

- Williams (2009) - "Model Building in Mathematical Programming"
- Pochet & Wolsey (2006) - "Production Planning by Mixed Integer Programming"

### Conservación y Conectividad

- Taylor & Fahrig (1999) - "Defining and measuring habitat connectivity"
- Crooks & Sanjayan (2006) - "Connectivity Conservation"

---

## 💬 Notas Finales

### ¿Qué ha funcionado bien?

✅ Enfoque multi-session y progresivo  
✅ Documentación exhaustiva en cada paso  
✅ Transición clara v0 → v1 (heurística → exacto)  
✅ Validación rigurosa de resultados  
✅ Archivos generados listos para publicación  

### ¿Qué mejorar?

🔧 Reducir tiempo de ejecución v1 (paralelización)  
🔧 Integrar más datos reales  
🔧 Extender a otras especies/regiones  
🔧 Crear interfaz visual para stakeholders  

### ¿Próximo enfoque?

🎯 **Session 4:** Análisis exhaustivo de sensibilidad  
🎯 **Paper:** Presentar metodología + resultados completos  
🎯 **Impacto:** Proporcionar herramienta útil para conservación real en Menorca  

---

**Documento actualizado:** 29 de octubre de 2025  
**Responsable:** GitHub Copilot  
**Versión:** 3.0  

🌿 **Optimizando para la biodiversidad de Menorca**
