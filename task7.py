import random
import numpy as np
from collections import defaultdict
from task3 import School, SubSchool, Student, MatchingState, fill_matching_table_students, fill_matching_table_schools, \
    get_adjusted_matching_table


class FixedPointAlgorithm:
    def __init__(self, matching_table, schools, students, constraints):
        self.matching_state = MatchingState()
        self.matching_table = matching_table
        self.schools = schools
        self.students = students
        self.P = [i for i in range(1, len(students) + 2)]
        self.satisfy_constraints = constraints

    def execute(self):
        p = self.find_fixed_point()
        demands = {}
        for school in self.schools:
            demands[school] = self.demand_at_school(school, p)
        return demands

    def find_fixed_point(self):
        res = 0
        for p in self.P:
            same_p = True
            for school in self.schools:
                if self.mapping_t(school, p) != p:
                    same_p = False
                    break
            if same_p:
                return p

        return -1

    def demand_at_school(self, s, p):
        cutoff_students = self.get_cutoff_students(s, p)
        demand = []
        first_condition_students = [student for student in cutoff_students if s in self.matching_table[student]]
        for student in first_condition_students:
            for school in self.matching_table[student]:
                cutoff_students_of_school = self.get_cutoff_students(school, p)
                if student in cutoff_students_of_school and school == s:
                    demand.append(student)
                    break
                elif student in cutoff_students_of_school:
                    break
        return demand

    def mapping_t(self, s, p):
        demand = self.demand_at_school(s, p)
        if self.satisfy_constraints(s, demand):
            return p
        return p + 1

    def get_cutoff_students(self, school, p):
        preferred_students = self.matching_table[school.school_parent]
        cutoff_students = preferred_students[:len(preferred_students) - p + 1]
        return cutoff_students


def instance2(n):
    s1 = School('s1', quota_group={"A": 0.9 * n // 4, "B": 0.9 * n // 4}, capacity=n // 4)
    s2 = School('s2', quota_group={"A": 0.9 * n // 4, "B": 0.9 * n // 4}, capacity=n // 4)
    schools = [s1, s2]
    students = []

    m = (9 * n) // 10
    for i in range(0, m):
        students.append(Student(f'i{i}', "A"))
    for i in range(m, n):
        students.append(Student(f'i{i}', "B"))

    matching_table = {}
    p1 = [s1, s2]
    p2 = [s2, s1]
    fill_matching_table_students(matching_table, p1, p2, students)

    fill_matching_table_schools(matching_table, schools, students)

    # adjusted = get_adjusted_matching_table(matching_table, schools, students)

    result = FixedPointAlgorithm(matching_table, schools, students, task8).execute()
    print(result)
    # res = plot(matching_table, result)
    # return result


def task8(school, demand):
    return len(demand) <= school.capacity


def task7():
    # Instance 1
    s1 = School('s1', {"A": 2, "B": 2}, 2)
    s2 = School('s2', {"A": 2, "B": 2}, 2)
    i1 = Student('i1', 'A')
    i2 = Student('i2', 'A')
    i3 = Student('i3', 'A')
    i4 = Student('i4', 'B')
    schools = [s1, s2]
    students = [i1, i2, i3, i4]
    matching_table = {
        i1: [s1, s2],
        i2: [s2, s1],
        i3: [s1],
        i4: [s2],
        s1: [i4, i3, i2, i1],
        s2: [i4, i3, i2, i1]
    }

    # adjusted = get_adjusted_matching_table(matching_table, schools, students)

    result1 = FixedPointAlgorithm(matching_table, schools, students, task8).execute()

    # Instance 2
    # instance2(6)


instance2(6)
