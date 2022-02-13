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


class CourseStudentLink:
    def __init__(self, link_id, course_id, student_id):
        self.id = link_id
        self.course_id = course_id
        self.student_id = student_id
