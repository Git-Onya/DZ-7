class Mentor:
    def __init__(self, name, surname, average=0):
        self.name = name
        self.surname = surname
        self.average = average
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
    def __str__(self):
        for grade in self.grades:
            self.average = round(sum(self.grades[grade]) / len(self.grades[grade]), 1)
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}')

    def comparison(self, another):
        if not isinstance(another, Lecturer):
            return
        if self.average > another.average:
            print(f'Средняя оценка выше у {self.name} {self.surname}')
        elif self.average < another.average:
            print(f'Средняя оценка выше у {another.name} {another.surname}')
        else:
            print('Средние оценки лекторов равны')

class Student:
    def __init__(self, name, surname, gender, average=0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.average = average
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for grade in self.grades:
            self.average = round(sum(self.grades[grade]) / len(self.grades[grade]), 1)
        print(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')

    def comparison(self, another):
        if not isinstance(another, Student):
            return
        if self.average > another.average:
            print(f'Средняя оценка выше у {self.name} {self.surname}')
        elif self.average < another.average:
            print(f'Средняя оценка выше у {another.name} {another.surname}')
        else:
            print('Средние оценки студентов равны')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}\nФамилия: {self.surname}')

first_student = Student('Dopey', 'Dwarf', 'Male')
first_student.courses_in_progress += ['Mining']
first_student.courses_in_progress += ['Craft']
second_student = Student('Sneezy', 'Dwarf', 'Male')
second_student.courses_in_progress += ['Craft']
first_lecturer = Lecturer('Hunts', 'Man')
first_lecturer.courses_attached += ['Mining']
second_lecturer = Lecturer('Snow', 'White')
second_lecturer.courses_attached += ['Craft']
first_reviewer = Reviewer('Gray', 'Wolf')
first_reviewer.courses_attached += ['Mining']
second_reviewer = Reviewer('Red', 'Hood')
second_reviewer.courses_attached += ['Craft']

first_reviewer.rate_hw(first_student, 'Mining', 5)
first_reviewer.rate_hw(first_student, 'Mining', 8)
first_reviewer.rate_hw(first_student, 'Mining', 5)
second_reviewer.rate_hw(second_student, 'Craft', 3)
second_reviewer.rate_hw(second_student, 'Craft', 3)
second_reviewer.rate_hw(second_student, 'Craft', 6)
second_reviewer.rate_hw(first_student, 'Craft', 4)
second_reviewer.rate_hw(first_student, 'Craft', 8)
second_reviewer.rate_hw(first_student, 'Craft', 8)
first_student.rate_lecturer(first_lecturer, 'Mining', 7)
first_student.rate_lecturer(first_lecturer, 'Mining', 10)
first_student.rate_lecturer(first_lecturer, 'Mining', 8)
second_student.rate_lecturer(second_lecturer, 'Craft', 9)
second_student.rate_lecturer(second_lecturer, 'Craft', 8)
second_student.rate_lecturer(second_lecturer, 'Craft', 10)

first_reviewer.__str__()
first_lecturer.__str__()
second_lecturer.__str__()
first_lecturer.comparison(second_lecturer)

first_student.__str__()
second_student.__str__()
first_student.comparison(second_student)

