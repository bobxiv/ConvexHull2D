import matplotlib.pyplot as plt
from point import Point
from utilities import random_points
from quick_hull import quick_hull, draw_points, flecha
from math import cos, sin, radians
from time import time

# points_mode puede ser "random" (puntos en un cuadrado
# centrado en el origen y con distribucion
# uniforme) o "circle"
points_mode = "random"

if points_mode == "random":
    cant = 1000
    xlim = [-1000, 1000]
    ylim = [-1000, 1000]
    points = random_points(cant, xlim, ylim)

if points_mode == "circle":
    points = []
    for dd in range(0, 3600, 10):
        d = dd/10.
        x = 100*cos(radians(d))
        y = 100*sin(radians(d))
        points.append(Point(x, y))

# vectors tiene las aristas del convex hull
# desordenadas (pero apuntando en la direccion
# correcta). Se puede hacer un algoritmo
# n*log(n) para pasar de esa lista de vectores
# a la lista de los puntos ordenada.
ini = time()
vectors = quick_hull(points)
fin = time()

print("Time: %f seconds." % (fin - ini))

draw_points(points)
for v in vectors:
    flecha(v[0], v[1])

plt.show()
