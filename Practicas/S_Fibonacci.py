sucesion = input("Ingrese: (S) límite máximo, (N) número de \
términos? ")

if sucesion == 'S':
    def fib(n):
        a, b = 0,1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
    m = int(input("Límite máximo~> "))   
    fib(m)

elif sucesion == 'N':
    a, b = 0,1
    n = int(input("Número de términos~> "))
    for i in range(n):
        print(i, a)
        a, b = b, a + b

else:
    print("Debe ingresar S o N")