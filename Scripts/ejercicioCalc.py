num_contagios = 0.9025 #Esta variable almacena el valor que multiplicara a "e"
val_e = 2.7182818284590452353602874713527 # Esta variable almacena el valor de e
pot = 0.3321 #Esta variable almacena el valor de la potencia a la que e sera elevada
x = 1 # X almacena el número de días transcurridos
val_f = 0 # Esta variable almacena el valor de la función

print("Inciso A), B), C) y D)\n")

while x < 31:  #Bucle que se encarga de calcular la función de X desde 1 a 30
    val_f = num_contagios*pow(val_e, pot*x)
    val_f = str(val_f)
    print("El día " + str(x) + " el número de contagios fue de: " + val_f)
    x = x + 1

def prev1(): # Función de programación que calcula el valor de X desde 98 a 100
    x = 98
    while x < 101:
        val_f = num_contagios*pow(val_e, pot*x)
        val_f = str(val_f)
        print("\nEl día " + str(x) + " el número de contagios fue de: " + val_f)
        x = x + 1

def prev2(): # Funcion de programacion que calcula el valor de X desde 98 a 100 usando la 2da formula
    cont = 0.8913
    exp = 0.3112
    evit_c = 0
    x2 = 98
    while x2 < 101:
        evit_c = cont*pow(val_e, exp*x2)
        evit_c = str(evit_c)
        print("\nEl día " + str(x2) + " el número de contagiados se siguieran los metodos preventivos sería de: " + evit_c)
        x2 = x2 + 1

def prev3():  # Función de programación que se encarga de calcular el valor de X desde 28 a 30
    cont = 0.8913
    exp = 0.3112
    evit_c = 0
    x2 = 28
    while x2 < 31:
        evit_c = cont*pow(val_e, exp*x2)
        evit_c = str(evit_c)
        print("\nEl día " + str(x2) + " el número de contagiados se siguieran los metodos preventivos sería de: " + evit_c)
        x2 = x2 + 1

print("-------------------------------------------------------------")
print("Inciso e)\n")
prev1()
print("-------------------------------------------------------------")
print("Inciso f)\n")
prev3()
print("-------------------------------------------------------------")
print("Inciso e)\n")
prev2()
print("-------------------------------------------------------------")

print("Inciso e)\n")

cont_sin = 123000976614520.67 + 171450105679656.34 + 238982970270944.34

cont_med = 15666186697235.61 + 21385319377674.84 + 29192291252717.79 

cont_pev = cont_sin - cont_med

print("El número de contagios totales prevenidos durante los 98, 99 y 100 días es de = " + str(cont_pev))

print("-------------------------------------------------------------")

print("Inciso f)\n")

cont_sin = 9859.723565249355 + 13743.392075105121 + 19156.80743786506

cont_med = 5423.658095562562 + 7403.6306862973615 + 10106.416439474777

cont_pev = cont_sin - cont_med

print("El número de contagios totales prevenidos durante los 28, 29 y 30 días es de = " + str(cont_pev))