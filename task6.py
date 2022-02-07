from collections import defaultdict

from algorithms import task2
from instances import instance1, instance3, instance2
from algorithms import task2, task5


def verify_45_rule(all_students, student_matching, groups):
    result = defaultdict(lambda: defaultdict(float))
    rational_groups = task5.get_ration_group_students(all_students, groups)
    school_matching = defaultdict(list)
    for student, school in student_matching.items():
        if not school:
            continue
        school_matching[school.school_parent].append(student)
    for school, students_school in school_matching.items():
        rational_school = task5.get_ration_group_students(students_school, groups)
        for g in groups:
            result[g][school.school_parent] = rational_school[g] / rational_groups[g] if rational_groups[g] != 0.0 else None
    return result


def task6():
    print('--------------------')
    # instance1
    matching_table, schools, students = instance1.generate_matching_table_schools_and_students()
    task5.get_fair_ranking_matching_table(matching_table, students, instance1.GROUPS)
    result = task2.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(students)
    print(result)
    verification = verify_45_rule(students, result, instance1.GROUPS)
    print(verification)
    print('--------------------')

    # instance2
    print('--------------------')
    matching_table, schools, students = instance2.generate_matching_table_schools_and_students(12)
    task5.get_fair_ranking_matching_table(matching_table, students, instance2.GROUPS)
    result = task2.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(students)
    print(result)
    verification = verify_45_rule(students, result, instance2.GROUPS)
    print(verification)
    print('--------------------')

    # instance3
    print('--------------------')
    matching_table, schools, students = instance3.generate_matching_table_schools_and_students(12)
    task5.get_fair_ranking_matching_table(matching_table, students, instance3.GROUPS)
    result = task2.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(students)
    print(result)
    verification = verify_45_rule(students, result, instance3.GROUPS)
    print(verification)
    print('--------------------')


task6()
