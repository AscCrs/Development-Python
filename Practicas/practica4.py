M = int(input("Ingrese la cantidad de automoviles producidos por México: "))

EU = int(input("Ingrese la cantidad de automoviles producidos por Estados Unidos: "))

C = int(input("Ingrese la cantidad de automoviles producidos por Canada: "))

porcM = round(M * 100 / (M + EU + C), 2)

print("El porcentaje de autos producidos por México es de " + str(porcM) + "%")

porcEU = round(EU * 100 / (M + EU + C), 2)

print("El porcentaje de autos producidos por Estados Unidos es de " + str(porcEU) + "%")

porcC = round(EU * 100 / (M + EU + C), 2)

print("El porcentaje de automoviles producidos por Canada es de " + str(porcC) + "%")