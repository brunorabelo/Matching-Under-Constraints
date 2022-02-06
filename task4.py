from utils import MatchingState, School, SubSchool, Student
from task2 import DeferredAcceptanceAlgo
import random
import numpy as np

def fill_matching_table_schools(matching_table, schools, students):
    w = np.random.standard_normal(len(students))
    for school in schools:
        noises = np.random.standard_normal(len(students))
        wn = w + noises
        student_idx_wn_list = sorted(enumerate(wn), reverse=True, key=lambda x: x[1])
        school_preference_row = []
        for st_idx, wn_st in student_idx_wn_list:
            school_preference_row.append(students[st_idx])
        matching_table[school] = school_preference_row


def fill_matching_table_students(matching_table, p1, p2, students):
    student_preferences = random.choices([p1, p2], k=len(students))
    for idx, st in enumerate(students):
        matching_table[st] = student_preferences[idx]

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

    result = DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    # res = plot(matching_table, result)
    return result


def task4():
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

    # result1 = DefferedAcceptanceAlgo(adjusted, schools, students).execute()

    # Instance 2
    instance2(6)
task4()