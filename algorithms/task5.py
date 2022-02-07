from collections import defaultdict
from copy import copy
from math import ceil, floor

from utils import School


def _count_students_of_group_in_rank(school_preference):
    count_group_rank = defaultdict(lambda: defaultdict(int))
    rank = 1
    cumulative_count_group = defaultdict(int)
    for student in school_preference:
        cumulative_count_group[student.group] += 1
        count_group_rank[rank] = copy(cumulative_count_group)

        rank += 1

    return count_group_rank


def _add_student_of_group_in_position(school_preference, position, group):
    # print(f"adding element at position {position}: {school_preference}")
    i = position + 1
    while i < len(school_preference) and school_preference[i].group != group:
        i += 1
    if i == len(school_preference):
        # print(f"Impossible to change array")
        return -1
    temp = school_preference[i]
    del school_preference[i]
    school_preference.insert(position, temp)
    # print(f"Array changed: {school_preference}")
    return True


def _remove_student_of_group_in_position(school_preference, position, group):
    # print(f"removing element at position {position}: {school_preference}")
    i = position + 1
    while i < len(school_preference) and school_preference[i].group == group:
        i += 1
    if i == len(school_preference):
        # print(f"Impossible to change array")
        return -1
    temp = school_preference[i]
    del school_preference[i]
    school_preference.insert(position, temp)
    # print(f"Array changed: {school_preference}")
    return True


def _make_school_preference_ranking_fair(school_preference, ration_students_group):
    dict_count_students_per_group_per_rank = _count_students_of_group_in_rank(school_preference)
    groups = ration_students_group.keys()
    for rank in range(1, len(school_preference) + 1):
        inf = {group: floor(rank * 0.8 * ration_students_group[group]) for group in groups}
        sup = {group: ceil(rank * 1.2 * ration_students_group[group]) for group in groups}
        i = rank - 1
        # while i < len(school_preference):
        current_student = school_preference[i]
        current_group = current_student.group
        count_group_in_rank = dict_count_students_per_group_per_rank[rank][current_group]
        if inf[current_group] <= count_group_in_rank <= sup[current_group]:
            # respects the 4/5 rule
            continue
        if count_group_in_rank < inf[current_group]:
            # we need to add one of the group in the rank
            _add_student_of_group_in_position(school_preference, i, current_group)
        else:
            # we need to remove one of the group in the rank
            _remove_student_of_group_in_position(school_preference, i, current_group)


def get_ration_group_students(students, groups):
    n_students = len(students)
    ration_students_group = {group: 0 for group in groups}
    for student in students:
        ration_students_group[student.group] += 1
    for group in groups:
        ration_students_group[group] /= n_students
    return ration_students_group


def get_fair_ranking_matching_table(matching_table, students, groups):
    ration_students_group = get_ration_group_students(students, groups)
    for school, school_preference in matching_table.items():
        if type(school) == School:
            _make_school_preference_ranking_fair(school_preference, ration_students_group)
