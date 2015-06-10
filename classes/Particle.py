#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from modules.ackley import f as ackley_f


class Particle(object):
    """Particle class : Ackley individual representation in PSACO algorithm"""

    def __init__(
        self,
        position=None,
        velocity=None,
        best_position=None,
        best_fitness=None,
        c1=None,
        c2=None,
        c3=None,
    ):
        self._position = position
        self._velocity = velocity
        self._best_position = best_position
        self._best_fitness = best_fitness
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3
        super(Particle, self).__init__()

    @property
    def position(self):
        return self._position

    @property
    def velocity(self):
        return self._velocity

    @property
    def best_position(self):
        return self._best_position

    @property
    def best_fitness(self):
        return self._best_fitness

    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2

    @property
    def c3(self):
        return self._c3

    @property
    def dimension(self):
        return len(self.position)

    def get_fitness(self):
        ackley_result = ackley_f(
            c1=self.c1,
            c2=self.c2,
            c3=self.c3,
            dimension=self.dimension,
            position=self.position
        )
        fitness = 1.0 / (1.0 + ackley_result)
        return fitness
