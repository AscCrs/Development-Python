from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

t = symbols('t')
s = symbols('s')
print("Transformada simbolica")
ft = t ** 2 * cos(t)
F = laplace_transform(ft, t, s)
print(F)

def laplace_transform():
    fs = 10 # frecuencia de muestreo (Hz)
    h = 1/fs # periodo de muestreo (seg)
    Nomuestras = 100 # numero de muestras en el tiempo
    freqmax = fs/2 # Hz
    sigm = 1.5 # abcisa de convergencia
    k = 1
    paso = 0.1 # incremento de la variable de Laplace
    ww = 0
    ppe = np.zeros(Nomuestras+1)
    xx = np.zeros(Nomuestras+1)
    Laplacer = np.zeros(int(freqmax/paso)+ Nomuestras)
    Laplacei = np.zeros(int(freqmax/paso)+ Nomuestras)
    for fo in np.arange(-freqmax, freqmax+paso, paso):
        Laplar = 0 # parte real
        Laplai = 0 # parte imaginaria
        for it in range(1, Nomuestras+1):
            i = int(it)
            t = i * h # instante de muestreo
            #pp = lambda i: t
            ppe[i] = t
            xt = t**2 * cos(t) # funcion del tiempo a encontrar su LT
            Laplar = xt*exp(-sigm*t)*np.cos(2*pi*fo*t)*h+Laplar
            Laplai = (-1)*xt*exp(-sigm*t)*np.sin(2*pi*fo*t)*h+Laplai
            #xxi = lambda i: xt # eje de la funcion
            xx[i] = xt
        #Laplacerlam = lambda k: Laplar
        Laplacer[k - 1] = Laplar
        #Laplaceilam = lambda k: Laplai
        Laplacei[k - 1] = Laplai

        ww = 2*pi*fo # eje de frecuencias
        k += 1

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    ax1.plot(ppe, xx)
    ax1.axis([0, 2, -2, 2])
    ax1.set_title('Funcion f(t)')
    p = 1
    print("Parte real")
    print(Laplacer)
    print("Parte imaginaria")
    print(Laplacei)
    sigma = 1.5
    Lainversatr=0;
    Lainversati=0;
    Lainversar = np.zeros(500)
    Lainversai = np.zeros(500)
    tte = np.zeros(500)
    for v in np.arange(-freqmax, freqmax+paso, paso):
        for m in range(1, Nomuestras+2):
            t = m*h
            #tt = lambda m: t
            tte[m - 1] = t
            laplainvr = Laplacer[p - 1]*np.exp(sigma*t)*np.cos(2*np.pi*v*t)*paso
            laplainvr = laplainvr - Laplacei[p - 1]*np.exp(sigma*t)*np.sin(2*np.pi*v*t)*paso
            laplainvi = Laplacei[p - 1]*np.exp(sigma*t)*np.cos(2*np.pi*v*t)*paso
            laplainvi = laplainvi + Laplacer[p - 1]*np.exp(sigma*t)*np.sin(2*np.pi*v*t)*paso
            #Lainversare = lambda m: laplainvr
            #Lainversaim = lambda m: laplainvi
            Lainversar[m - 1] = laplainvr
            Lainversai[m - 1] = laplainvi

        if v == 5:
            # graficar parte real en eje ax2_1
            ax2_1 = ax2.twinx()
            ax2_1.plot(tte, Lainversar, color='red')
            ax2_1.axis([0, 2, -0.1, 0.1])
            ax2_1.set_ylabel('Re[Componente de 5Hz]', color='red')

            # graficar parte imaginaria en eje ax2_2
            ax2_2 = ax2.twinx()
            ax2_2.spines["right"].set_position(("axes", 1.1))
            ax2_2.plot(tte, Lainversai, color='blue')
            ax2_2.axis([0, 2, -0.1, 0.1])
            ax2_2.set_ylabel('Im[Componente de 5Hz]', color='blue')

            # configurar título del eje ax2
            ax2.set_title('Componente de 5Hz')
    
        Lainversatr = Lainversatr + Lainversar
        Lainversati = Lainversati + Lainversai
        p = p + 1
    plt.show()

laplace_transform()