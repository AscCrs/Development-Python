import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def f(x):
    return x

def square_wave(t, T):
    return 0.5 * (np.sign(np.sin(2 * np.pi * t / T)) + 1)

def fourier(w0, n, T, t):
    suma = 0

    for i in range(1, n + 1):
        suma += 1/(2 * i - 1) * np.sin(i * w0 * t)
        
    return suma * 4 / np.pi 

# Definir impares = 2n - 1
n1 = 10 
n2 = 100
n3 = 1000
T = 5
Tmax = T/2
Tmin = 0

t = np.linspace(Tmin, Tmax, 1000)

w0 = (2 * np.pi) / T 

s1 = fourier(w0, n1, T, t)
s2 = fourier(w0, n2, T, t)
s3 = fourier(w0, n3, T, t)

# Graficar la serie de Fourier como un tren de pulsos
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(t, square_wave(t, T), lw=1, label='Función original')
ax.plot(t, s1, lw=1, label=f'Aproximación con n={n1}')
ax.plot(t, s2, lw=1, label=f'Aproximación con n={n2}')
ax.plot(t, s3, lw=1, label=f'Aproximación con n={n3}')

ax.legend(loc='best')
ax.set_xlabel('t')
ax.set_ylabel('f(t)')
ax.set_title('Aproximación de la serie de Fourier')

plt.show()


