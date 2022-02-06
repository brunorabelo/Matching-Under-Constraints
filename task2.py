from utils import MatchingState, School, SubSchool, Student


class DeferredAcceptanceAlgo:
    def __init__(self, matching_table, schools, students):
        self.matching_state = MatchingState()
        self.schools = schools
        self.students = students
        self.matching_table = self.adjusted_matching_table(matching_table)

    def execute(self):
        while True:
            student = self.next_unmatched_student()
            if student == -1:
                break
            school = self.next_school_for_student(student)
            if school == -1:
                self.add_matching_none(student)
                continue
            if self.school_is_matched(school):
                self.remove_match(school)
            self.add_matching(school, student)
        return self.matching_state.get_students_match()

    def adjusted_matching_table(self, matching_table):
        adjusted_table = {}
        for student in self.students:
            row = []
            for school in matching_table[student]:
                row += school.sub_schools
            adjusted_table[student] = row
        for school in self.schools:
            adjusted_table[school] = matching_table[school]
        return adjusted_table

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
        next_school = -1
        for school in preferred_schools:
            current_matched_student = self.school_match(school)
            preferred_student = current_matched_student and self.preferred_student_by_school(school, target_student,
                                                                                             current_matched_student)

            # check justified envy
            if current_matched_student and preferred_student != target_student:
                continue

            # capacity constraint
            current_total_quantity_school = school.get_quantity_current_students(self.matching_state)
            if not current_matched_student and current_total_quantity_school == school.get_max_capacity():
                continue

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

    def add_matching_none(self, student):
        self.matching_state.add_match_none(student)
