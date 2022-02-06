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
            if not self.student_is_matched(student):
                return student
        return -1

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
        target_student_group = target_student.group
        for school in preferred_schools:
            max_quantity_group_school = school.get_max_quantity_group(target_student_group)
            current_quantity_group_school = school.get_quantity_current_students(self.matching_state,
                                                                                 target_student_group)

            current_matched_student = self.school_match(school)
            current_matched_student_group = current_matched_student and current_matched_student.group

            if current_quantity_group_school == max_quantity_group_school and current_matched_student_group and \
                    current_matched_student_group != target_student_group:
                continue

            if not current_matched_student:
                return school
            if target_student == self.preferred_student_by_school(school, target_student, current_matched_student):
                return school

        return -1

    def preferred_student_by_school(self, school, s1, s2):
        preferred_students = self.matching_table[school.school_parent]
        for student in preferred_students:
            if student == s1:
                return s1
            if student == s2:
                return s2
        return -1

    def add_matching(self, school, student):
        self.matching_state.add_match(school, student)


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
        return school in self._matched_schools

    def student_is_matched(self, student):
        return student in self._matched_students

    def get_students_match(self):
        return self._matched_students


class School:
    def __init__(self, school_name, quota_group, capacity):
        self.school_name = school_name
        self.sub_schools = []
        self.quota_group = quota_group
        self.capacity = capacity

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

    def get_quantity_current_students(self, matching_state, group):
        return self.school_parent.get_quantity_current_students(matching_state, group)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.school_name == other.school_name

    def __hash__(self):
        return hash(self.school_name)

    def __repr__(self):
        return self.school_name


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

    result1 = DefferedAcceptanceAlgo(adjusted, schools, students).execute()


task3()
