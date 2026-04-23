# Cuadratura Gaussiana aplicada a una integral no elemental

## Introducción

En este proyecto se estudia la aproximación numérica de la integral:

\[
I = \int_0^\pi \sin{(x^2)}\, \mathrm{d}x
\]

Esta integral; en términos generales, no tiene una antiderivada elemental. De forma similar a 
\[
I = \int e^{x^2}\, \mathrm{d}x
\]

o del mismo modo:
\[
\int \dfrac{1}{\ln{(x)}}\, \mathrm{d}x
\]

---

## Método utilizado

Se emplea la **cuadratura Gaussiana de Legendre**, la cual aproxima integrales definidas mediante una suma ponderada de evaluaciones de la función en puntos específicos del intervalo por medio de los polinomios ortogonales de Legendre.

En su forma general:

\[
\int_a^b f(x)\,dx \approx \sum_{k=1}^{N} w_k\,f(x_k)
\]

donde:
- \(x_k\) son los puntos de colocación
- \(w_k\) son los pesos asociados
- \(N\) es el número de puntos utilizados

---

## Objetivo

El objetivo de este trabajo es:

- Evaluar la integral en el intervalo \([0,\pi]\)
- Analizar la convergencia del método en función de \(N\)

---

## Resultados esperados

Se espera que, al aumentar el número de puntos \(N\), el valor de la integral converja hacia un valor cercano a:

\[
I \approx 0.77265
\]

---

## Contenido del proyecto

El repositorio se organiza de la siguiente manera:

- [Explicación del método](explanation.md)
- [Ejemplo de uso](tutorials.md)
- [Referencia de funciones empleadas y su descripción debidamente documentada](reference.md)

---

## Notas adicionales

El código fuente utilizado para la implementación se encuentra en el archivo correspondiente dentro del repositorio como un archivo .py
