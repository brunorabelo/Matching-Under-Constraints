def next_unmatched_student(students, matched_students):
    for student in students:
        if student not in matched_students:
            return student
    return -1


def next_school_for_student(matching_table, schools, matched_schools, target_student):
    preferred_schools = matching_table[target_student]
    for school in preferred_schools:
        if school not in matched_schools:
            return school
        current_matched_student = matched_schools[school]
        preferred_students = matching_table[school]
        for student in preferred_students:
            if student == target_student:
                return school
            if student == current_matched_student:
                break
    return -1


def deferred_acceptance(matching_table, students, schools):
    matched_students = {}
    matched_schools = {}
    while True:
        student = next_unmatched_student(students, matched_students)
        if student == -1:
            break
        school = next_school_for_student(matching_table, schools, matched_schools, student)
        if school == -1:
            break
        if school in matched_schools:
            student_unmatched = matched_schools[school]
            del matched_schools[school]
            del matched_students[student_unmatched]
        matched_schools[school] = student
        matched_students[student] = school
    return matched_students


def get_adjusted_matching_table(matching_table, students, schools):
    adjusted_table = {}
    for student in students:
        row = []
        for school in matching_table[student]:
            capacity = schools[school]
            for i in range(0, capacity):
                new_school_name = school + str(i)
                row.append(new_school_name)
                adjusted_table[new_school_name] = matching_table[school]
        adjusted_table[student] = row

    return adjusted_table


def task2():
    # Instance 1
    matching_table = {
        'i1': ['s1', 's2'],
        'i2': ['s2', 's1'],
        'i3': ['s1'],
        'i4': ['s2'],
        's1': ['i4', 'i3', 'i2', 'i1'],
        's2': ['i4', 'i3', 'i2', 'i1']
    }
    students = ['i1', 'i2', 'i3', 'i4']
    schools = {
        's1': 2,
        's2': 2
    }
    adjusted = get_adjusted_matching_table(matching_table, students, schools)
    result1 = deferred_acceptance(adjusted, students, schools)

    # Instance 2


task2()
