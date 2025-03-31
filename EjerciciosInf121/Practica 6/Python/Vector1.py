class Vector:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def __add__(self, other):
        return Vector(self.a1 + other.a1, self.a2 + other.a2, self.a3 + other.a3)

    def __sub__(self, other):
        return Vector(self.a1 - other.a1, self.a2 - other.a2, self.a3 - other.a3)

    def __mul__(self, scalar):
        return Vector(self.a1 * scalar, self.a2 * scalar, self.a3 * scalar)

    def __matmul__(self, other):
        return Vector(
            self.a2 * other.a3 - self.a3 * other.a2,
            self.a3 * other.a1 - self.a1 * other.a3,
            self.a1 * other.a2 - self.a2 * other.a1
        )

    def longitud(self):
        return (self.a1**2 + self.a2**2 + self.a3**2) ** 0.5

    def normalizar(self):
        longitud = self.longitud()
        return Vector(self.a1 / longitud, self.a2 / longitud, self.a3 / longitud)

    def producto_escalar(self, other):
        return self.a1 * other.a1 + self.a2 * other.a2 + self.a3 * other.a3

    def es_ortogonal(self, other):
        return self.producto_escalar(other) == 0

    def proyeccion_sobre(self, other):
        escalar = self.producto_escalar(other) / other.producto_escalar(other)
        return other * escalar

    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"


def main():
    a = Vector(3, 4, 5)
    b = Vector(2, 1, 3)

    suma = a + b
    print("la Suma de A y B:", suma)

    escalar_multiplicado = a * 2
    print("A multiplicado por 2:", escalar_multiplicado)

    longitud_a = a.longitud()
    print("Longitud de A:", longitud_a)

    normal_a = a.normalizar()
    print("vector A normalizado:", normal_a)

    producto_escalar = a.producto_escalar(b)
    print("Producto escalar de A y B:", producto_escalar)

    producto_vectorial = a @ b
    print("producto vectorial de A y B:", producto_vectorial)

    ortogonal = a.es_ortogonal(b)
    print("A es ortogonal a B?", ortogonal)
if __name__ == "__main__":
    main()