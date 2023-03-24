import math

# Función a transformar
def f(t):
    return t ** 2

# Transformada de Laplace numérica por sumas de Riemann
def laplaceTransform(s, dt, N):
    sum = 0
    for i in range(N):
        t = i * dt
        sum += f(t) * math.exp(-s*t) * dt
    return sum

if __name__ == "__main__":
    s = 1.0
    dt = 0.01
    T = 10.0
    N = int(T/dt) + 1
    result = laplaceTransform(s, dt, T, N)
    print("Transformada de Laplace en s=", s, ": ", result)
