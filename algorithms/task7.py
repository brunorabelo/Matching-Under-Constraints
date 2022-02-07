class FixedPointAlgorithm:
    def __init__(self, matching_table, schools, students, constraints):
        self.matching_table = matching_table
        self.schools = schools
        self.students = students
        self.P = [i for i in range(1, len(students) + 2)]
        self.satisfy_constraints = constraints

    def get_student_matching_from_school_matching(self, school_matching):
        student_matching = {}
        for school, students in school_matching.items():
            for student in students:
                student_matching[student] = school
        for student in self.students:
            student_matching.setdefault(student, None)
        return student_matching

    # def execute(self):
    #     p = self.find_fixed_point()
    #     demands = {}
    #     for school in self.schools:
    #         demands[school] = self.demand_at_school(school, p)
    #     students_matching = self.get_student_matching_from_school_matching(demands)
    #     return students_matching
    #
    # def find_fixed_point(self):
    #     for p in self.P:
    #         same_p = True
    #         for school in self.schools:
    #             if self.mapping_t(school, p) != p:
    #                 same_p = False
    #                 break
    #         if same_p:
    #             return p
    #     return -1

    def execute(self):
        demands = {}
        for school in self.schools:
            p = self.find_fixed_point_for_school(school)
            demands[school] = self.demand_at_school(school, p)
        students_matching = self.get_student_matching_from_school_matching(demands)
        return students_matching

    def find_fixed_point_for_school(self, school):
        for p in self.P:
            if self.mapping_t(school, p) == p:
                return p
        return 1

    def demand_at_school(self, s, p):
        cutoff_students = self.get_cutoff_students(s, p)
        demand = []
        first_condition_students = [student for student in cutoff_students if s in self.matching_table[student]]
        for student in first_condition_students:
            for school in self.matching_table[student]:
                cutoff_students_of_school = self.get_cutoff_students(school, p)
                if student in cutoff_students_of_school and school == s:
                    demand.append(student)
                    break
                elif student in cutoff_students_of_school:
                    break
        return demand

    def mapping_t(self, s, p):
        demand = self.demand_at_school(s, p)
        if self.satisfy_constraints(s, demand):
            return p
        return p + 1

    def get_cutoff_students(self, school, p):
        preferred_students = self.matching_table[school.school_parent]
        cutoff_students = preferred_students[:len(preferred_students) - p + 1]
        return cutoff_students
