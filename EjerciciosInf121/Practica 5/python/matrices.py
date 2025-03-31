class Matriz:
    def __init__(self, e):
        self.e = e
    def sumar(self, o):
        if self.filas() != o.filas() or self.columnas() != o.columnas():
            return None
        r = []
        for i in range(self.filas()):
            fila = []
            for j in range(self.columnas()):
                fila.append(self.e[i][j] + o.e[i][j])
            r.append(fila)
        return Matriz(r)
    def filas(self):
        c = 0
        for _ in self.e:
            c += 1
        return c
    def columnas(self):
        c = 0
        for _ in self.e[0]:
            c += 1
        return c
    def mostrar(self):
        for fila in self.e:
            for v in fila:
                print(v, end=" ")
            print()
m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
m3 = m1.sumar(m2)
if m3:
    m3.mostrar()