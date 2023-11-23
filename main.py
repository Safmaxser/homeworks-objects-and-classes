class GradeBook:

    def __init__(self):
        self.grades = {}

    def _average_rating(self):
        list_grades = [list_all_grades for all_grades in
                       self.grades.values() for list_all_grades in
                       all_grades]
        return round(sum(list_grades) / len(list_grades), 2)

    def __eq__(self, other):
        return self._average_rating() == other._average_rating()

    def __lt__(self, other):
        return self._average_rating() < other._average_rating()

    def __le__(self, other):
        return self._average_rating() <= other._average_rating()


class Student(GradeBook):

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        GradeBook.__init__(self)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._average_rating()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached and
                isinstance(grade, int) and
                grade in range(11)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, GradeBook):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        GradeBook.__init__(self)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._average_rating()}')


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_course_grade(participant_list, course):
    if isinstance(participant_list, list):
        list_grades = []
        for participant in participant_list:
            if (isinstance(participant, GradeBook) and
                    course in participant.grades.keys()):
                list_grades += participant.grades[course]
    return round(sum(list_grades) / len(list_grades), 2)


student_1 = Student('Антон', 'Антипов', 'мужской')
student_2 = Student('Оля', 'Петрова', 'женский')

lecturer_1 = Lecturer('Ярослав', 'Брежнев')
lecturer_2 = Lecturer('Иван', 'Силов')

reviewer_1 = Reviewer('Андрей', 'Замятин')
reviewer_2 = Reviewer('Александр', 'Высоцкий')

student_1.courses_in_progress += ['Python', 'Java']
student_1.courses_in_progress += ['Swift']
student_2.courses_in_progress += ['Python', 'C++']
student_2.courses_in_progress += ['Kotlin']

lecturer_1.courses_attached += ['Python', 'C++', 'C#']
lecturer_2.courses_attached += ['Java', 'Kotlin']

reviewer_1.courses_attached += ['Python', 'Java', 'C++']
reviewer_2.courses_attached += ['Kotlin', 'Swift']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_1, 'Kotlin', 8)

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'C++', 10)
reviewer_1.rate_hw(student_2, 'C++', 7)
reviewer_2.rate_hw(student_2, 'Kotlin', 8)
reviewer_2.rate_hw(student_2, 'Swift', 6)

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'C++', 7)
student_1.rate_hw(lecturer_1, 'C#', 9)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'C++', 6)
student_2.rate_hw(lecturer_1, 'C#', 8)

student_1.rate_hw(lecturer_2, 'Java', 9)
student_1.rate_hw(lecturer_2, 'Java', 6)
student_1.rate_hw(lecturer_2, 'Kotlin', 9)
student_2.rate_hw(lecturer_2, 'Kotlin', 10)
student_2.rate_hw(lecturer_2, 'Kotlin', 8)
student_2.rate_hw(lecturer_2, 'Java', 10)

print(student_1, '\n')
print(student_2, '\n')
print(lecturer_1, '\n')
print(lecturer_2, '\n')
print(reviewer_1, '\n')
print(reviewer_2, '\n')

print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 >= lecturer_2)
print(lecturer_1 <= lecturer_2)
print()
print(student_1 == student_2)
print(student_1 != student_2)
print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 >= student_2)
print(student_1 <= student_2)

print()
print(average_course_grade([student_1, student_2], 'Python'))
print(average_course_grade([lecturer_1, lecturer_2], 'Python'))