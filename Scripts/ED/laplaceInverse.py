import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy import integrate
from numpy import real
from numpy import cos
from numpy import pi
from numpy import exp

# t: el paso de tiempo para calcular la función inversa
#
# x: cualquier punto real arbitrario que no tenga singularidades a su derecha en el plano complejo.
#
# tolerance: la tolerancia para la precisión
#
# outProcess: una bandera; colóquelo en valores no nulos para obtener los resultados intermedios.


# Se utiliza el metodo de cuadratura de Gauss-Kronrod de orden 15
def inverseLaplace(F, t, x, outProcess=0, tolerance=1e-8):
    lSegm = 5.0 / t  # Segmentos inciales de integracion
    # Se definen los limites de la integral
    lowerLim = 0
    upperLim = lowerLim + lSegm
    # Definir el integrando basado en la función de argumento
    integF = lambda u: real(F(complex(x + 1j * u))) * cos(u * t)
    # Ejecutar la primera integración fuera del ciclo
    lastRes = 0
    actRes = (2.0 * exp(x * t) / pi) * integrate.quad(
        integF, lowerLim, upperLim
    )[0]
    segmentIter = 1
    exceptZero = 1e-15  # Un número muy pequeño para evitar la división por cero
    relError = abs(abs(actRes) - abs(lastRes)) / abs(lastRes + exceptZero)

    # Ejecutar iterativamente la integración
    while relError > tolerance:
        segmentIter = segmentIter + 1
        lowerLim = upperLim
        upperLim = upperLim + lSegm
        lastRes = actRes
        actRes = (
            actRes
            + (2.0 * exp(x * t) / pi)
            * integrate.quad(integF, lowerLim, upperLim)[0]
        )
        relError = abs(abs(actRes) - abs(lastRes)) / (abs(lastRes) + exceptZero)

    if outProcess == 0:
        print("t{t} Calculado con {segmentRuns} segmentos de integracion, con un limite superior de {upperBound}")
        print("Resultado={integIter}")

    return actRes


######### Graficando la inversa numérica
# Graficando los puntos de datos que se calculan analíticamente

if __name__ == "__main__":
    s = sp.symbols("s")
    f_str = input("Ingrese la función de la transformada de Laplace (como cadena de caracteres): ")
    f_str = 1 / (s**2 + 1)

    # Ingreso de los parámetros
    x0 = float(input("Ingrese el valor del inicio de tiempo: "))
    xf = float(input("Ingrese el valor del limite de tiempo: "))
    p = float(input("Ingrese el tamaño de cada paso: "))
    x0 = 0.2
    xf = 3
    p = 0.2

    tList = np.arange(x0, xf, p)  # Rango de valores sobre los cuales se va a realizar el calculo
    f = sp.lambdify(s, f_str)

    yList_numerical = []
    for t in tList:
        y = inverseLaplace(f, t, 1, 1)
        yList_numerical.append(y)

    plt.plot(tList, yList_numerical)
    plt.title("Transformada de Laplace inversa " + str(f_str))
    plt.xlabel("t")
    plt.ylabel("f(t)")
    plt.show()