from utils import School, Student

GROUPS = ['A', 'B']


def generate_matching_table_schools_and_students():
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

    return matching_table, schools, students


def report(algorithm):
    matching_table, schools, students = generate_matching_table_schools_and_students()
    return algorithm(matching_table, schools, students)
