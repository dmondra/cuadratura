# Tutorial de uso

En esta sección se muestran ejemplos de uso de las funciones implementadas para aproximar la integral:

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
