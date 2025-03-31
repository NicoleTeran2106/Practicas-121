class Vector:
    def __init__(self, e):
        self.e = e
    
    def sumar(self, o):
        if self.t() != o.t():
            return None
        r = []
        for i in range(self.t()):
            r.append(self.e[i] + o.e[i])
        return Vector(r)

    def t(self):
        c = 0
        for _ in self.e:
            c += 1
        return c
    
    def mostrar(self):
        for i in self.e:
            print(i, end=" ")
        print()
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1.sumar(v2)
if v3:
    v3.mostrar()
