# Explicación del método

## Introducción

La cuadratura gaussiana es un método numérico utilizado para aproximar integrales definidas de la forma:

\[
\int_a^b f(x)\,dx
\]

A diferencia de otros métodos como trapecios o Simpson, la cuadratura gaussiana selecciona de manera óptima los puntos de evaluación de la función, logrando una mayor precisión con un menor número de evaluaciones.

---

## Cuadratura de Gauss-Legendre

En este trabajo se utiliza la cuadratura gaussiana basada en los **polinomios de Legendre**, los cuales están definidos en el intervalo \([-1,1]\).

La aproximación general es:

\[
\int_{-1}^{1} f(x)\,dx \approx \sum_{k=1}^{N} w_k f(x_k)
\]

donde:

- \(x_k\) son las raíces del polinomio de Legendre de grado \(N\)
- \(w_k\) son los pesos asociados a cada punto
- \(N\) es el número de puntos de colocación

Este método tiene la propiedad de integrar exactamente polinomios de grado hasta \(2N-1\).

---

## Transformación de intervalo

Dado que la integral a resolver está definida en el intervalo \([0,\pi]\), es necesario transformar el intervalo \([-1,1]\) al intervalo general \([a,b]\).

Se utiliza el cambio de variable:

\[
x' = \frac{b-a}{2}x + \frac{b+a}{2}
\]

y el diferencial se transforma como:

\[
dx' = \frac{b-a}{2}dx
\]

Por lo tanto, la integral original se reescribe como:

\[
\int_a^b f(x')\,dx' = \frac{b-a}{2} \int_{-1}^{1} f\left(\frac{b-a}{2}x + \frac{b+a}{2}\right)\,dx
\]

---

## Aproximación final

Aplicando la cuadratura gaussiana, se obtiene:

\[
\int_a^b f(x)\,dx \approx \sum_{k=1}^{N} w_k' f(x_k')
\]

donde:

- \(x_k' = \frac{b-a}{2}x_k + \frac{b+a}{2}\)
- \(w_k' = \frac{b-a}{2} w_k\)

---

## Aplicación al problema

Se desea aproximar la integral:

\[
\int_0^\pi \sin(x^2)\,dx
\]

En este caso:

- \(a = 0\)
- \(b = \pi\)
- \(f(x) = \sin(x^2)\)

Se utilizan los puntos y pesos obtenidos mediante la función `leggauss(N)` de la librería `numpy`, los cuales corresponden a la cuadratura de Gauss-Legendre en \([-1,1]\).

Luego, estos valores son transformados al intervalo \([0,\pi]\) utilizando las expresiones descritas anteriormente.

---

## Convergencia del método

A diferencia de funciones polinómicas, la función \(\sin(x^2)\) no puede integrarse exactamente con un número finito pequeño de puntos. Sin embargo, al aumentar el valor de \(N\), la aproximación mejora y converge rápidamente hacia el valor real de la integral.

En este caso, se observa que la integral converge aproximadamente a:

\[
\int_0^\pi \sin(x^2)\,dx \approx 0.77265
\]

---

## Conclusión

La cuadratura gaussiana es un método altamente eficiente para la aproximación de integrales, especialmente cuando se utilizan funciones suaves. En este trabajo se comprobó que el método converge rápidamente al valor esperado al incrementar el número de puntos de colocación.
