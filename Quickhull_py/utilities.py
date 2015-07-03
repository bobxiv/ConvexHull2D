from point import Point
from random import random

def random_point(xlim=[-10,10], ylim=[-10,10]):
    dx = xlim[1] - xlim[0]
    dy = ylim[1] - ylim[0]
    x = xlim[0] + random() * dx
    y = ylim[0] + random() * dy
    return Point(x, y)

def random_points(cant=20, xlim=[-10,10], ylim=[-10,10]):
    points = [random_point(xlim, ylim) for i in range(cant)]
    return points
