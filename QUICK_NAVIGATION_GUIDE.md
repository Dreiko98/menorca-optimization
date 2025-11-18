# 🗺️ GUÍA DE NAVEGACIÓN RÁPIDA - Menorca Optimization

**Fecha:** 18 de noviembre de 2025 | **Versión:** 1.0

---

## 🎯 ¿QUÉ NECESITAS?

### 👤 "Soy nuevo en el proyecto"
**Tiempo:** 15 minutos

1. Lee [README.md](README.md) - Descripción general (5 min)
2. Lee [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) - Resumen ejecutivo (5 min)
3. Ve [PROJECT_STATUS_DASHBOARD.md](PROJECT_STATUS_DASHBOARD.md) - Estado actual (5 min)

**Resultado:** Entiendes qué es el proyecto y dónde estamos.

---

### 🚀 "Quiero ejecutar algo rápido"
**Tiempo:** 30 minutos

```bash
cd /home/ayuda137/Escritorio/asuntos\ internos/menorca-optimization
source .venv/bin/activate

# Opción 1: Ver resultados Session 2 (ya ejecutada)
jupyter notebook notebooks/session2/session2_modeling_executed.ipynb

# Opción 2: Ver resultados Session 1 (ya ejecutada)
jupyter notebook notebooks/session1/session1_exploration.ipynb

# Opción 3: Ejecutar Session 3 (ÉSA ES LA CRÍTICA)
jupyter notebook notebooks/session3_connectivity.ipynb
# Luego: Kernel → Restart & Run All
```

**Resultado:** Ves la optimización en acción.

---

### 📊 "Quiero entender la matemática"
**Tiempo:** 45 minutos

1. Lee [notebooks/SESSION3_REPORT.md](notebooks/SESSION3_REPORT.md) - Formulas + explicación (30 min)
2. Abre `notebooks/session3_connectivity.ipynb` en VS Code (10 min)
3. Lee las celdas de documentación (5 min)

**Resultado:** Entiendes la formulación MILP y los corredores ecológicos.

---

### 🔬 "Quiero ver todos los archivos de este proyecto"
**Tiempo:** 5 minutos

Abre: [FILES_MANIFEST.txt](FILES_MANIFEST.txt)  
O: [MINDMAP.md](MINDMAP.md)

**Resultado:** Ves toda la estructura del proyecto.

---

### 💻 "Necesito refactorizar/mejorar el código"
**Tiempo:** Variable

1. Lee [TODO_LIST.md](TODO_LIST.md) sección "Refactorizar código" (30 min)
2. Abre `notebooks/session2/session2_modeling.ipynb` (30 min)
3. Extrae funciones a `src/model_greedy.py` (2 horas)

**Resultado:** Código modular y reutilizable.

---

### 📈 "¿Cuál es el siguiente paso?"
**Tiempo:** 5 minutos

Lee: [TODO_LIST.md](TODO_LIST.md) sección "TAREAS CRÍTICAS"

**Resumen:**
1. Ejecutar Session 3 (70 min)
2. Crear Session 4 (2-3 horas)
3. Iniciar paper (8-10 horas)

---

### 📄 "Necesito escribir el paper IEEE"
**Tiempo:** Variable (8-10 horas)

1. Lee [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) para contenido (10 min)
2. Lee [notebooks/SESSION3_REPORT.md](notebooks/SESSION3_REPORT.md) para ecuaciones (30 min)
3. Abre `paper/ieee_template.tex` (2 min)
4. Comienza a escribir secciones (7-9 horas)

**Estructura Propuesta en TODO_LIST.md**

---

### 🎓 "Quiero aprender análisis geoespacial"
**Tiempo:** Variable

1. Abre `notebooks/session1/session1_exploration.ipynb` (30 min)
2. Lee `notebooks/session1/CONCLUSIONS.md` (15 min)
3. Explora `data/dataset_processed.geojson` (opcional)

**Resultado:** Aprendes técnicas EDA geoespacial.

---

### 🧪 "Necesito validar un resultado"
**Tiempo:** 15 minutos

1. Abre [PROJECT_STATUS_DASHBOARD.md](PROJECT_STATUS_DASHBOARD.md)
2. Ve sección "Checklist de Validación"
3. Sigue los pasos

**Resultado:** Sabes si todo está bien.

---

## 📑 ÍNDICE JERÁRQUICO

### NIVEL 1: Orientación General
```
├── README.md ⭐ EMPEZAR AQUÍ
├── EXECUTIVE_SUMMARY.md
├── PROJECT_STATUS_DASHBOARD.md
└── WORKSPACE_ORGANIZATION_REPORT.md
```

### NIVEL 2: Documentación de Sessions
```
├── notebooks/INDEX.md
├── notebooks/SESSION3_REPORT.md (más técnico)
├── notebooks/QUICKSTART_SESSION3.md (más rápido)
├── notebooks/session2/SESSION2_COMPLETE_REPORT.md
└── notebooks/session1/CONCLUSIONS.md
```

### NIVEL 3: Código Ejecutable
```
├── notebooks/session1/session1_exploration.ipynb ✅
├── notebooks/session2/session2_modeling.ipynb ✅
├── notebooks/session2/session2_modeling_executed.ipynb ✅
├── notebooks/session3_connectivity.ipynb ⏳
└── notebooks/session4_sensitivity.ipynb 🔄
```

### NIVEL 4: Datos
```
├── data/dataset_processed.geojson (procesado)
├── data/adaptations_detailed.csv (Session 2)
├── data/corridor_adjacency.csv (Session 3)
└── data/preprocessing_log.json
```

### NIVEL 5: Código Fuente
```
├── src/utils.py (✅ existente)
├── src/model_habitat.py (esqueleto)
├── src/model_greedy.py (TODO: extraer)
└── src/model_milp.py (TODO: extraer)
```

---

## 🎯 RUTAS DE NAVEGACIÓN POR PERFIL

### 👨‍💼 Directivo/Stakeholder

**Pregunta Típica:** "¿Cuál es el estado del proyecto?"

**Ruta Recomendada:**
1. EXECUTIVE_SUMMARY.md (5 min)
2. PROJECT_STATUS_DASHBOARD.md - sección "PROGRESO GENERAL" (2 min)
3. Infografía: PROJECT_STATUS_DASHBOARD.md - sección "MÉTRICAS" (3 min)

**Tiempo Total:** 10 minutos

---

### 👨‍🔬 Científico/Investigador

**Pregunta Típica:** "¿Cómo funcionan los modelos?"

**Ruta Recomendada:**
1. README.md (5 min)
2. notebooks/SESSION3_REPORT.md - "MILP Formulation" (20 min)
3. notebooks/session3_connectivity.ipynb - celdas de explicación (20 min)
4. Datos: data/adaptations_detailed.csv (10 min)

**Tiempo Total:** 55 minutos

---

### 👨‍💻 Desarrollador/Ingeniero

**Pregunta Típica:** "¿Cómo mejoro/extiende el código?"

**Ruta Recomendada:**
1. WORKSPACE_ORGANIZATION_REPORT.md - sección "CÓDIGO" (10 min)
2. TODO_LIST.md - sección "Refactorizar" (15 min)
3. Abre notebooks en VS Code (20 min)
4. Lee src/utils.py y src/model_habitat.py (10 min)

**Tiempo Total:** 55 minutos

---

### 📊 Analista de Datos

**Pregunta Típica:** "¿Qué datos tenemos y qué se espera?"

**Ruta Recomendada:**
1. notebooks/session1/CONCLUSIONS.md (15 min)
2. FILES_MANIFEST.txt - sección "DATA" (10 min)
3. data/preprocessing_log.json (5 min)
4. notebooks/session2/optimization_results.png - ver visualización (5 min)

**Tiempo Total:** 35 minutos

---

### 📝 Redactor de Paper/Presentación

**Pregunta Típica:** "¿Qué contenido necesito para el paper?"

**Ruta Recomendada:**
1. EXECUTIVE_SUMMARY.md (10 min)
2. notebooks/SESSION3_REPORT.md (45 min)
3. TODO_LIST.md - sección "Iniciar Paper IEEE" (5 min)
4. paper/ieee_template.tex (2 min)

**Tiempo Total:** 60 minutos + 8-10 horas de escritura

---

## 🔍 BÚSQUEDA POR PREGUNTA FRECUENTE

### "¿Cuál es el objetivo principal del proyecto?"
→ [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) - Primer párrafo
→ [README.md](README.md) - "Descripción del Proyecto"

### "¿Qué datos utilizamos?"
→ [notebooks/session1/CONCLUSIONS.md](notebooks/session1/CONCLUSIONS.md) - "Dataset Overview"
→ [FILES_MANIFEST.txt](FILES_MANIFEST.txt) - sección "DATA FILES"

### "¿Cuáles son los resultados esperados?"
→ [PROJECT_STATUS_DASHBOARD.md](PROJECT_STATUS_DASHBOARD.md) - "COMPARATIVA SESSIONS"
→ [README.md](README.md) - "Resultados Resumidos"

### "¿Cómo ejecuto Session 3?"
→ [notebooks/QUICKSTART_SESSION3.md](notebooks/QUICKSTART_SESSION3.md) (5 minutos)
→ [notebooks/README_SESSION3.md](notebooks/README_SESSION3.md) (30 minutos)

### "¿Cuál es la fórmula matemática?"
→ [notebooks/SESSION3_REPORT.md](notebooks/SESSION3_REPORT.md) - "Mathematical Formulation"

### "¿Qué es Session 2 vs Session 3?"
→ [PROJECT_STATUS_DASHBOARD.md](PROJECT_STATUS_DASHBOARD.md) - "COMPARATIVA SESSIONS"

### "¿Cuál es el siguiente paso?"
→ [TODO_LIST.md](TODO_LIST.md) - "TAREAS CRÍTICAS"

### "¿Cómo navego todo el proyecto?"
→ [notebooks/INDEX.md](notebooks/INDEX.md) (navegación maestra)
→ [MINDMAP.md](MINDMAP.md) (visualización)

### "¿Dónde están los datos CSV?"
→ [data/](data/) carpeta
→ [FILES_MANIFEST.txt](FILES_MANIFEST.txt) - sección "DATA FILES"

### "¿Dónde está el código Python?"
→ [src/](src/) carpeta
→ En los notebooks (todavía no refactorizado)

---

## ⏱️ TIEMPOS TÍPICOS

| Actividad | Tiempo | Archivo |
|-----------|--------|---------|
| Orientación general | 15 min | README.md + EXECUTIVE_SUMMARY.md |
| Ejecutar Session 2 | 15 min | session2_modeling_executed.ipynb |
| Ejecutar Session 3 | 70 min | session3_connectivity.ipynb |
| Entender matemática | 45 min | SESSION3_REPORT.md |
| Refactorizar código | 4-6 h | TODO_LIST.md + src/ |
| Crear Session 4 | 2-3 h | Notebook nuevo |
| Escribir paper | 8-10 h | paper/ieee_template.tex |

---

## 📂 ARCHIVOS CLAVE

| Archivo | Propósito | Audiencia | Tiempo |
|---------|----------|-----------|--------|
| **README.md** | Inicio | Todos | 5 min |
| **EXECUTIVE_SUMMARY.md** | Resumen ejecutivo | Stakeholders | 10 min |
| **PROJECT_STATUS_DASHBOARD.md** | Estado actual | Gestores | 10 min |
| **notebooks/INDEX.md** | Índice completo | Desarrolladores | 15 min |
| **notebooks/SESSION3_REPORT.md** | Técnica MILP | Científicos | 45 min |
| **TODO_LIST.md** | Próximos pasos | Gestores | 5 min |
| **WORKSPACE_ORGANIZATION_REPORT.md** | Análisis detallado | Arquitectos | 30 min |

---

## 🚀 QUICK LINKS

```
📖 Documentación Principal:
   → README.md
   → EXECUTIVE_SUMMARY.md
   
📊 Estado del Proyecto:
   → PROJECT_STATUS_DASHBOARD.md
   → WORKSPACE_ORGANIZATION_REPORT.md
   
📋 Qué Hacer Ahora:
   → TODO_LIST.md
   
🔬 Técnica Detallada:
   → notebooks/SESSION3_REPORT.md
   → notebooks/INDEX.md
   
⚡ Inicio Rápido:
   → notebooks/QUICKSTART_SESSION3.md
   
🗺️ Navegación:
   → MINDMAP.md
   → notebooks/INDEX.md
   
📁 Estructura:
   → FILES_MANIFEST.txt
```

---

## ✅ CHECKLIST: "¿Qué LEÍ hoy?"

Marca lo que has revisado:

- [ ] README.md
- [ ] EXECUTIVE_SUMMARY.md
- [ ] PROJECT_STATUS_DASHBOARD.md
- [ ] PROJECT_STATUS_DASHBOARD.md
- [ ] TODO_LIST.md
- [ ] WORKSPACE_ORGANIZATION_REPORT.md
- [ ] notebooks/INDEX.md
- [ ] notebooks/SESSION3_REPORT.md
- [ ] MINDMAP.md
- [ ] FILES_MANIFEST.txt

**Si marcaste 5+:** ¡Estás bien orientado!  
**Si marcaste 3-4:** Lee 2-3 archivos más  
**Si marcaste <3:** Comienza con README.md

---

## 🎓 RECOMENDACIÓN FINAL

### RUTA ESENCIAL (1 HORA)
1. README.md (5 min)
2. EXECUTIVE_SUMMARY.md (10 min)
3. PROJECT_STATUS_DASHBOARD.md (15 min)
4. TODO_LIST.md (10 min)
5. notebooks/QUICKSTART_SESSION3.md (20 min)

**Resultado:** Entiendes qué es el proyecto y qué hacer ahora.

### RUTA COMPLETA (4 HORAS)
1. Ruta Esencial (1 h)
2. WORKSPACE_ORGANIZATION_REPORT.md (30 min)
3. MINDMAP.md (15 min)
4. notebooks/INDEX.md (30 min)
5. notebooks/SESSION3_REPORT.md (45 min)
6. FILES_MANIFEST.txt (15 min)

**Resultado:** Dominas toda la estructura y contenido del proyecto.

---

**Generado por:** GitHub Copilot  
**Fecha:** 18 de noviembre de 2025  
**Versión:** 1.0  
**Próxima Actualización:** Después ejecutar Session 3
