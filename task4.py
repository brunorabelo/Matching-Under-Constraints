from algorithms.task2 import DeferredAcceptanceAlgo
from instances.instance2 import report


def algorithm(matching_table, schools, students):
    return DeferredAcceptanceAlgo(matching_table, schools, students).execute()


report(algorithm)
