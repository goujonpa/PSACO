#!/usr/local/bin/python
# -*-coding:Utf-8 -*


class Population(object):
    """Population class : contains the Ackley individual represented by Particles"""

    def __init__(self, arg):
        super(Population, self).__init__()
        self.arg = arg
