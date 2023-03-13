import numpy as np
import matplotlib.pyplot as plt

# Definir las constantes
q = 1.6e-19
Bz = 1e-6
m = 9.11e-31
Ex = 50
Ez = 0.2e-6

# Definir las funciones x(t), y(t) y z(t)
def x(t):
    return 1 - (q*Bz/m)*t**2 - (q*Ex/(2*m))*t**2

def y(t):
    return -1 - 2*t

def z(t):
    return -t + (q*Ez/(2*m))*t**2

# Crear los puntos para la gráfica
t = np.arange(0, 100, 0.5)
X = x(t)
Y = y(t)
Z = z(t)

# Crear la figura en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar las tres funciones en la misma figura
# ax.plot(X, Y, Z)

# Graficar las tres funciones en la misma figura
for i in range(len(t)):
    ax.plot(X[i], Y[i], Z[i], 'bo')  # 'bo' para puntos azules

# Limitar los valores de los ejes
ax.set_xlim3d([min(X), max(X)])
ax.set_xlabel('X')

ax.set_ylim3d([min(Y), max(Y)])
ax.set_ylabel('Y')

ax.set_zlim3d([min(Z), max(Z)])
ax.set_zlabel('Z')

# Mostrar la gráfica
plt.show()
