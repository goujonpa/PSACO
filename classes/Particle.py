#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from modules.ackley import f as ackley_f
from math import pi
from random import uniform as randuniform


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
        dimension=None,
        max_inertia=None,
        min_inertia=None,
        max_velocity=None,
        min_velocity=None,
        cognitive_scaling=None,
        social_scaling=None
    ):
        self._position = position
        self._velocity = velocity
        self._best_position = best_position
        self._best_fitness = best_fitness
        self._max_inertia = max_inertia
        self._min_inertia = min_inertia
        self._max_velocity = max_velocity
        self._min_velocity = min_velocity
        self._cognitive_scaling = cognitive_scaling
        self._social_scaling = social_scaling
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3
        self._dimension = dimension
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
    def dimension(self):
        return self._dimension

    @property
    def max_inertia(self):
        return self._max_inertia

    @property
    def min_inertia(self):
        return self._min_inertia

    @property
    def max_velocity(self):
        return self._max_velocity

    @property
    def min_velocity(self):
        return self._min_velocity

    @property
    def cognitive_scaling(self):
        return self._cognitive_scaling

    @property
    def social_scaling(self):
        return self._social_scaling

    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2

    @property
    def c3(self):
        return self._c3

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

    def _psaco_initialisation(self):
        self._c1 = 20.0
        self._c2 = 0.2
        self._c3 = 2.0 * pi
        self._dimension = 30
        self._min_velocity = -2.0
        self._max_velocity = 2.0
        self._max_inertia = 0.7
        self._min_inertia = 0.4
        self._cognitive_scaling = 2
        self._social_scaling = 2
        self._position = []
        self._velocity = []
        for i in range(0, self.dimension):
            self._position.append(randuniform(-15.0, 15.0))
        for i in range(0, self.dimension):
            self._velocity.append(randuniform(self.min_velocity, self.max_velocity))
