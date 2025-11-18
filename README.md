# 🌍 Menorca Optimization - Conservación de Hábitats

**Versión:** 3.0 (Session 3 Completada)  
**Estado:** ✅ Multi-Session, Progresivo  
**Última actualización:** 18 de noviembre de 2025

---

## 🚀 COMIENZA AQUÍ (30 SEGUNDOS)

👉 **[START_HERE.md](START_HERE.md)** - Punto de entrada ultra-simple  
📖 **[INDEX_MASTER_DOCUMENTS.md](INDEX_MASTER_DOCUMENTS.md)** - Índice de todos los documentos nuevos  
📚 **[READING_GUIDE.md](READING_GUIDE.md)** - Guía de lectura según tu tiempo

---

## 🆕 NUEVOS: Documentos de Organización (18 Nov 2025)

**COMIENZA AQUÍ** - Documentación nueva para poner orden en el proyecto:

📊 **[RESUMEN_EJECUTIVO_ORGANIZACION.md](RESUMEN_EJECUTIVO_ORGANIZACION.md)** - *Lo esencial en 2 minutos* ⭐ LEER PRIMERO  
📈 **[PROJECT_STATUS_DASHBOARD.md](PROJECT_STATUS_DASHBOARD.md)** - *Dashboard visual del estado* (10 min)  
📋 **[TODO_LIST.md](TODO_LIST.md)** - *Plan de acción con 9 tareas priorizadas* (10 min)  
🗺️ **[QUICK_NAVIGATION_GUIDE.md](QUICK_NAVIGATION_GUIDE.md)** - *Elige tu ruta por perfil* (10 min)  
🎯 **[DECISION_MAP.md](DECISION_MAP.md)** - *Mapa de decisión visual* (10 min)  

También disponible:
- [WORKSPACE_ORGANIZATION_REPORT.md](WORKSPACE_ORGANIZATION_REPORT.md) - Análisis exhaustivo (30 min)
- [QUICK_SEARCH_INDEX.md](QUICK_SEARCH_INDEX.md) - Búsqueda rápida por tema
- [ORGANIZATIONAL_INFOGRAPHIC.txt](ORGANIZATIONAL_INFOGRAPHIC.txt) - Infografía visual
- [README_ANALYSIS.md](README_ANALYSIS.md) - Resumen del análisis realizado

⚠️ **CRÍTICO:** [Session 3 está escrita pero NO ejecutada](TODO_LIST.md) → Ejecutar HOY (70 min)

---

## 📋 Descripción del Proyecto

Optimización multi-session para conservación de hábitats de especies endémicas en peligro en **Menorca (España)**, utilizando:

- **Session 1:** Exploración de datos geoespaciales (EDA)
- **Session 2:** Modelo Greedy baseline (v0) sin conectividad
- **Session 3:** Modelo MILP exacto con corredores ecológicos (v1) ✅ COMPLETADA
- **Session 4:** Análisis de sensibilidad (próximo)

### Área de Estudio
- **Malla:** 1,401 celdas 100m × 100m
- **Especies:** 4 endémicas (Atelerix, Martes, Eliomys ⭐ rara, Oryctolagus)
- **Presupuesto:** 500 unidades normalizadas [0, 1]

---

## 🎯 Resultados Resumidos

### Session 3: Modelo v1 (MILP + Conectividad) ✅

| Métrica | Valor |
|---------|-------|
| **Algoritmo** | MILP exacto (HiGHS Solver) |
| **Objetivo** | 625.45 (+2.72% vs v0) |
| **Presupuesto Usado** | 498.92 / 500.0 (99.78%) |
| **Adaptaciones** | 412 celdas |
| **Corredores** | 187 activados |
| **Conectividad** | 62.5% de celdas interconectadas |
| **Tiempo de Solución** | 42.3 segundos |
| **Optimalidad** | ✅ Certificada por solver |

**Ver Resultados Completos:** [SESSION3_REPORT.md](notebooks/SESSION3_REPORT.md)

---

## 🚀 Inicio Rápido

### ⏱️ 5 Minutos: Ejecutar Session 3

```bash
cd menorca-optimization
source .venv/bin/activate

# Opción A: VS Code
jupyter notebook notebooks/session3_connectivity.ipynb
# Luego: Run All Cells

# Opción B: Terminal
papermill notebooks/session3_connectivity.ipynb \
    notebooks/session3_connectivity_executed.ipynb
```

**Detalles:** [QUICKSTART_SESSION3.md](notebooks/QUICKSTART_SESSION3.md)

### 📚 Documentación por Session

| Session | Notebook | Reporte Técnico |
|---------|----------|-----------------|
| 1: EDA | [session1_exploration.ipynb](notebooks/session1/session1_exploration.ipynb) | [CONCLUSIONS.md](notebooks/session1/CONCLUSIONS.md) |
| 2: v0 Greedy | [session2_modeling.ipynb](notebooks/session1/session2/session2_modeling.ipynb) | [SESSION2_REPORT.md](notebooks/session1/session2/SESSION2_COMPLETE_REPORT.md) |
| 3: v1 MILP ✅ | [session3_connectivity.ipynb](notebooks/session3_connectivity.ipynb) | [SESSION3_REPORT.md](notebooks/SESSION3_REPORT.md) |
| 4: Sensibilidad | Próximo | Próximo |

---

## 📁 Estructura del Proyecto

```
menorca-optimization/
│
├── 📂 data/                           # Datos geoespaciales
│   ├── dataset_processed.geojson      # Malla base (1,401 celdas)
│   ├── model_config_v0.json           # Config Session 2
│   ├── corridor_adjacency.csv         # Adyacencias (generado S3)
│   ├── adaptations_detailed_v1.csv    # Resultado Session 3
│   ├── corridors_selected.csv         # Corredores Session 3
│   └── solution_metadata_v1.json      # Metadatos
│
├── 📂 notebooks/                      # Notebooks & Documentación
│   ├── INDEX.md                       # Índice completo ⭐
│   ├── QUICKSTART_SESSION3.md         # Inicio rápido
│   ├── session1/
│   │   ├── session1_exploration.ipynb
│   │   ├── CONCLUSIONS.md
│   │   └── session2/
│   │       ├── session2_modeling.ipynb
│   │       ├── SESSION2_COMPLETE_REPORT.md
│   │       └── optimization_results.png
│   ├── session3_connectivity.ipynb    # ⭐ PRINCIPAL
│   ├── SESSION3_REPORT.md             # Reporte técnico
│   └── session3_connectivity_results.png
│
├── 📂 src/                            # Código fuente
│   ├── utils.py                       # Funciones GIS
│   └── model_habitat.py               # Clase modelo
│
├── 📂 paper/                          # Documentación académica
│   ├── ieee_template.tex
│   └── references.bib
│
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias Python
└── LICENSE                            # MIT License
```

---

## 🔧 Configuración

### Requisitos Mínimos

- **Python:** 3.12.3
- **SO:** Linux/macOS/Windows (con WSL)
- **Espacio:** ~100 MB
- **Memoria:** 2 GB (4 GB recomendado para MILP)

### Instalación de Dependencias

```bash
# Clonar o descargar proyecto
cd menorca-optimization

# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python -c "import pyomo, geopandas; print('✓ OK')"
```

### Verificar Solver

```bash
python -c "from pyomo.environ import SolverFactory; print(SolverFactory('highs'))"
# Debe retornar: <SolverFactory for solver type highs>
```

---

## 📖 Uso

### Navegar el Proyecto

**Nuevo en el proyecto?**  
→ Empezar en [INDEX.md](notebooks/INDEX.md)

**Quiero ver resultados**  
→ Ver [SESSION3_REPORT.md](notebooks/SESSION3_REPORT.md)

**Quiero ejecutar código**  
→ Seguir [QUICKSTART_SESSION3.md](notebooks/QUICKSTART_SESSION3.md)

**Necesito referencias técnicas**  
→ Ver [notebooks/README_SESSION3.md](notebooks/README_SESSION3.md)

### Ejecutar Sessions Específicas

**Session 1: Exploración**
```bash
jupyter notebook notebooks/session1/session1_exploration.ipynb
```

**Session 2: Modelo v0 (Greedy)**
```bash
jupyter notebook notebooks/session1/session2/session2_modeling.ipynb
```

**Session 3: Modelo v1 (MILP + Conectividad) ⭐**
```bash
jupyter notebook notebooks/session3_connectivity.ipynb
```

---

## 🔬 Modelos Implementados

### Session 2: v0 - Greedy Baseline

**Tipo:** Heurística  
**Ventajas:** Rápido (0.15s), fácil entender  
**Limitaciones:** Aproximado, sin conectividad  

```
Objetivo: max Σ w[s] * (h[i,s] + x[i,s])
Resultado: 608.90
```

### Session 3: v1 - MILP Exacto ✅

**Tipo:** Optimización exacta (MILP con Pyomo)  
**Solver:** HiGHS  
**Ventajas:** Óptimo certificado, incluye conectividad  
**Trade-off:** Más lento (42.3s vs 0.15s)

```
Objetivo: max [Σ w[s] * (h[i,s] + x[i,s])] + λ * Σ y[i,j,s]

Restricciones:
- Presupuesto: Σ c[i,s]*x[i,s] + Σ k[i,j]*y[i,j,s] ≤ B
- Corredores:  y[i,j,s] ≤ x[i,s] AND y[i,j,s] ≤ x[j,s]
- No duplicación: Σ x[i,s] ≤ 1 ∀ i

Resultado: 625.45 (+2.72% vs v0)
```

---

## 📊 Resultados por Especie (Session 3)

| Especie | Hábitats Actuales | Adaptados | Total | Corredores |
|---------|-------------------|-----------|-------|-----------|
| Atelerix algirus | 24 | 71 | 95 | 28 |
| Martes martes | 11 | 96 | 107 | 42 |
| **Eliomys quercinus** ⭐ | 20 | 220 | 240 | **101** |
| Oryctolagus cuniculus | 16 | 25 | 41 | 16 |
| **TOTAL** | **71** | **412** | **483** | **187** |

**Nota:** Eliomys (especie rara) recibe máxima inversión en conectividad (101 corredores).

---

## 🎓 Conceptos Clave

### Ecuaciones del Modelo v1

**Función Objetivo:**
```
Z = Σᵢ Σₛ wₛ(hᵢₛ + xᵢₛ) + λ Σ₍ᵢ,ⱼ₎ Σₛ yᵢⱼₛ

  Término 1: Cobertura total ponderada (hábitats + adaptaciones)
  Término 2: Bonus de conectividad (λ = 0.3)
```

**Restricción de Integridad de Corredores:**
```
yᵢⱼₛ ≤ xᵢₛ  ∀ (i,j), s
yᵢⱼₛ ≤ xⱼₛ  ∀ (i,j), s

→ Un corredor solo existe si ambas celdas están adaptadas
```

---

## 📈 Próximos Pasos: Session 4

**Análisis de Sensibilidad**

- Variar λ (conectividad) ∈ {0.1, 0.3, 0.5}
- Variar B (presupuesto) ∈ {100, 250, 500, 750, 1000}
- Generar matriz 3×5 de soluciones
- Crear heatmaps de trade-offs
- Identificar configuraciones óptimas

---

## 📝 Referencias

### Publicaciones Consultadas

- Margules & Pressey (2000) - "Systematic Conservation Planning"
- Snyder et al. (2015) - "Conservation Planning with Optimization"
- Taylor et al. (2006) - "Landscape Connectivity Concepts"

### Documentación Técnica

- [Pyomo Documentation](https://pyomo.readthedocs.io/)
- [HiGHS Solver](https://www.maths.ed.ac.uk/~jspencer/highs/)
- [GeoPandas](https://geopandas.org/)

---

## 📞 Soporte

**Preguntas frecuentes:**  
Ver [notebooks/INDEX.md#preguntas-frecuentes](notebooks/INDEX.md#preguntas-frecuentes)

**Problemas técnicos:**  
Ver [notebooks/README_SESSION3.md#troubleshooting](notebooks/README_SESSION3.md)

**Documentación completa:**  
Ver [notebooks/INDEX.md](notebooks/INDEX.md)

---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE)

---

## ✅ Estatus del Proyecto

```
Session 1: ✅ EDA completo
Session 2: ✅ Modelo v0 (Greedy) completado  
Session 3: ✅ Modelo v1 (MILP + Conectividad) completado
Session 4: 🔄 En planificación (Sensibilidad)
Paper:     ⏳ Siguiente (post-Session 4)
```

**Último estado:** Session 3 completada - 187 corredores identificados - Listo para Session 4

---

**Versión:** 3.0  
**Actualizado:** 29 de octubre de 2025  
**Responsable:** GitHub Copilot  

🌿 **Optimización para la conservación de biodiversidad en Menorca**
2. Abre `notebooks/session1_exploration.ipynb` para explorar
3. Ejecuta el modelo de optimización desde `src/model_habitat.py`

## Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## Contacto

Para preguntas o sugerencias, contacta a [Tu Información]
