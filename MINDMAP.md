# 🗺️ Mapa Mental: Menorca Optimization Project

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    MENORCA OPTIMIZATION PROJECT                           ║
║                    Conservación de Hábitats (v3.0)                        ║
╚═══════════════════════════════════════════════════════════════════════════╝

                                    ROOT
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                README.md        ROADMAP.md    EXECUTIVE_SUMMARY.md
                    │                │                │
                    └────────────────┼────────────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                📂 DATA            📂 NOTEBOOKS      📂 SRC
                │                  │                  │
     ┌──────────┼──────────┐  ┌─────┼─────┐      ┌──┴──┐
     │          │          │  │     │     │      │     │
session1/   session2/  session3/  INDEX.md  utils.py  model.py
     │          │          │
     │          │          ├─ session3_connectivity.ipynb
     │          │          ├─ SESSION3_REPORT.md
     │          │          ├─ README_SESSION3.md
     │          │          ├─ QUICKSTART_SESSION3.md
     │          │          └─ session3_connectivity_results.png
     │          │
     │          ├─ session2_modeling.ipynb
     │          ├─ SESSION2_COMPLETE_REPORT.md
     │          ├─ optimization_results.png
     │          └─ README.md
     │
     ├─ session1_exploration.ipynb
     ├─ CONCLUSIONS.md
     └─ TECHNICAL_STATUS.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                        ESTRUCTURA POR SESSION

    ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
    │  SESSION 1   │      │  SESSION 2   │      │  SESSION 3   │
    │     EDA      │  →   │   v0 GREEDY  │  →   │  v1 MILP+CON │
    └──────────────┘      └──────────────┘      └──────────────┘
          │                      │                      │
          │                      │                      │
    ✅ 1,401 celdas    ✅ 407 adaptadas      ✅ 412 adaptadas
    ✅ Validadas      ✅ Objetivo: 608.90   ✅ 187 corredores
    ✅ Exploradas      ✅ Sin conectividad   ✅ Objetivo: 625.45
                       ✅ Baseline           ✅ MILP exacto

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    FLUJO DE DATOS Y PROCESAMIENTO

    INPUT: dataset_processed.geojson (1,401 celdas)
      │
      ├─→ [SESSION 1: EDA]
      │       ├─ Validar datos
      │       ├─ Estadísticas
      │       └─ Visualizaciones
      │
      ├─→ [SESSION 2: v0 Greedy]
      │       ├─ Algoritmo heurístico
      │       ├─ 407 adaptaciones
      │       ├─ Objetivo: 608.90
      │       └─ Baseline para comparación
      │
      ├─→ [SESSION 3: v1 MILP] ⭐
      │       ├─ Formulación MILP
      │       ├─ Solver HiGHS
      │       ├─ 412 adaptaciones + 187 corredores
      │       ├─ Objetivo: 625.45 (+2.72%)
      │       ├─ Conectividad: 62.5%
      │       └─ ÓPTIMO CERTIFICADO
      │
      └─→ [SESSION 4: Sensibilidad] 🔄
              ├─ Variar λ ∈ {0.1, 0.3, 0.5}
              ├─ Variar B ∈ {100, 250, 500, 750, 1000}
              ├─ Matriz 3×5 de soluciones
              └─ Recomendaciones finales

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    ARCHIVOS CLAVE POR PROPÓSITO

┌─ DOCUMENTACIÓN PRINCIPAL ─────────────────────────────┐
│                                                        │
│ • README.md                    → Inicio general        │
│ • INDEX.md                     → Navegación completa   │
│ • EXECUTIVE_SUMMARY.md         → Resumen ejecutivo     │
│ • ROADMAP.md                   → Plan del proyecto     │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ DOCUMENTACIÓN SESSION 3 ─────────────────────────────┐
│                                                        │
│ • SESSION3_REPORT.md           → Técnico detallado     │
│ • README_SESSION3.md           → Guía de ejecución    │
│ • QUICKSTART_SESSION3.md       → 5 minutos rápido     │
│ • SESSION3_CHECKLIST.md        → Verificación         │
│ • SESSION3_COMPLETE.md         → Resumen logros       │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ NOTEBOOKS EJECUTABLES ───────────────────────────────┐
│                                                        │
│ • notebooks/session1_exploration.ipynb                │
│ • notebooks/session1/session2_modeling.ipynb          │
│ • notebooks/session3_connectivity.ipynb ⭐            │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ DATOS GENERADOS ─────────────────────────────────────┐
│                                                        │
│ • adaptations_detailed_v1.csv  → 412 adaptaciones     │
│ • corridors_selected.csv       → 187 corredores       │
│ • corridor_adjacency.csv       → 8,500+ adyacencias   │
│ • solution_metadata_v1.json    → Metadatos completos  │
│                                                        │
└────────────────────────────────────────────────────────┘

┌─ VISUALIZACIONES ─────────────────────────────────────┐
│                                                        │
│ • session3_connectivity_results.png (300 DPI, 850KB)  │
│   ├─ Panel 1: Mapa con corredores                     │
│   ├─ Panel 2: Comparativa v0 vs v1                    │
│   ├─ Panel 3: Distribución por especie                │
│   └─ Panel 4: Resumen de resultados                   │
│                                                        │
└────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    CONCEPTOS FUNDAMENTALES

    ┌─ VARIABLES ────────────────────┐
    │                                 │
    │ x[i,s] ∈ {0,1}                │
    │  Celda i adaptada para s       │
    │  (1 = sí, 0 = no)              │
    │                                 │
    │ y[i,j,s] ∈ {0,1}              │
    │  Corredor entre i,j para s     │
    │  (1 = sí, 0 = no)              │
    │                                 │
    └─────────────────────────────────┘

    ┌─ RESTRICCIONES ────────────────┐
    │                                 │
    │ 1. PRESUPUESTO                 │
    │    Σ c[i,s]·x[i,s]             │
    │  + Σ k[i,j]·y[i,j,s]           │
    │    ≤ B (500 unidades)          │
    │                                 │
    │ 2. INTEGRIDAD CORREDORES       │
    │    y[i,j,s] ≤ x[i,s]           │
    │    y[i,j,s] ≤ x[j,s]           │
    │                                 │
    │ 3. NO DUPLICACIÓN              │
    │    Σ x[i,s] ≤ 1 ∀ i            │
    │    (máx 1 especie por celda)    │
    │                                 │
    └─────────────────────────────────┘

    ┌─ OBJETIVO ─────────────────────┐
    │                                 │
    │ max Z = Σ w[s]·(h[i,s]         │
    │             + x[i,s])          │
    │        + λ·Σ y[i,j,s]          │
    │                                 │
    │ Cobertura + Conectividad       │
    │ (λ = 0.3 equilibrio)            │
    │                                 │
    └─────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    ESPECIES EN ESTUDIO

    ┌────────────────────────────────────────────────────┐
    │ Atelerix algirus              PESO: 1.0  MEDIA     │
    │ ├─ Hábitats actuales: 24                           │
    │ ├─ Adaptaciones: 71                                │
    │ ├─ Corredores: 28                                  │
    │ └─ Total: 95 (+295%)                               │
    └────────────────────────────────────────────────────┘

    ┌────────────────────────────────────────────────────┐
    │ Martes martes                 PESO: 1.2  VULNERABLE│
    │ ├─ Hábitats actuales: 11                           │
    │ ├─ Adaptaciones: 96                                │
    │ ├─ Corredores: 42                                  │
    │ └─ Total: 107 (+873%)                              │
    └────────────────────────────────────────────────────┘

    ┌────────────────────────────────────────────────────┐
    │ Eliomys quercinus ⭐          PESO: 1.5  MÁXIMA    │
    │ ├─ Hábitats actuales: 20                           │
    │ ├─ Adaptaciones: 220  ← Máxima inversión           │
    │ ├─ Corredores: 101   ← Mayor conectividad         │
    │ └─ Total: 240 (+1100%)  ← Mejor protegida         │
    └────────────────────────────────────────────────────┘

    ┌────────────────────────────────────────────────────┐
    │ Oryctolagus cuniculus         PESO: 0.8  BAJA      │
    │ ├─ Hábitats actuales: 16                           │
    │ ├─ Adaptaciones: 25                                │
    │ ├─ Corredores: 16                                  │
    │ └─ Total: 41 (+156%)                               │
    └────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    RESULTADOS SESSION 3

    ╔═══════════════════════════════════════════════════╗
    ║ MODELO v1 (MILP + CONECTIVIDAD)                   ║
    ╠═══════════════════════════════════════════════════╣
    ║                                                    ║
    ║ Objetivo:              625.45                      ║
    ║ Presupuesto:           498.92 / 500.0 (99.78%)    ║
    ║ Adaptaciones:          412 celdas                  ║
    ║ Corredores:            187 activados              ║
    ║ Conectividad:          62.5% de celdas            ║
    ║ Tiempo Ejecución:      42.3 segundos              ║
    ║ Solver:                HiGHS                      ║
    ║ Optimalidad:           ✅ CERTIFICADA             ║
    ║                                                    ║
    ║ vs v0 (Greedy):                                   ║
    ║ • Mejora Objetivo:     +2.72%                     ║
    ║ • Corredores Nuevos:   187                        ║
    ║ • Conectividad Nueva:  62.5%                      ║
    ║ • Trade-off Tiempo:    ×282 más lento             ║
    ║                                                    ║
    ╚═══════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    MATRIZ DE DECISIÓN

    ┌─────────────────────────────────────────────────┐
    │ ¿QUÉ LEER?          ¿PARA QUÉ?                  │
    ├─────────────────────────────────────────────────┤
    │ README.md           Intro general               │
    │ QUICKSTART_S3.md    Ejecutar en 5 minutos      │
    │ SESSION3_REPORT.md  Entender técnicamente      │
    │ INDEX.md            Navegar proyecto            │
    │ ROADMAP.md          Ver futuro                  │
    │ EXECUTIVE_SUMMARY   Resumen ejecutivo           │
    │ SESSION3_COMPLETE   Logros y estado             │
    └─────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    TIMELINE DEL PROYECTO

    Semana 1: ✅ Session 1 (EDA)              Completa
    Semana 2: ✅ Session 2 (v0 Greedy)       Completa
    Semana 3: ✅ Session 3 (v1 MILP) ⭐      Completa
    Semana 4: 🔄 Session 4 (Sensibilidad)    Planificada
    Semana 5: ⏳ Paper IEEE                   Planificada
    Semana 6: ⏳ Presentación                 Planificada

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                        ESTADO ACTUAL

    ┌────────────────────────────────────────────────┐
    │                                                 │
    │  ███████████████░░░░░░░░░░░░░░░░░░  75%        │
    │                                                 │
    │  ✅ 3 Sessions completadas                      │
    │  🔄 1 Session en planificación                  │
    │  📝 26+ documentos generados                    │
    │  🎯 10+ archivos de datos creados              │
    │  📊 Visualizaciones en 300 DPI                 │
    │  ✨ Código reproducible y documentado          │
    │                                                 │
    │  🚀 LISTO PARA SESSION 4 y publicación         │
    │                                                 │
    └────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Proyecto: Menorca Optimization v3.0
    Fecha: 29 de octubre de 2025
    Estado: ✅ Session 3 Completada - Excelencia Técnica
    Próximo: Session 4 - Análisis de Sensibilidad

    🌿 Optimización para la Conservación de Biodiversidad 🌿
```
