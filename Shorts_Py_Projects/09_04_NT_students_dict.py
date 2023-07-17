"""
1.  Convert the data so that it is presented as a dictionary, where the keys are student numbers and the values are a list of other student data.
2.  Write a function that takes as an argument the student’s number and the new group number
    and allows you to change the student’s group number to a new one inside the created dictionary.
3.  Write a function that takes the group number and lists (names, names, patronymic) of all students in this group. You must refer to the dictionary.
"""




students = [
["0001", "Антонов", "Антон", "Игоревич", "20.08.2009","БСТ161"],
["1102", "Богов", "Артем", "Игоревич", "25.01.2010","БСТ162"],
["0333", "Глаголева", "Анастасия", "Николаевна", "11.07.2009", "БСТ163"],
["4004", "Степанова", "Наталья", "Александровна", "13.02.2008", "БСТ161"],
["0045", "Боков", "Игорь", "Харитонович", "02.06.2009", "БСТ161"],
["0096", "Васильков", "Валентин", "Сергеевич", "20.03.2009", "БСТ164"],
["0607", "Сиропова", "Виолетта", "Эдуардовна", "28.05.2010", "БСТ162"]
    ]


def convert_list_to_dict(students:list) -> dict:
    conv_students = {}
    for student in students:
        conv_students[student[0]] = student[1:]
    return conv_students


def change_group_of_student(num_student:str, new_group:str, students:dict) -> dict:
    students[num_student] = students.get(num_student)[:4] + [new_group]
    return students


def print_students_of_group(group_num:str, students:dict) -> None:
    print(f'Student list of group {group_num}:')
    for student in students.values():
        if student[4] == group_num:
            print(f'{student[0]} {student[1]} {student[2]}')


students = convert_list_to_dict(students)
print(students)

students = change_group_of_student('0001', 'БСТ167', students)
print(students)

print_students_of_group('БСТ162', students)