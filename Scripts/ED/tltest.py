import numpy as np
import matplotlib.pyplot as plt

def leggauss(n):
    '''
    Calcula los nodos y pesos de la fórmula de Gauss-Legendre de grado n.
    '''

    # Coeficientes iniciales
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)

    # Aproximación inicial de los nodos (raíces del polinomio de Legendre)
    for i in range(n):
        a[i] = -np.cos(np.pi * (i + 0.75) / (n + 0.5))

    # Mejora de la aproximación utilizando el método de Newton
    eps = 1e-15
    delta = 1.0
    while delta > eps:
        for i in range(n):
            p = 1.0
            for j in range(n):
                if j != i:
                    p *= (a[i] - a[j])
            b[i] = sum(a) - a[i]
            c[i] = sum(1.0 / (a[i] - a[j]) for j in range(n) if j != i)
            a[i] -= p / ((1.0 - b[i]**2) * c[i])
        delta = np.max(np.abs(p / ((1.0 - b**2) * c)))

    # Cálculo de los pesos
    w = 2.0 / ((1.0 - b**2) * c)

    return a, w

def laplace_transform(func, s):
    """
    Calcula la transformada de Laplace de una función dada utilizando
    el método de cuadratura de Gauss-Legendre.
    
    Parameters:
    -----------
    func : callable
        Función a integrar.
    s : float
        Valor de s en la transformada de Laplace.
    
    Returns:
    --------
    L : float
        Valor de la transformada de Laplace en s.
    """
    # Obtenemos los puntos y pesos de la cuadratura de Gauss-Legendre
    x, w = leggauss(100)
    
    # Evaluamos la función en los puntos y sumamos los resultados ponderados por los pesos
    res = 0.0
    for i in range(len(x)):
        res += w[i] * func(x[i] / (s + 0j))
    
    # Multiplicamos por un factor común y devolvemos el resultado
    return res * (1 / s)

def func(t):
    return np.exp(-10*t) * t

w = 2 * np.pi
s = 1j * w
L = laplace_transform(func, s)

print(f"Transformada de Laplace en s = {s} : {L}")

# Graficamos la función original
t = np.linspace(0, 2, 1000)
y = func(t)
plt.plot(t, y, label="Función original")

# Graficamos la parte real e imaginaria de la transformada de Laplace
plt.plot(w.real, L.real, 'o', label="Parte real")
plt.plot(w.imag, L.imag, 'o', label="Parte imaginaria")

# Configuramos el gráfico
plt.xlabel("s")
plt.ylabel("Transformada de Laplace")
plt.title("Transformada de Laplace de $te^{-10t}$")
plt.legend()
plt.show()