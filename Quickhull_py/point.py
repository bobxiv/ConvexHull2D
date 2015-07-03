# Point tiene dos metodos importantes:
#
# leftest, que recibe otro punto y una
# lista de puntos y devuelve el indice
# del punto que esta mas a la izquierda
# del vector formado por los dos puntos,
# y -1 si no hay ningun punto a la izquierda.
# Tambien devuelve el area del paralelogramo
# que forman, con signo.
#
# right_turn, que recibe otros dos puntos
# y devuelve True si hacen un giro a la derecha
# y False si estan alineados o giran a la
# izquierda.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def leftest(self, p2, P):
        v1 = p2 - self
        max_z = 0
        max_i = -1
        for i, p in enumerate(P):
            v2 = p - self
            z = self._cross_product(v1, v2)
            if z > max_z:
                max_z = z
                max_i = i
        return (max_i, max_z)

    def right_turn(self, p2, p3):
        v1 = p2 - self
        v2 = p3 - p2
        return self._cross_product(v1, v2) < 0

    def _cross_product(self, v1, v2):
        return v1.x * v2.y - v1.y * v2.x

    def __lt__(self, p):
        return ((self.y < p.y) if (self.x == p.x) else (self.x < p.x))
    def __sub__(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return Point(dx, dy)

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)
    def __repr__(self):
        return self.__str__()


#---------------------------------

