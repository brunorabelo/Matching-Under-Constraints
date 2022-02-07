from algorithms.task7 import FixedPointAlgorithm
from instances.instance2 import generate_report


def task8_constraints(school, demand):
    return len(demand) <= school.capacity


def algorithm_with_constraints(matching_table, schools, students):
    return FixedPointAlgorithm(matching_table, schools, students, task8_constraints).execute()


generate_report(algorithm_with_constraints)
