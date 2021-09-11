
class Student_data:
    def __init__(self, last_name, class_name, grades):
        last_name: str
        class_name: str
        grades: list

    def add_new_student(self):
        last_name = input('Your last name^ ')
        class_name = input('Class ')
        grades = []
        n = 0
        while n < 5:
            grades.append(int(input('Your grades ')))
            n += 1

    add_new_student(self)