from collections.abc import Iterable, Iterator


class StudentsIterator(Iterator):
    _position: int = None

    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value


class CourseCategory:
    name: str
    description: str


class Course(Iterable):
    name: str
    description: str

    def __init__(self):
        self.students = []

    def add_student(self, student: 'Student'):
        print(f'adding student {student.name} {student.surname} to course {self.name}')
        if not (student in self.students):
            self.students.append(student)

    def __iter__(self):
        return StudentsIterator(self.students)


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class TrainingSite:
    course_categories: list
    courses: list
    students: list

    def get_categories(self):
        return self.course_categories

    def get_courses(self):
        return self.courses

    def get_course_by_name(self, name):
        for course in self.courses:
            if course.name == name:
                return course
        return None

    def get_students(self):
        return self.students

    def get_student(self, name, surname):
        for student in self.students:
            if (student.name == name) & (student.surname == surname):
                return student
        return None
