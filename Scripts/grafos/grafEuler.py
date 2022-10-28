# !Clase que define un vertice
class vertice:
    # Constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.VerticeAd = [] # Conexión con otros nodos
    
    def agregaVerticeAd(self, n):
        if n not in self.VerticeAd:
            self.VerticeAd.append(n)

# Clase que define a una gráfica
class grafica:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, v): 
        if v not in self.vertices:
            # Vertices que tendra la gráfica
            self.vertices[v] = vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVerticeAd(b)
            self.vertices[b].agregaVerticeAd(a)

    def bfs(self, r):
        if r in self.vertices:
            cola = [r]

            self.vertices[r].visitado = True
            self.vertices[r].nivel = 0

            print("(" + str(r) + ", " + str(self.vertices[r].nivel) + ")")

            while (len(cola) > 0):
                act = cola[0]
                cola = cola[1:]

                for v in self.vertices[act].VerticeAd:
                    if self.vertices[v].visitado == False:
                        cola.append(v)
                        self.vertices[v].visitado = True
                        self.vertices[v].nivel = self.vertices[act].nivel + 1
                        
                        print("(" + str(v) + ", " + str(self.vertices[v].nivel) + ")")

def main():

    g = grafica()

    # Lista que muestra los vertices
    l = [0, 1, 2, 3, 4, 5, 6]
    for n in l:
        g.agregaVertice(n)

    # Lista que muestra las aristas en función de los vertices
    #l = [2, 0, 0, 6, 6, 3, 0, 5, 6, 5, 6, 5, 0, 1, 6, 4, 1, 4]
    l = [1, 4, 4, 3, 4, 6, 3, 5, 3, 2, 6, 5, 5, 2]
    for i in range(0, len(l) -1, 2):
        g.agregarArista(l[i], l[i + 1])

    for v in g.vertices:
        print(v, g.vertices[v].VerticeAd)

    print("\n")

    g.bfs(2)

main()
    