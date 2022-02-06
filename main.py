
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


def plot(matching_table, result):
    res = defaultdict(lambda: defaultdict(int))
    for st, school in result.items():
        res[st.group]['total'] += 1
        if school and school.school_parent == matching_table[st][0]:
            res[st.group]['first'] += 1
    return res


