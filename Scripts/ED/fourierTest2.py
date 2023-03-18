import numpy as np
import matplotlib.pyplot as plt

# Expansión de la serie de Fourier
def fourier(t, n):
    w0 = 2 * np.pi / 5
    suma = 0
    for i in range(1, n+1, 2):
        suma += 1 / (i ** 2) * np.cos(i * w0 * t)
    return suma * (16 / np.pi ** 2)

# Parámetros
Tmin = -5/2
Tmax = 5/2
T = Tmax - Tmin
n1 = 10
n2 = 100
n3 = 1000

# Graficar la función original y la expansión de Fourier
t = np.linspace(0, 20, 500)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(t, fourier(t, n1), lw=1, label=f'Aproximación con n={n1}')
ax.plot(t, fourier(t, n2), lw=1, label=f'Aproximación con n={n2}')
ax.plot(t, fourier(t, n3), lw=1, label=f'Aproximación con n={n3}')

ax.legend(loc='best')
ax.set_xlabel('t')
ax.set_ylabel('f(t)')
ax.set_title('Expansión de Fourier para f(t)')
plt.show()
