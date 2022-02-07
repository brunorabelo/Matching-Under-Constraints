from collections import defaultdict

from algorithms import task7
from algorithms.task7 import FixedPointAlgorithm
from instances import instance1
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


def task9():
    # example of using task9
    matching_table, schools, students = instance1.generate_matching_table_schools_and_students()
    result_task2_instance1 = task7.FixedPointAlgorithm(matching_table, schools, students, task9_constraints).execute()
    print(result_task2_instance1)


def algorithm_with_constraints(matching_table, schools, students):
    return FixedPointAlgorithm(matching_table, schools, students, task9_constraints).execute()


# print report plots
report(algorithm_with_constraints)
