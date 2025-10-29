# ⚡ Quick Start - Session 2

**¿Quieres ejecutar el notebook ahora?** Sigue estos pasos:

## 1️⃣ Accede a la carpeta del proyecto

```bash
cd "/home/ayuda137/Escritorio/asuntos internos/menorca-optimization"
```

## 2️⃣ Activa el entorno virtual

```bash
source .venv/bin/activate
```

## 3️⃣ Abre el notebook en Jupyter

```bash
jupyter notebook notebooks/session1/session2/session2_modeling.ipynb
```

VS Code debería abrirse con el notebook. Si no, copia la URL que aparece en la terminal en tu navegador.

## 4️⃣ Selecciona el Kernel Python

En VS Code:
1. Haz clic en "Select Kernel" (arriba a la derecha)
2. Elige "Python 3.12.3 ('.venv')" o similar
3. Si no aparece, haz clic en "Enter interpreter path..." y selecciona `.venv/bin/python`

## 5️⃣ Ejecuta las celdas

**Opción A (Una a una):**
- Haz clic en cada celda y presiona `Ctrl+Enter`

**Opción B (Todas a la vez):**
- Presiona `Ctrl+A` para seleccionar todo
- Luego `Ctrl+Shift+Enter` para ejecutar todas

## 6️⃣ Visualiza los resultados

Después de ejecutar, verás:
- ✓ Dataset cargado con 1401 celdas
- ✓ Modelo creado con 5604 variables
- ✓ Solución encontrada en < 1 segundo
- ✓ Gráficos generados
- ✓ Archivos CSV y JSON guardados

## 🎯 ¿Qué esperar?

**Outputs esperados:**

```
✓ Dataset cargado: 1401 celdas
✓ Parámetros preparados: 1401 celdas × 4 especies
✓ SOLUCIÓN ENCONTRADA (Greedy por eficiencia)
  Adaptaciones: 407
  Coste total: 499.80 / 500.0 (100.0%)
  Valor objetivo: 608.90

Por especie:
  atelerix: 24 + 69 = 93
  martes: 11 + 94 = 105
  eliomys: 20 + 217 = 237
  oryctolagus: 16 + 27 = 43

✓ Gráfico guardado: optimization_results.png
✓ Resultados guardados en /data

✅ SESSION 2 COMPLETADA EXITOSAMENTE
```

## ❌ ¿Problemas?

### "No kernel available"
→ Ver paso 4️⃣ (Seleccionar kernel)

### "Module not found: geopandas"
→ Ejecuta en la terminal:
```bash
source .venv/bin/activate
pip install geopandas pandas numpy matplotlib
```

### "File not found: dataset_processed.geojson"
→ Asegúrate de que ejecutaste la Session 1 primero
→ O ejecuta desde la carpeta correcta

### Ejecución lenta
→ Es normal (< 1 segundo generalmente)
→ Depende de tu CPU

## 📊 Visualización de Resultados

Los gráficos se guardan automáticamente en:
```
notebooks/session1/session2/optimization_results.png
```

Puedes abrirlos con:
```bash
xdg-open notebooks/session1/session2/optimization_results.png
```

## 📚 Siguiente Lectura

Después de ejecutar el notebook, lee en este orden:
1. **README.md** - Descripción general
2. **INDEX.md** - Guía de navegación
3. **SESSION2_COMPLETE_REPORT.md** - Análisis técnico profundo

## ✅ Checklist de Éxito

- [ ] Kernel seleccionado correctamente
- [ ] Todas las celdas ejecutadas sin errores
- [ ] Outputs mostrados en el notebook
- [ ] `optimization_results.png` generado (682 KB aprox)
- [ ] Archivo `adaptations_detailed.csv` en `/data/`
- [ ] Archivo `solution_metadata_v0.json` en `/data/`

Si todo está ✓, ¡felicidades! Session 2 está completa.

---

**Tiempo total estimado:** 5-10 minutos
**Resultado:** Modelo de optimización funcional con 407 adaptaciones

