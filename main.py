#!/usr/local/bin/python
# -*-coding:Utf-8 -*

from classes.Population import Population
from classes.Particle import Particle


def run():
    population = Population()
    population._psaco_initialisation()
    best = population._run_PSACO()
    print('{} : {}'.format(best.position, best.get_fitness()))

run()
