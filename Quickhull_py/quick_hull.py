import matplotlib.pyplot as plt
from operator import sub
from pprint import pprint
from random import random
from Queue import Queue
from point import Point

def quick_hull(P_):
    """
    quick_hull recibe una lista de puntos y devuelve
    una lista de vectores (que son representados
    simplemente como pares de puntos) que forma
    el convex hull de los puntos en orden ccw
    """
    # Si P_ tiene un solo punto, devuelvo un vector
    # que empieza y termina en ese punto. Esto es
    # solamente por consistencia
    if len(P_) == 1:
        return ((P_[0], P_[0]))

    # Si P_ tiene dos puntos, devuelvo los dos vectores
    # que forman. Esto se hace asi por consistencia con
    # lo que hace el algoritmo para puntos alineados (ver
    # mas abajo)
    elif len(P_) == 2:
        return ((P_[0], P_[1]), (P_[1], P_[0]))
    
    # Ordeno los puntos lexicograficamente.
    # TODO: Esto es n*log(n), pero como en realidad
    # solo quiero el que esta mas a la izquierda
    # y el que esta mas a la derecha, podria hacerse
    # en una pasada de n iteraciones.
    P = sorted(P_)

    # Uso una queue para hacer la recursividad.
    # No hago una funcion recursiva para evitarme
    # problemas de limites de recursiones.
    vector_queue = Queue()

    # Una lista de vectores (pares de puntos)
    vectors = []

    # Encuentro el que esta mas a la izquierda,
    # mas a la derecha y mas arriba
    far_left = P[0]
    far_right = P[-1]

    # Meto el vector que apunta de la izquierda a
    # la derecha, y el que apunta de la derecha a
    # la izquierda, en la queue.
    # Esto es mas elegante, pero para puntos alineados
    # devuelve esos dos vectores, que puede no ser deseable.
    vector_queue.put((far_right, far_left))
    vector_queue.put((far_left, far_right))

    
    while not vector_queue.empty():
        # Saco un vector de la queue y busco el punto
        # que esta mas a la izquierda
        p1, p2 = vector_queue.get()
        p3_i, z = p1.leftest(p2, P)

        # Si no hay nada a la izquierda, el par
        # de puntos pertenece al CH
        # Si hay, elimino todos los puntos dentro
        # del triangulo que forman los dos puntos
        # de mi vector y el punto encontrado.
        # despues agrego los dos vectores que se forman
        # entre los puntos de mi vector y el nuevo punto,
        # de forma que se mantenga el sentido clockwise.
        if p3_i == -1:
            vectors.append((p1, p2))
        else:
            p3 = P[p3_i]
            clean_triangle(p1, p3, p2, P)
            vector_queue.put((p1, p3))
            vector_queue.put((p3, p2))

    return vectors

def clean_triangle(p1, p2, p3, P):
    indexes_to_remove = []

    for i, p in enumerate(P):
        r12 = p1.right_turn(p2, p)
        r23 = p2.right_turn(p3, p)
        r31 = p3.right_turn(p1, p)

        if r12 and r23 and r31:
            indexes_to_remove.append(i)

    for i in reversed(indexes_to_remove):
        P.pop(i)

def flecha(p1, p2):
    """Draws an arrow from p1 to p2"""
    plt.arrow(p1.x, p1.y,
              p2.x-p1.x, p2.y-p1.y)

def draw_points(points):
    x = [p.x for p in points]
    minx = min(x)
    maxx = max(x)
    dx = maxx - minx

    y = [p.y for p in points]
    miny = min(y)
    maxy = max(y)
    dy = maxy - miny

    plt.plot(x, y, 'o')
    plt.xlim(minx - 0.1*dx, maxx + 0.1*dx)
    plt.ylim(miny - 0.1*dy, maxy + 0.1*dy)
