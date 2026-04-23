import numpy as np
import matplotlib.pyplot as plt


def gaussxw(N):
    """
    Calcula los puntos de colocación y pesos para la cuadratura de Gauss-Legendre.

    Parameters
    ----------
    N : int
        Número de puntos de colocación.

    Returns
    -------
    x : ndarray
        Puntos de colocación en el intervalo [-1, 1].
    w : ndarray
        Pesos asociados a cada punto.

    Examples
    --------
    >>> x, w = gaussxw(3)
    >>> x.shape
    (3,)
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w


def gaussxwab(a, b, x, w):
    """
    Transforma los puntos y pesos al intervalo [a, b].

    Parameters
    ----------
    a : float
        Límite inferior del intervalo.
    b : float
        Límite superior del intervalo.
    x : ndarray
        Puntos en el intervalo [-1, 1].
    w : ndarray
        Pesos en el intervalo [-1, 1].

    Returns
    -------
    xp : ndarray
        Puntos transformados al intervalo [a, b].
    wp : ndarray
        Pesos ajustados al intervalo [a, b].

    Examples
    --------
    >>> import numpy as np
    >>> x, w = gaussxw(3)
    >>> xp, wp = gaussxwab(0, np.pi, x, w)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


def funcionInt(x):
    """
    Evalúa la función f(x) = sin(x^2).

    Parameters
    ----------
    x : float or ndarray
        Valor o arreglo de valores donde se evalúa la función.

    Returns
    -------
    float or ndarray
        Resultado de evaluar sin(x^2).

    Examples
    --------
    >>> funcionInt(1.0)
    0.84147...
    """
    return np.sin(x**2)


def calcular_convergencia(N_max=30):
    """
    Calcula la aproximación de la integral para valores de N desde 1 hasta N_max.

    Parameters
    ----------
    N_max : int, optional
        Número máximo de puntos de colocación. Por defecto es 30.

    Returns
    -------
    valoresEnN : list
        Lista de valores de N utilizados.
    valoresEnI : list
        Lista de aproximaciones de la integral para cada N.

    Examples
    --------
    >>> N, I = calcular_convergencia(10)
    >>> len(N)
    10
    """
    valoresEnN = []
    valoresEnI = []

    for j in range(1, N_max + 1):
        xj, wj = gaussxw(j)
        xp, wp = gaussxwab(0, np.pi, xj, wj)
        I = np.sum(wp * funcionInt(xp))

        valoresEnN.append(j)
        valoresEnI.append(I)

    return valoresEnN, valoresEnI


def graficar_convergencia(valoresEnN, valoresEnI):
    """
    Grafica la convergencia de la integral en función de N.

    Parameters
    ----------
    valoresEnN : list
        Lista de valores de N.
    valoresEnI : list
        Lista de aproximaciones de la integral.

    Returns
    -------
    None

    Examples
    --------
    >>> N, I = calcular_convergencia(10)
    >>> graficar_convergencia(N, I)
    """
    plt.figure(figsize=(8, 5))
    plt.plot(valoresEnN, valoresEnI, marker='o')
    plt.xlabel("N")
    plt.ylabel("I(N)")
    plt.title("Convergencia de la integral")
    plt.grid(True)
    plt.show()
