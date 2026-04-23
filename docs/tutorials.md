# Tutorial de uso

## Ejemplos de funciones

```python
import numpy as np

# gaussxw
x, w = gaussxw(3)
print(x)
print(w)

# gaussxwab
xp, wp = gaussxwab(0, np.pi, x, w)
print(xp)
print(wp)

# funcionInt (escalar)
print(funcionInt(1.0))

# funcionInt (vector)
x_vals = np.array([0.0, 1.0, 2.0])
print(funcionInt(x_vals))
