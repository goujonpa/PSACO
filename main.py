#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from classes.Population import Population
from classes.Particle import Particle


def run():
    population = Population()
    population._psaco_initialisation()
    result = population._run_PSACO()
    best = result[0]
    iteration = result[1]
    print('{} : {} at {}'.format(best.position, best.get_fitness(), iteration))

run()
