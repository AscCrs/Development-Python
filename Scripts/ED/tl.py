import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(t):
    return t * np.exp(-10*t)

def laplace_transform(f, s):
    def integrand(t):
        return f(t) * np.exp(-s*t)
    integral, _ = integrate.quad(integrand, 0, np.inf)
    return integral

# Calcular transformada de Laplace
w = 2 * np.pi
s = 1j * w
F = laplace_transform(f, s)
print('Transformada de Laplace en s = ', s, ': ', F)

# Graficar la función
t = np.linspace(0, 1, 1000)
plt.plot(t, f(t))
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Gráfica de f(t)')
plt.show()
