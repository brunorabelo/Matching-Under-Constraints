from collections import defaultdict

from algorithms.task7 import FixedPointAlgorithm
from instances.instance2 import report


def task9_constraints(school, demand):
    # maximum quota constraint
    current_group_quantity = defaultdict(int)
    for student in demand:
        current_group_quantity[student.group] += 1
    for group, quota in school.quota_group.items():
        if current_group_quantity > quota:
            return False
    # capacity constraint
    return len(demand) <= school.capacity


def algorithm_with_constraints(matching_table, schools, students):
    return FixedPointAlgorithm(matching_table, schools, students, task9_constraints).execute()


report(algorithm_with_constraints)
