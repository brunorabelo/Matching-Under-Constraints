import random
import numpy as np
from collections import defaultdict


class MatchingState:
    """
    Class to take care of the current matches
    """

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

    def get_students_matches(self):
        return self._matched_students

    def get_schools_matches(self):
        return self._matched_schools

    def add_match_none(self, student):
        self._matched_students[student] = None


class School:
    """
    Class representing a school and its properties
    """

    def __init__(self, school_name, quota_group, capacity):
        self.school_name = school_name
        self.sub_schools = []
        self.quota_group = quota_group
        self.capacity = capacity
        self.school_parent = self

        self.create_sub_schools()

    def create_sub_schools(self):
        """
        Ideal to create schools proportionally to their capacity.
        school s1 with capacity 2 turns to: s10 s11
        """
        for i in range(0, self.capacity):
            new_school_name = self.school_name + str(i)
            new_sub_school = SubSchool(new_school_name, self, i)
            self.sub_schools.append(new_sub_school)

    #
    def get_max_quantity_group(self, group):
        """
        :param group: the specific group to search for the quota
        :return: max quantity
        """
        return self.quota_group[group]

    def get_quantity_current_students(self, matching_state, group=None):
        """
        get the current quantity of matched students
        :param matching_state: the matching state to get the matching state
        :param group: if group is given, returns only the quantity of students of that group
        :return: the quantity of students matched to this school of a group or in total
        """
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
    """
    Class to represent the students
    """

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
        return f"{self.name} - group: {self.group}"


class SubSchool(School):
    """ Class to represent the school availble places"""

    def __init__(self, school_name, school_parent, place=0):
        self.school_name = school_name
        self.school_parent = school_parent
        self.place = place

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
        return f"{self.school_parent.school_name} - place: {self.place + 1}"
