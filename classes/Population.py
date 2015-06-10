#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from classes.Particle import Particle


class Population(object):
    """Population class : contains the Ackley individual represented by Particles"""

    def __init__(
        self,
        population=None,
        size=None,
        max_iter=None,
        max_fitness=None,
        best_global_pos=None,
        best_global_fit=None,
        min_sd=None,
        current_sd=None,
        sd_dec=None
    ):
        self._population = population
        self._size = size
        self._max_iter = max_iter
        self._max_fitness = max_fitness
        self._best_global_pos = best_global_pos
        self._best_global_fit = best_global_fit
        self._min_sd = min_sd
        self._current_sd = current_sd
        self._sd_dec = sd_dec
        super(Population, self).__init__()

    @property
    def population(self):
        return self._population

    @property
    def size(self):
        return self._size

    @property
    def max_iter(self):
        return self._max_iter

    @property
    def max_fitness(self):
        return self._max_fitness

    @property
    def best_global_pos(self):
        return self._best_global_pos

    @property
    def best_global_fit(self):
        return self._best_global_fit

    @property
    def min_sd(self):
        return self._min_sd

    @property
    def current_sd(self):
        return self._current_sd

    @property
    def sd_dec(self):
        return self._sd_dec

    def _psaco_initialisation(self):
        self._size = 10
        self._max_iter = 3000
        self._max_fitness = 0.9
        self._current_sd = 1.0
        self._min_sd = 0.01
        self._sd_dec = 0.75
        self._population = []
        for i in range(0, self.size):
            particle = Particle()
            particle._psaco_initialisation()
            self._population.append((particle, particle.get_fitness()))
