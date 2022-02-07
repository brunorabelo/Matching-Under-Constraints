# examples of executing an algorithm
from algorithms import task3, task2, task5, task7
from instances import instance1, instance2, instance3


def task4():
    # Task2 and Instance 1
    matching_table, schools, students = instance1.generate_matching_table_schools_and_students()
    result_task2_instance1 = task2.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(result_task2_instance1)
    # Task2 and Instance 2
    matching_table, schools, students = instance2.generate_matching_table_schools_and_students()
    result_task2_instance2 = task2.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(result_task2_instance2)

    # Task2 and Instance 3
    matching_table, schools, students = instance3.generate_matching_table_schools_and_students()
    result_task2_instance3 = task2.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(result_task2_instance3)

    # ------------#
    # Task3 and Instance 1
    matching_table, schools, students = instance1.generate_matching_table_schools_and_students()
    result_task3_instance1 = task3.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(result_task3_instance1)

    # Task3 and Instance 2
    matching_table, schools, students = instance2.generate_matching_table_schools_and_students()
    result_task3_instance2 = task3.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(result_task3_instance2)

    # Task3 and Instance 3
    matching_table, schools, students = instance3.generate_matching_table_schools_and_students()
    result_task3_instance3 = task3.DeferredAcceptanceAlgo(matching_table, schools, students).execute()
    print(result_task3_instance3)

