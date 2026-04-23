# Tutorial de uso

## Ejemplos de uso

```python
>>> import numpy as np
>>> from cuadrature import gaussxw, gaussxwab, funcionInt

>>> x, w = gaussxw(3)
>>> x
array([-0.77459667,  0.        ,  0.77459667])

>>> w
array([0.55555556, 0.88888889, 0.55555556])

>>> xp, wp = gaussxwab(0, np.pi, x, w)
>>> xp
array([...])

>>> wp
array([...])

>>> funcionInt(1.0)
0.8414709848...

>>> funcionInt(np.array([0.0, 1.0, 2.0]))
array([ 0.        ,  0.84147098, -0.7568025 ])
