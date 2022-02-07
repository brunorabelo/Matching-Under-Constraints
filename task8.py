from algorithms import task7
from algorithms.task7 import FixedPointAlgorithm
from instances import instance2
from instances.instance2 import report


def task8_constraints(school, demand):
    return len(demand) <= school.capacity


def algorithm_with_constraints(matching_table, schools, students):
    return FixedPointAlgorithm(matching_table, schools, students, task8_constraints).execute()


def task8():
    # example of using task8
    matching_table, schools, students = instance2.generate_matching_table_schools_and_students()
    result_task2_instance1 = task7.FixedPointAlgorithm(matching_table, schools, students, task8_constraints).execute()
    print(result_task2_instance1)


# print report plots
print(report(algorithm_with_constraints))
