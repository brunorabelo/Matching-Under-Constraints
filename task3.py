from task2 import DeferredAcceptanceAlgo
from utils import MatchingState, School, SubSchool, Student


class DeferredAcceptanceAlgoCapacityConstraint(DeferredAcceptanceAlgo):
    def __init__(self, matching_table, schools, students):
        super().__init__(matching_table, schools, students)

    def next_school_for_student(self, target_student):
        preferred_schools = self.matching_table[target_student]
        target_student_group = target_student.group
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

            # group capacity constraint
            max_quantity_group_school = school.get_max_quantity_group(target_student_group)
            current_quantity_group_school = school.get_quantity_current_students(self.matching_state,
                                                                                 target_student_group)

            current_matched_student_group = current_matched_student and current_matched_student.group
            reached_limit = max_quantity_group_school == current_quantity_group_school
            # case 1: not matched and reached limit students
            if not current_matched_student and reached_limit:
                continue
            # case 2: matched with different group and reached limit students
            if current_matched_student and target_student_group != current_matched_student_group and reached_limit:
                continue

            return school
        return -1
