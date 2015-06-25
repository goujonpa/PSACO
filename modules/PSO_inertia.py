#!/usr/local/bin/python
# -*-coding:Utf-8 -*


def PSO_inertia(current_iteration, max_iteration, min_inertia, max_inertia):
    inertia = float(max_inertia - min_inertia) * (float(max_iteration - current_iteration)) / float(max_iteration)
    inertia += min_inertia
    return float(inertia)
