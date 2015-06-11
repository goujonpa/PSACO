#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from classes.Particle import Particle
from views.saveFigure import save_figure


class Population(object):
    """Population class : contains the Ackley individual represented by Particles"""

    def __init__(
        self,
        population=None,
        size=None,
        max_iter=None,
        max_fitness=None,
        global_best=None,
        best_global_fit=None,
        min_sd=None,
        current_sd=None,
        sd_dec=None,
        measure_iter=None,
        measure_best_fitness=None
    ):
        self._population = population
        self._size = size
        self._max_iter = max_iter
        self._max_fitness = max_fitness
        self._global_best = global_best
        self._best_global_fit = best_global_fit
        self._min_sd = min_sd
        self._current_sd = current_sd
        self._sd_dec = sd_dec
        self._measure_iter = measure_iter
        self._measure_best_fitness = measure_best_fitness
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
    def global_best(self):
        return self._global_best

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
        self._size = 50
        self._max_iter = 1000
        self._max_fitness = 0.9
        self._current_sd = 2.0
        self._min_sd = 0.001
        self._sd_dec = 0.90
        self._population = list()
        self._best_global_fit = 0.0
        for i in range(0, self.size):
            particle = Particle()
            particle._psaco_initialisation()
            if particle.get_fitness() > self._best_global_fit:
                self._global_best = particle
                self._best_global_fit = particle.get_fitness()
            self._population.append((particle, particle.get_fitness()))

    def _run_PSACO(self):
        t = 0
        self._measure_iter = []
        self._measure_best_fitness = []
        while t < self.max_iter:
            print('Iteration : {} / {}'.format(t, self.max_iter))
            self._measure_iter.append(t)
            self._measure_best_fitness.append(self._best_global_fit)
            t += 1
            new_population = list()
            for (particle, fitness) in self.population:
                new_particle = particle._update_position(
                    current_iteration=t,
                    max_iteration=self.max_iter,
                    global_best_position=self.global_best.position,
                    current_sd=self.current_sd
                )
                if new_particle.get_fitness() > self.best_global_fit:
                    self._global_best = new_particle
                    self._best_global_fit = new_particle.get_fitness()
                new_population.append((new_particle, new_particle.get_fitness()))
                self._current_sd *= self.sd_dec
                if self.current_sd < self.min_sd:
                    self._current_sd = self.min_sd
        self._measure_iter.append(t)
        self._measure_best_fitness.append(self._best_global_fit)
        measures = dict()
        measures['max_fit'] = self._measure_best_fitness
        save_figure(self._measure_iter, measures, 'simu')
        return self._global_best
