import numpy as np
from scipy.integrate import simps
from sympy.abc import s
import matplotlib.pyplot as plt
import sympy as sp

"""
Aproximacion de la transformada de laplace de la funcion f(t) utilizando el 
metodo de Simpson
"""
def laplace_transform(func, t, s):
    F = np.zeros_like(s)
    for i, si in enumerate(s):
        integrand = lambda t: func(t) * np.exp(-si *  t)
        F[i] = simps(integrand(t), t)
    return F

def func(t):
    return t**2

t = np.linspace(0, 10, 1000)
s = np.array([1 + 1j, 2 + 2j, 3 + 3j])

F = laplace_transform(func, t, s)
print(F)

"""
Aproximación de una transformada inversa de laplace utilizanndo el
metodo de Gauss 
"""
# def gauss_laplace_inverse(f, T, N):
#     """
#     Calcula la transformada inversa de Laplace de una función F(s) utilizando el método de cuadratura de Gauss.

#     Parámetros:
#     F (función): la función de Laplace F(s).
#     T (float): el valor de t en el que se quiere evaluar la función inversa de Laplace.
#     N (int): el número de puntos de la cuadratura de Gauss a utilizar.

#     Retorna:
#     El valor de la función inversa de Laplace evaluada en t.
#     """

#     # Definimos la función a integrar
#     def integrand(u):
#         return f(u) * np.exp(u*T)

#     # Calculamos los puntos y pesos de la cuadratura de Gauss
#     x, w = np.polynomial.legendre.leggauss(N)

#     # Convertimos los puntos de la cuadratura de Gauss a nuestro intervalo de integración
#     a = -1
#     b = 1
#     t = 0.5*(b-a)*x + 0.5*(b+a)

#     # Evaluamos la función en los puntos de la cuadratura de Gauss y multiplicamos por los pesos correspondientes
#     integrand_values = integrand(t)
#     integral_value = np.dot(w, integrand_values)

#     # Dividimos por pi para obtener la función inversa de Laplace
#     result = integral_value / np.pi

#     return result

# def f(s):
#     return 1 / np.sqrt(s**2 + 1)

# result = gauss_laplace_inverse(f, 8, 12)
# print(result)


# def euler_method():
#     # Ingreso de la función de la transformada
#     F_str = input("Ingrese la función de la transformada de Laplace (como cadena de caracteres): ")
#     F = lambda x: eval(F_str)  # Definir la función de la transformada de Laplace
    
#     # Ingreso de los parámetros
#     x0 = float(input("Ingrese el valor inicial x0: "))
#     y0 = float(input("Ingrese el valor inicial y0: "))
#     h = float(input("Ingrese el tamaño del paso h: "))
#     N = int(input("Ingrese el número de iteraciones N: "))
    
#     # Definición del arreglo de puntos
#     x = np.zeros(N+1)
#     y = np.zeros(N+1)
#     x[0] = x0
#     y[0] = y0
    
#     # Cálculo de los puntos usando el método de Euler
#     for n in range(N):
#         y[n+1] = y[n] + h * np.real(F(x[n])[0]) 
#         print(F(x[n]))
#         x[n+1] = x[n] + h
    
#     # Imprimir los puntos
#     print("Puntos calculados:")
#     for n in range(N+1):
#         print(f"x_{n} = {x[n]:.4f}   y_{n} = {y[n]:.4f}")

# euler_method()


# def f(x,y):
#     return evalf(func)

# def euler(f, x0, y0, h, t):
#     # Calculamos el número de iteraciones necesarias
#     n = t
    
#     # Inicializamos los arreglos de x e y
#     x = np.zeros(n+1)
#     y = np.zeros(n+1)
    
#     # Asignamos los valores iniciales de x e y
#     x[0] = x0
#     y[0] = y0
    
#     # Iteramos para encontrar los valores de x e y en cada paso
#     for i in range(1, n+1):
#         x[i] = x[i-1] + h
#         y[i] = y[i-1] + h * np.real(f(x[i-1], y[i-1])[0])

#     print("Puntos calculados:")
#     for n in range(n+1):
#         print(f"x_{n} = {x[n]:.4f}   y_{n} = {y[n]:.4f}")
        
#     return x, y

# s = sp.symbols('s')
# t = sp.symbols('t', positive=True)

# func = 1/(s+1)

# func = sp.inverse_laplace_transform(func, s, t)
# print(func)

# # Parámetros del problema
# x0 = 0
# y0 = 0
# h = 0.1
# t = 5

# x, y = euler(f, x0, y0, h, t)

# # Calculamos la transformada inversa de Laplace para cada valor de x
# result = np.zeros(x.shape)
# for i in range(x.shape[0]):
#     result[i] = eval(func.replace("s", str(x[i])))  

# print(x)
# print(y)


# plt.plot(result)
# plt.title("Solución de la transformada inversa de Laplace de " + func)
# plt.xlabel("Índice de tiempo")
# plt.ylabel("Valor de la función")
# plt.show()

import matplotlib.pyplot as plt

# def inverse_laplace(transform, t_final, h):
#     """
#     Función que resuelve la transformada inversa de Laplace de una función utilizando el método de Euler.
    
#     transform: cadena de caracteres que representa la transformada de Laplace de la función.
#     t_final: tiempo final de simulación.
#     h: tamaño de paso de la simulación.
    
#     return: dos arrays, uno con los valores de tiempo y otro con los valores de la función.
#     """
    
#     # Definimos la función de la transformada inversa.
#     def f(y, t):
#         s = y
#         F = eval(transform)
#         return F
    
#     # Definimos el valor inicial y el vector de tiempo.
#     y0 = np.array([0])
#     t = np.arange(0, t_final + h, h)
    
#     # Resolvemos la EDO con el método de Euler.
#     y = [y0]
#     for i in range(1, len(t)):
#         y.append(y[i-1] + h*(f(y[i-1], t[i-1]) + f(y[i-1] + h*f(y[i-1], t[i-1]), t[i]))/2)

#     print(y)
    
#     # Graficamos los resultados.
#     plt.plot(t, y)
#     plt.xlabel('Tiempo')
#     plt.ylabel('Función')
#     plt.title('Transformada inversa de Laplace')
#     plt.grid()
#     plt.show()
    
#     return t, y

# inverse_laplace('2/(s**2+4)', 100, 5)

def inverse_laplace(F, x0, y0, h, N):
    
    # Definición del arreglo de puntos
    x = np.zeros(N+1)
    y = np.zeros(N+1, dtype=np.complex128)
    x[0] = x0
    y[0] = y0
    
    # Cálculo de los puntos usando el método de Euler
    for n in range(N):
        y[n+1] = y[n] + h * (F(x[n]) + F(x[n+1])) / 2
        print(F(x[n]) + F(x[n+1]))
        x[n+1] = x[n] + h
    
    # Imprimir los puntos
    print("Puntos calculados:")
    for n in range(N+1):
        print(f"x_{n} = {x[n]:.4f}   y_{n} = {y[n].real:.4f} + {y[n].imag:.4f}j")
    
    # Graficar la función resultante
    plt.plot(x, y.real)
    plt.plot(x, y.imag)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Parte real', 'Parte imaginaria'])
    plt.show()
    
# Ingreso de la función de la transformada
F_str = input("Ingrese la función de la transformada de Laplace (como cadena de caracteres): ")
F = lambda s: eval(F_str)  # Definir la función de la transformada de Laplace


# Ingreso de los parámetros
x0 = float(input("Ingrese el valor inicial x0: "))
y0 = float(input("Ingrese el valor inicial y0: "))
h = float(input("Ingrese el tamaño del paso h: "))
N = int(input("Ingrese el número de iteraciones N: "))

inverse_laplace(F, x0, y0, h, N)