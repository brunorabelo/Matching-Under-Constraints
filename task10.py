from collections import defaultdict

import utils
from algorithms.task7 import FixedPointAlgorithm
from algorithms.task5 import get_rational_group_students
from instances.instance2 import report


def get_groups_from_schools(schools):
    return schools[0].quota_group.keys()


def algorithm_with_constraints(matching_table, schools, students):
    def task10_constraints(school, demand):
        rational = get_rational_group_students(students, )
        # capacity constraint
        return len(demand) <= school.capacity

    return FixedPointAlgorithm(matching_table, schools, students, task10_constraints).execute()


report(algorithm_with_constraints)
