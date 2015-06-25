#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from math import pi
from math import sqrt
from math import exp
from math import cos


def f(c1=20, c2=0.2, c3=(2 * pi), dimension=None, position=None):
    """f function : calculate the result of Ackley function"""
    calcul = 0.0
    calcul2 = 0.0
    agregat = 0.0
    c1 = float(c1)
    c2 = float(c2)
    c3 = float(c3)

    for i in range(0, dimension):
        agregat += float(1.0 / dimension * pow(position[i], 2))
    calcul = sqrt(calcul)
    calcul = -c2 * calcul
    calcul = exp(calcul)
    calcul = -c1 * calcul
    agregat = 0.0
    for i in range(0, dimension):
        a = c3 * position[i]
        agregat += cos(a)
    calcul2 = (1.0 / dimension) * agregat
    calcul2 = -1.0 * exp(calcul2)
    result = calcul + calcul2 + c1 + exp(1)
    return float(result)
