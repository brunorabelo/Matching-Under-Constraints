from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
import random
from utils import School, Student

GROUPS = ['A', 'B']


def _fill_matching_table_schools(matching_table, schools, students):
    w = np.random.standard_normal(len(students))
    for school in schools:
        noises = np.random.standard_normal(len(students))
        wn = w + noises
        student_idx_wn_list = sorted(enumerate(wn), reverse=True, key=lambda x: x[1])
        school_preference_row = []
        for st_idx, wn_st in student_idx_wn_list:
            school_preference_row.append(students[st_idx])
        matching_table[school] = school_preference_row


def _fill_matching_table_students(matching_table, p1, p2, students):
    student_preferences = random.choices([p1, p2], k=len(students))
    for idx, st in enumerate(students):
        matching_table[st] = student_preferences[idx]


def generate_matching_table_schools_and_students(n):
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
    _fill_matching_table_students(matching_table, p1, p2, students)

    _fill_matching_table_schools(matching_table, schools, students)

    return matching_table, schools, students


def _count_students_first_choice_per_group(matching_table, student_matching):
    res = defaultdict(int)
    # get total students with their first choice met
    for student, school in student_matching.items():
        if school and matching_table[student][0] == school:
            res[student.group] += 1
    return res


def _get_groups(schools):
    return schools.quota_group.keys()


def _plot(x_array, group_array):
    for group, y_array in group_array:
        plt.plot(x_array, y_array, label=f"Group: {group}")

    plt.legend("sdds")
    plt.show()


def generate_report(algorithm):
    realizations = 10
    n_array = [20, 50, 100, 500, 1000]
    avg_per_group = defaultdict(list)
    for n in n_array:
        count_group = defaultdict(int)
        for i in range(realizations):

            matching_table, schools, students = generate_matching_table_schools_and_students(n)
            student_matching = algorithm(matching_table, schools, students)
            count_per_group = _count_students_first_choice_per_group(matching_table,
                                                                     student_matching)
            for group, count in count_per_group.items():
                count_group[group] += count / realizations
        for group in GROUPS:
            count_avg = count_group.get(group, 0)
            avg_per_group[group].append(count_avg)

    _plot(n_array, avg_per_group)
