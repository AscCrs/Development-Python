from operator import truediv

x = int(input("Ingrese el limite de elementos que ingresara en su arreglo: "))
lista = []
c = 0
y = 0

while c < x:
    y = int(input("Ingrese el elemento: " + str((c+1)) + ": "))
    lista.append(y)
    c += 1

print(lista)

for lis in lista: 
    print(lis)
