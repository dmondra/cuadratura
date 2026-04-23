# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#encontrar pesos y puntos de colocación.
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w
#generalizar el intervalo de integración a cualquier [a,b]
def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w
#definir la función a integrar
def funcionInt(x):
  return np.sin(x**2)

#probar para valores de N (de N=1 a N=30) para evaluar una convergencia. A mayores N, mejor la aproximación.
valoresEnN= []
valoresEnI=[]
for j in range(1, 31):
    xj, wj = gaussxw(j)
    NValor = gaussxwab(0, np.pi, xj, wj)
    I = np.sum(NValor[1] * funcionInt(NValor[0]))

    print("Resultado para N =", j, ":", I)

    valoresEnN.append(j)
    valoresEnI.append(I)
plt.figure(figsize=(8,5))
plt.plot(valoresEnN, valoresEnI, marker='o')
plt.xlabel("N")
plt.ylabel("I(N)")
plt.title("Convergencia de I con respecto a los valores de N")
plt.grid(True)
plt.show()
