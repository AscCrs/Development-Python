c = 0 #Variable iteradora
rep_bu = True #Variable de control para el ciclo while

val = float(input("Ingrese el precio inicial del kilo de uva: "))

while rep_bu: #Validacion del precio inicial por kilo de uva
    if val > 0:
        c = 1
    else:
        print("El valor ingresado debe ser positivo")
        pre = input("Ingrese el valor inicial del kilo de uva: ")
        val = float(pre)
    rep_bu = (c < 0) #repeticion (emulacion do-while)

tipo = input("Ingrese el tipo de uva A o B: ")

while rep_bu: #Validacion del tipo de uva
    if tipo == 'A' or tipo == 'B' or tipo == 'a' or tipo == 'b':
        c = 1
    else:
        print("El valor tipo ingresado no coincide")
        tipo = input("Ingrese el tipo de uva: ")
    rep_bu = (c < 0)

tam = int(input("Ingrese el tamaño de la uva: "))

while rep_bu: #Validacion del tamaño de las uvas
    if tam == 1 or tam == 2:
        c = 1
    else:
        print("El tamaño de la uva debe ser 1 o 2")
        tam = int(input("Ingrese el tamaño de la uva: "))
    rep_bu = (c < 0)

kilo = float(input("Ingrese los kilos de uva: "))

while rep_bu: #validacion de los kilos de uva
    if kilo > 0:
        c = 1
    else:
        print("La cantidad de uva debe ser mayor que 0")
        kilo = float(input("Ingrese los kilos de uva: "))
    rep_bu = (c < 0)

if tipo == 'A' or tipo == 'a' and tam == 1: #condicional encargada de evaluar los casos de seleccion por tipo y tamaño
    val = (val + .20) * kilo
else:
    if tipo == 'A' or tipo == 'a' and tam == 2:
        val = 0
    else:
        if tipo == 'B' or tipo == 'b' and tam == 1:
            val = (val - .30) * kilo
        else:
            if tipo == 'B' or tipo == 'b' and tam == 2:
                val = (val - .50) * kilo
            else:
                val = 0
if val > 0: # Condicional encargada de escribir el resultado
    print("La ganancia obtenida por " + str(kilo) + "kg es de $" + str(val))