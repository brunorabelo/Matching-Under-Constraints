from algorithms.task2 import DeferredAcceptanceAlgo
from instances.instance2 import generate_report


def algorithm(matching_table, schools, students):
    return DeferredAcceptanceAlgo(matching_table, schools, students).execute()


generate_report(algorithm)
