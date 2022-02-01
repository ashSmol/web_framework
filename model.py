class CourseCategory:
    name: str
    description: str


class Course:
    name: str
    description: str


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

    def get_students(self):
        return self.students
