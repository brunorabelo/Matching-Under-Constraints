import random
import numpy as np
from collections import defaultdict


class MatchingState:
    def __init__(self):
        self._matched_schools = {}
        self._matched_students = {}

    def remove_match(self, school):
        if school in self._matched_schools:
            student = self._matched_schools[school]
            del self._matched_students[student]
            del self._matched_schools[school]

    def add_match(self, school, student):
        self._matched_schools[school] = student
        self._matched_students[student] = school

    def student_match_or_none(self, student):
        return self._matched_students.get(student)

    def school_match_or_none(self, school):
        return self._matched_schools.get(school)

    def school_is_matched(self, school):
        return school in self._matched_schools.keys()

    def student_is_matched(self, student):
        return student in self._matched_students.keys()

    def get_students_match(self):
        return self._matched_students

    def add_match_none(self, student):
        self._matched_students[student] = None


class School:
    def __init__(self, school_name, quota_group, capacity):
        self.school_name = school_name
        self.sub_schools = []
        self.quota_group = quota_group
        self.capacity = capacity
        self.school_parent = self

        self.create_sub_schools()

    def create_sub_schools(self):
        for i in range(0, self.capacity):
            new_school_name = self.school_name + str(i)
            new_sub_school = SubSchool(new_school_name, self)
            self.sub_schools.append(new_sub_school)

    def get_max_quantity_group(self, group):
        return self.quota_group[group]

    def get_quantity_current_students(self, matching_state, group=None):
        res = 0
        for sub in self.sub_schools:
            student = matching_state.school_match_or_none(sub)
            if student and (not group or group == student.group):
                res += 1
        return res

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.school_name == other.school_name

    def __hash__(self):
        return hash(self.school_name)

    def __repr__(self):
        return self.school_name


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name


class SubSchool(School):
    def __init__(self, school_name, school_parent):
        self.school_name = school_name
        self.school_parent = school_parent

    def get_max_quantity_group(self, group):
        return self.school_parent.get_max_quantity_group(group)

    def get_quantity_current_students(self, matching_state, group=None):
        return self.school_parent.get_quantity_current_students(matching_state, group)

    def get_max_capacity(self):
        return self.school_parent.capacity

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.school_name == other.school_name

    def __hash__(self):
        return hash(self.school_name)

    def __repr__(self):
        return self.school_name




##########
##################################
######
def get_adjusted_matching_table(matching_table, schools, students):
    adjusted_table = {}
    for student in students:
        row = []
        for school in matching_table[student]:
            row += school.sub_schools
        adjusted_table[student] = row
    for school in schools:
        adjusted_table[school] = matching_table[school]
    return adjusted_table


def plot(matching_table, result):
    res = defaultdict(lambda: defaultdict(int))
    for st, school in result.items():
        res[st.group]['total'] += 1
        if school and school.school_parent == matching_table[st][0]:
            res[st.group]['first'] += 1
    return res


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

    adjusted = get_adjusted_matching_table(matching_table, schools, students)

    result = DefferedAcceptanceAlgo(adjusted, schools, students).execute()
    res = plot(matching_table, result)
    return result


def task3():
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

    adjusted = get_adjusted_matching_table(matching_table, schools, students)

    # result1 = DefferedAcceptanceAlgo(adjusted, schools, students).execute()

    # Instance 2
    instance2(6)
