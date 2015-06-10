#!/usr/local/bin/python
# -*-coding:Utf-8 -*


class Population(object):
    """Population class : contains the Ackley individual represented by Particles"""

    def __init__(
        self,
        population=None,
        size=None,
        max_iter=None,
        max_fitness=None
        best_global_pos=None
        best_global_fit=None
        max_inertia=None
        min_inertia=None
        max_velocity=None
        min_velocity=None
        cognitive_scaling=None
        social_scaling=None
        min_sd=None
        current_sd=None
        sd_dec=None
    ):
        self._population = population
        self._size = size
        self._max_iter = max_iter
        self._max_fitness = max_fitness
        self._best_global_pos = best_global_pos
        self._best_global_fit = best_global_fit
        self._max_inertia = max_inertia
        self._min_inertia = min_inertia
        self._max_velocity = max_velocity
        self._min_velocity = min_velocity
        self._cognitive_scaling = cognitive_scaling
        self._social_scaling = social_scaling
        self._min_sd = min_sd
        self._current_sd = current_sd
        self._sd_dec = sd_dec
        super(Population, self).__init__()
