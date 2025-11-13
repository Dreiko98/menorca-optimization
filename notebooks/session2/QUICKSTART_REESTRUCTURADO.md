# 📖 Guía de Ejecución - Session 2 Reestructurada

## 🎯 Notebook Reestructurado

El notebook `session2_modeling_executed.ipynb` ha sido **completamente reestructurado** para implementar optimización regional desde el principio.

---

## 📋 Estructura del Notebook

### Sección 1: Configuración Inicial (Celdas 1-3)
1. **Título y descripción** del enfoque regional
2. **Estrategia explicada** (problema, solución, ventajas)
3. **Importaciones y dependencias**

### Sección 2: Carga de Datos (Celdas 4-5)
4. **Importación de librerías** (Pyomo, GeoPandas, scikit-learn, etc.)
5. **Carga del dataset** geoespacial

### Sección 3: Parámetros del Modelo (Celdas 6-7)
6. **Parámetros principales** (especies, costes, hábitats naturales)
7. **Funciones auxiliares** (idoneidad ecológica)

### Sección 4: Definición del Modelo (Celda 8)
8. **Función de modelo MILP** ultra-simplificado

### Sección 5: Configuración (Celdas 9-11)
9. **Parámetros de optimización** (presupuesto, pesos, umbrales, N_REGIONS)
10. **Tabla de idoneidad ecológica** (23 tipos de terreno × 4 especies)

### Sección 6: Particionamiento (Celda 12)
11. **K-Means clustering** espacial (divide en N_REGIONS)

### Sección 7: Visualización Regiones (Celda 13)
12. **Mapa de regiones** creadas

### Sección 8: Optimización (Celda 14)
13. **Loop principal** que resuelve región por región

### Sección 9: Análisis (Celdas 15-16)
14. **Desglose por especie** (natural + adaptado)
15. **Desglose por región** (adaptaciones y costes)

### Sección 10: Visualización (Celdas 17-18)
16. **Mapa de regiones** con colores
17. **Mapas por especie** mostrando adaptaciones

### Sección 11: Guardado (Celda 19)
18. **CSV + JSON** con resultados y metadatos

### Sección 12: Resumen (Celda 20)
19. **Tabla comparativa** y documentación

---

## 🚀 Instrucciones de Ejecución

### Opción 1: Ejecución Completa (Recomendada)

**Paso 1**: Reinicia el kernel
```
Kernel → Restart Kernel
```

**Paso 2**: Ejecuta todas las celdas en orden
```
Cell → Run All
```

**Tiempo total esperado**: 2-5 minutos

---

### Opción 2: Ejecución Paso a Paso

Si quieres ver el progreso en cada etapa:

```
Celda 1-3:   Introducción y configuración (5 seg)
Celda 4:     Instalación de dependencias (20 seg)
Celda 5:     Importación de librerías (2 seg)
Celda 6:     Carga de dataset (3 seg)
Celda 7-8:   Parámetros y funciones (1 seg)
Celda 9:     Definición de modelo (1 seg)
Celda 10-11: Configuración y tabla idoneidad (1 seg)
Celda 12:    Particionamiento espacial (60 seg)
Celda 13:    Visualización de regiones (5 seg)
Celda 14:    🔥 OPTIMIZACIÓN (40-120 seg)
Celda 15-16: Análisis de resultados (1 seg)
Celda 17-18: Visualizaciones (10 seg)
Celda 19:    Guardado de archivos (1 seg)
Celda 20:    Resumen final
```

---

## 📊 Configuración Ajustable

### Cambiar Número de Regiones

En la **celda 9**, modifica:
```python
N_REGIONS = 8  # Prueba con 4, 6, 8, 10, 12...
```

**Guía**:
- **N=4**: Regiones grandes, más rápido (~20 seg), menos óptimo
- **N=8**: Balance óptimo (~60 seg) ✅ **RECOMENDADO**
- **N=12**: Regiones pequeñas, más lento (~120 seg), más óptimo

### Cambiar Presupuesto

En la **celda 9**, modifica:
```python
BUDGET = 500.0  # Ajusta según caso de estudio
```

### Cambiar Pesos por Especie

En la **celda 9**, modifica:
```python
weights = {
    'atelerix': 1.0,      # Ajusta prioridad
    'martes': 1.2,        
    'eliomys': 1.5,       # Mayor valor = mayor prioridad
    'oryctolagus': 0.8    
}
```

---

## ✅ Validaciones Automáticas

El notebook valida automáticamente:

- ✅ **Presupuesto**: No excede límite en cada región
- ✅ **Doble conteo**: No adapta donde ya hay hábitat natural
- ✅ **Idoneidad**: Solo adapta en terrenos con q >= tau
- ✅ **Convergencia**: Todas las regiones resuelven exitosamente

---

## 📁 Archivos Generados

Al completar la ejecución se generan:

### 1. `adaptations_detailed_v0.csv`
```csv
grid_id,species,cost,region
1234,eliomys,1.23,3
5678,martes,2.45,5
...
```

### 2. `solution_metadata_v0.json`
```json
{
  "model_version": "v0_habitat_adaptation_regional",
  "optimization_strategy": "spatial_partitioning",
  "n_regions": 8,
  "budget": 500.0,
  "total_cost": 487.23,
  "n_adaptations": 142,
  "solve_time_seconds": 67.3,
  "species_breakdown": {...},
  "regional_breakdown": {...}
}
```

---

## 🔧 Troubleshooting

### Error: "No module named 'sklearn'"
**Solución**: La celda 3 instala automáticamente. Si falla:
```bash
pip install scikit-learn
```

### Error: "Solver glpk not available"
**Solución**: La celda 3 instala automáticamente. Si falla:
```bash
pip install glpk
# O con conda:
conda install -c conda-forge glpk
```

### Error: "NameError: name 'N_REGIONS' is not defined"
**Causa**: No ejecutaste las celdas en orden.
**Solución**: Reinicia kernel y ejecuta desde celda 1.

### Warning: "Some regions failed to solve"
**Causa**: Solver no disponible o región con restricciones muy estrictas.
**Solución**: Verifica que al menos GLPK o CBC estén instalados.

---

## 📊 Resultados Esperados

### Consola (Celda 14)

```
======================================================================
🚀 INICIANDO OPTIMIZACIÓN POR REGIONES (8 regiones)
======================================================================

======================================================================
📍 REGIÓN 1/8
======================================================================
   Celdas: 176 (12.6% del total)
   Presupuesto: 62.81 (12.6% del total)
   Variables: 704
   ✅ ÓPTIMA con GLPK en 8.2s
   Valor objetivo: 142.35
   Adaptaciones: 12
   Coste gastado: 61.42 / 62.81

[... regiones 2-8 ...]

======================================================================
✅ OPTIMIZACIÓN COMPLETADA
======================================================================
⏱️  Tiempo total: 67.3 segundos
🎯 Valor objetivo acumulado: 1,234.56
💰 Coste total gastado: 487.23 / 500.00
📍 Total adaptaciones: 142
======================================================================
```

### Análisis por Especie (Celda 15)

```
📊 DESGLOSE POR ESPECIE:
======================================================================

🐾 ATELERIX:
   Natural:   24 celdas
   Adaptadas:  18 celdas
   TOTAL:   42 celdas (3.0% cobertura)
   Coste: 45.67

🐾 MARTES:
   Natural:   11 celdas
   Adaptadas:  32 celdas
   TOTAL:   43 celdas (3.1% cobertura)
   Coste: 123.45

🐾 ELIOMYS:
   Natural:   20 celdas
   Adaptadas:  67 celdas
   TOTAL:   87 celdas (6.2% cobertura)
   Coste: 234.56

🐾 ORYCTOLAGUS:
   Natural:   16 celdas
   Adaptadas:  25 celdas
   TOTAL:   41 celdas (2.9% cobertura)
   Coste: 83.55

======================================================================
```

---

## 🎓 Conceptos Clave

### ¿Por Qué Funciona la Optimización Regional?

1. **Problema pequeño**: Cada región tiene ~700 variables (vs 5,604 total)
2. **Memoria manejable**: Modelos pequeños caben fácilmente en RAM
3. **Solver estable**: GLPK funciona bien con problemas pequeños
4. **Sin presolve hang**: Modelos resuelven en segundos

### Limitaciones Conocidas

- **Optimalidad**: Solución regional-óptima ≠ global-óptima (gap ~5-15%)
- **Efectos de frontera**: No considera corredores entre regiones
- **Distribución de presupuesto**: Proporcional a celdas (no a valor esperado)

---

## 📚 Documentación Adicional

- **`REGIONAL_OPTIMIZATION_GUIDE.md`**: Guía técnica completa (15 páginas)
- **`IMPLEMENTATION_SUMMARY.md`**: Resumen ejecutivo de cambios
- **`README.md`**: Descripción general del proyecto

---

## ✅ Checklist Final

Antes de dar por completada la ejecución, verifica:

- [ ] Todas las celdas ejecutaron sin errores
- [ ] Se generaron 2 archivos en `data/` (CSV + JSON)
- [ ] Las 8 regiones resolvieron exitosamente
- [ ] Tiempo total < 5 minutos
- [ ] Presupuesto no excedido
- [ ] Valor objetivo > 0
- [ ] Adaptaciones distribuidas entre especies
- [ ] Visualizaciones generadas correctamente

---

**Fecha de reestructuración**: 13 de noviembre de 2025  
**Versión**: v0_habitat_adaptation_regional  
**Estado**: ✅ LISTO PARA EJECUTAR
