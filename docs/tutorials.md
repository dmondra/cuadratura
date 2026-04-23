# Tutorial de uso

En esta sección se muestran ejemplos de uso de las funciones implementadas en [cuadrature.py](cuadrature.py):

\[
\int_0^\pi \sin(x^2)\,dx
\]

---

## 1. Uso de `gaussxw(N)`

Esta función devuelve los puntos de colocación y los pesos en el intervalo \([-1,1]\).

### Ejemplo

```python
import numpy as np

x, w = gaussxw(3)

print(x)
print(w)
```
## 2. Uso de `gaussxwab(a,b,x,w)`

Esta función devuelve los puntos de colocación y los pesos en el intervalo \([0, \pi]\).

### Ejemplo

```python
import numoy as np
x, w = gaussxw(3)
xp, wp = gaussxwab(0, np.pi, x, w)

print(xp)
print(wp)
