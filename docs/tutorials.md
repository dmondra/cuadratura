# Tutorial de uso

## Ejemplos de uso

```python
import numpy as np
from cuadrature import gaussxw, gaussxwab, funcionInt

# --- gaussxw ---
x, w = gaussxw(3)
print(x)
# array([-0.77459667,  0.        ,  0.77459667])

print(w)
# array([0.55555556, 0.88888889, 0.55555556])

# --- gaussxwab ---
xp, wp = gaussxwab(0, np.pi, x, w)
print(xp)
# array([...])

print(wp)
# array([...])

# --- funcionInt ---
print(funcionInt(1.0))
# 0.8414709848...

x_vals = np.array([0.0, 1.0, 2.0])
print(funcionInt(x_vals))
# array([ 0.        ,  0.84147098, -0.7568025 ])

# --- Ejemplo completo ---
N = 10
x, w = gaussxw(N)
xp, wp = gaussxwab(0, np.pi, x, w)
I = np.sum(wp * funcionInt(xp))

print(I)
# ~0.77265

# --- Convergencia ---
for N in range(1, 11):
    x, w = gaussxw(N)
    xp, wp = gaussxwab(0, np.pi, x, w)
    I = np.sum(wp * funcionInt(xp))
    print(f"N={N}, I={I}")
