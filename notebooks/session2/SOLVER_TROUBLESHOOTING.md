# 🔧 Solución de Problemas - Solvers

## ❌ Problema: "Could not locate the executable"

### Síntoma
```
WARNING: Could not locate the 'glpsol' executable, which is required for solver 'glpk'
WARNING: Could not locate the 'cbc' executable, which is required for solver cbc
```

### Causa
Los solvers GLPK y CBC no están instalados correctamente en tu sistema.

---

## ✅ Solución: Instalar CBC (Recomendado)

### Opción 1: Usando pip (Más fácil)

**Ejecuta esta celda en el notebook:**

```python
import sys
!{sys.executable} -m pip install coinor-cbc
```

**Luego:**
1. Reinicia el kernel (Kernel → Restart Kernel)
2. Ejecuta todas las celdas desde el principio

---

### Opción 2: Usando conda (Alternativa)

Si usas Anaconda/Miniconda:

```bash
conda install -c conda-forge coincbc
```

**Luego:**
1. Reinicia el kernel
2. Ejecuta todas las celdas

---

## 🔍 Verificar Instalación

Ejecuta esta celda para verificar:

```python
from pyomo.opt import SolverFactory

# Verifica CBC
solver = SolverFactory('cbc')
if solver.available():
    print("✅ CBC está disponible")
else:
    print("❌ CBC NO está disponible")

# Verifica HiGHS (alternativa)
solver = SolverFactory('appsi_highs')
if solver.available():
    print("✅ HiGHS está disponible")
else:
    print("❌ HiGHS NO está disponible")
```

---

## 📋 Orden de Preferencia de Solvers

El notebook intentará usar los solvers en este orden:

1. **CBC** (Community Branch & Cut)
   - ✅ Estable en Windows
   - ✅ Funciona bien con Pyomo
   - ✅ Instalar con: `pip install coinor-cbc`

2. **HiGHS** (High-performance solver)
   - ✅ Muy rápido
   - ⚠️ Puede causar crashes en Windows/Jupyter
   - ✅ Instalar con: `pip install highspy`

3. **GLPK** (GNU Linear Programming Kit)
   - ✅ Estable
   - ❌ Requiere ejecutable externo
   - ⚠️ Difícil de instalar en Windows

---

## 🚀 Ejecución Rápida

### Si tienes problemas con los solvers:

1. **Instala CBC:**
   ```python
   !pip install coinor-cbc
   ```

2. **Reinicia el kernel:**
   ```
   Kernel → Restart Kernel
   ```

3. **Ejecuta todas las celdas:**
   ```
   Cell → Run All
   ```

---

## 🆘 Si Nada Funciona

### Plan B: Usa HiGHS (ya instalado con Pyomo)

Si CBC falla, el notebook automáticamente intentará HiGHS. 

**Modificación manual** (si necesario):

En la celda de optimización (celda 14), cambia el orden:

```python
# Cambia esto:
solvers_to_try = [
    ('cbc', 'CBC (COIN-OR)'),
    ('appsi_highs', 'HiGHS'),
    ('glpk', 'GLPK')
]

# Por esto (HiGHS primero):
solvers_to_try = [
    ('appsi_highs', 'HiGHS'),
    ('cbc', 'CBC (COIN-OR)'),
    ('glpk', 'GLPK')
]
```

**Advertencia:** HiGHS puede causar crashes en algunos sistemas Windows.

---

## 📊 Comparación de Solvers

| Solver | Velocidad | Estabilidad Windows | Instalación |
|--------|-----------|---------------------|-------------|
| **CBC** | Media | ✅ Excelente | ✅ Fácil (`pip install`) |
| **HiGHS** | Rápida | ⚠️ Variable | ✅ Fácil (incluido) |
| **GLPK** | Lenta | ✅ Buena | ❌ Difícil (ejecutable) |

**Recomendación:** Usa CBC para máxima estabilidad.

---

## 🎯 Checklist de Solución

- [ ] Ejecuté `pip install coinor-cbc`
- [ ] Reinicié el kernel
- [ ] Ejecuté la celda de verificación de solvers (celda 8)
- [ ] Veo "✅ CBC está disponible"
- [ ] Ejecuté todas las celdas desde el principio
- [ ] La optimización se completa sin errors

---

## 💡 Otras Soluciones

### Si CBC se instala pero no funciona:

1. **Actualiza Pyomo:**
   ```python
   !pip install --upgrade pyomo
   ```

2. **Verifica versión de Python:**
   ```python
   import sys
   print(sys.version)
   ```
   
   Debe ser Python 3.8 o superior.

3. **Reinstala todo:**
   ```python
   !pip uninstall -y pyomo coinor-cbc
   !pip install pyomo coinor-cbc
   ```

---

## 📞 Contacto

Si después de todo esto no funciona:
1. Verifica que estás usando el kernel correcto
2. Comprueba permisos de instalación
3. Intenta ejecutar desde terminal: `pip install coinor-cbc`

---

**Última actualización:** 13 de noviembre de 2025
