class Vertice:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None 
        self.distancia = float('inf')

    def agregarVerticeAd(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append(v, p)

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a]

