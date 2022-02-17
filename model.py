from collections.abc import Iterable, Iterator


class IncorrectFieldValueException(Exception):
    def __init__(self, msg):
        raise Exception(f'Record not found! \n {msg}')


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

    def __init__(self, course_id, name, description):
        self.id = course_id
        self.name = name
        self.description = description
        self.students = []

    def add_student(self, student: 'Student'):
        print(f'adding student {student.name} {student.surname} to course {self.name}')
        if not (student in self.students):
            self.students.append(student)

    def __iter__(self):
        return StudentsIterator(self.students)


class Student:
    def __init__(self, student_id, name, surname):
        self.id = student_id
        self.name = name
        self.surname = surname
        self.validate()

    def validate(self):
        if (len(self.name) < 3) | (' ' in self.name):
            raise IncorrectFieldValueException(
                'Incorrect Student name. It must be longer than 3 symbols and not contain spaces')
        if (len(self.surname) < 3) | (' ' in self.surname):
            raise IncorrectFieldValueException(
                'Incorrect Student surname. It must be longer than 3 symbols and not contain spaces')
