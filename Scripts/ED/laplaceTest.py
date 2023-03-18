import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def laplace_inverse(F, a, b, N):
    # Definición de los pesos y nodos de la cuadratura de Gauss
    # x son los nodos 
    # w los pesos que tendran en un orden de N
    x, w = np.polynomial.legendre.leggauss(N)

    # Cálculo de la integral
    integral = 0 # Esta variable acumula la contribución de cada uno de los nodos

    for i in range(N):
        integral += w[i] * F((b - a) / 2 * x[i] + (a + b) / 2)
    
    # Multiplicar por el factor de escala (b - a) / 2
    integral *= (b - a) / 2
    
    # Imprimir la integral y graficar la función
    print("El valor de la integral es:", integral)
    
    # Crear un vector de valores x para graficar la función
    x_vals = np.linspace(a, b, 1000)
    
    # Evaluar la función F en los valores x
    y_vals = [F(x) for x in x_vals]

    # Graficar la función
    plt.plot(x_vals, y_vals)
    plt.title("Transformada de Laplace inversa " + str(F_str))
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.show()

sp.init_printing()

# Ingreso de la función de la transformada
F_str = input("Ingrese la función de la transformada de Laplace (en términos de s): ")
s = sp.symbols('s')
t = sp.symbols('t', positive=True)
F = sp.lambdify(s, F_str)  # Definir la función de la transformada de Laplace
F_str = sp.inverse_laplace_transform(F_str, s, t)  # Transformación inversa de la transformada de Laplace

# Ingreso de los parámetros
a = float(input("Ingrese el valor del limite inferior a: "))
b = float(input("Ingrese el valor del limite superior b: "))
N = int(input("Ingrese el número de puntos N: "))

laplace_inverse(F, a, b, N)
