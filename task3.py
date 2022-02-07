from algorithms.task2 import DeferredAcceptanceAlgo
from instances import instance3


def algorithm(matching_table, schools, students):
    return DeferredAcceptanceAlgo(matching_table, schools, students).execute()


x_array, group_array = instance3.report(algorithm)
