class DefferedAcceptanceAlgo:
    def __init__(self, matching_table, schools, students):
        self.matching_state = MatchingState()
        self.matching_table = matching_table
        self.schools = schools
        self.students = students

    def execute(self):
        while True:
            student = self.next_unmatched_student()
            if student == -1:
                break
            school = self.next_school_for_student(student)
            if school == -1:
                break
            if self.school_is_matched(school):
                self.remove_match(school)
            self.add_matching(school, student)
        return self.matching_state.get_students_match()

    def remove_match(self, school):
        self.matching_state.remove_match(school=school)

    def next_unmatched_student(self):
        for student in self.students:
            if student not in self.matching_state._matched_students:
                return student
        return -1

    def get_student_group(self, student):
        return self.students[student]

    def get_max_quantity_group_school(self, sub_school, group):
        # TODO dsds
        return sub_school.parent.group[group]

    def get_current_quantity_group_school(self, sub_school, group):
        current_quantity_group_school = 0
        school_names = sub_school.parent.get['school_names']
        for school_name in school_names:
            if self.is_school_matched(school_name) and self.get_student_group(
                    self.school_match(school_name)) == group:
                current_quantity_group_school += 1
        return current_quantity_group_school

    def school_match(self, school):
        return self.matching_state.school_match_or_none(school)

    def student_match(self, student):
        return self.matching_state.student_match_or_none(student)

    def school_is_matched(self, school):
        return self.matching_state.school_is_matched(school)

    def student_is_matched(self, student):
        return self.matching_state.student_is_matched(student)

    def next_school_for_student(self, target_student):
        preferred_schools = self.matching_table[target_student]
        target_student_group = self.get_student_group(target_student)
        for school in preferred_schools:
            max_quantity_group_school = self.get_max_quantity_group_school(school, target_student_group)
            current_quantity_group_school = self.get_current_quantity_group_school(school, target_student_group)

            current_matched_student = self.school_match(school)
            current_matched_student_group = current_matched_student and self.get_student_group(current_matched_student)

            if current_quantity_group_school == max_quantity_group_school and current_matched_student_group and \
                    current_matched_student_group != target_student_group:
                continue

            if not self.school_is_matched(school):
                return school
            current_matched_student = self.school_match(school)
            preferred_students = self.matching_table[school]
            for student in preferred_students:
                if student == target_student:
                    return school
                if student == current_matched_student:
                    break
        return -1

    def add_matching(self, school, student):
        self.matching_state.add_match(school, student)


class MatchingState:
    def __init__(self):
        self._matched_schools = {}
        self._matched_students = {}

    def remove_match(self, school):
        if school in self._matched_schools:
            student = self._matched_students[school]
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
        return school in self._matched_schools

    def student_is_matched(self, student):
        return student in self._matched_students

    def get_students_match(self):
        return self._matched_students


class School:
    def __init__(self, school_name, quota_group, capacity):
        pass


class Student:
    pass


class SubSchool(School):
    def __init__(self, school_name):
        self.school_name


def next_unmatched_student(students, matched_students):
    for student in students:
        if student not in matched_students:
            return student
    return -1


def next_school_for_student(matching_table, schools, students, matched_schools, target_student):
    preferred_schools = matching_table[target_student]
    target_student_group = students[target_student]
    for school in preferred_schools:
        max_quantity_group_school = schools[school][target_student_group]
        current_quantity_group_school = 0
        school_names = schools[school]['school_names']
        for school_name in school_names:
            if school_name in matched_schools and students[matched_schools[school_name]] == target_student:
                current_quantity_group_school += 1

        current_matched_student = matched_schools[school]
        current_matched_student_group = students[current_matched_student]
        if current_quantity_group_school == max_quantity_group_school and current_matched_student_group != target_student_group:
            continue
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
        school = next_school_for_student(matching_table, schools, students, matched_schools, student)
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
            capacity = schools[school]['capacity']
            for i in range(0, capacity):
                new_school_name = school + str(i)
                row.append(new_school_name)
                adjusted_table[new_school_name] = matching_table[school]
                schools[school]['school_names'].append(new_school_name)
        adjusted_table[student] = row

    return adjusted_table


def task3():
    # Instance 1
    matching_table = {
        'i1': ['s1', 's2'],
        'i2': ['s2', 's1'],
        'i3': ['s1'],
        'i4': ['s2'],
        's1': ['i4', 'i3', 'i2', 'i1'],
        's2': ['i4', 'i3', 'i2', 'i1']
    }
    students = {'i1': "A", 'i2': "A", 'i3': "A", 'i4': "B"}
    schools = {
        's1': {'quota_group': {"A": 2, "B": 2}, "capacity": 2, "school_names": []},
        's2': {'quota_group': {"A": 2, "B": 2}, "capacity": 2, "school_names": []}
    }

    schools = [School('s1', quota_group={"A": 2, "B": 2}, capacity=2, subschools=[])]

    adjusted = get_adjusted_matching_table(matching_table, students, schools)

    result1 = deferred_acceptance(adjusted, students, schools)


# Instance 2

task3()
