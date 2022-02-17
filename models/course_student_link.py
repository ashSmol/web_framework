import threading
import sqlite3

from patterns.mappers import DbDeleteException, RecordNotFoundException

connection = sqlite3.connect('my_db.db')


class CourseStudentLinkMapper:
    def __init__(self, _connection):
        self.connection = _connection
        self.cursor = _connection.cursor()

    def find_courses_for_student(self, student_id):

        statement = "SELECT ID, COURSE_ID, STUDENT_ID FROM COURSE_STUDENT WHERE STUDENT_ID=?"
        try:
            self.cursor.execute(statement, (student_id,))
        except Exception as e:
            raise RecordNotFoundException(e.args)
        results = self.cursor.fetchall()
        if results:
            return [CourseStudentLink(*result) for result in results]
        else:
            return []

    def find_students_for_course(self, course_id):

        statement = "SELECT ID, COURSE_ID, STUDENT_ID FROM COURSE_STUDENT WHERE COURSE_ID=?"
        try:
            self.cursor.execute(statement, (course_id,))
        except Exception as e:
            raise RecordNotFoundException(e.args)
        results = self.cursor.fetchall()
        if results:
            return [CourseStudentLink(*result) for result in results]
        else:
            return []

    def insert(self, course_id, student_id):
        statement = "INSERT INTO COURSE_STUDENT (COURSE_ID, STUDENT_ID) VALUES (?, ?)"
        try:
            self.cursor.execute(statement, (course_id, student_id))
            self.connection.commit()
        except Exception as e:
            print(e.args)

    # def update(self, course: Course):
    #     statement = "UPDATE COURSE SET NAME=?, DESCRIPTION=? WHERE ID=?"
    #     self.cursor.execute(statement, (course.name, course.description, course.id))
    #     try:
    #         self.connection.commit()
    #     except Exception as e:
    #         raise DbUpdateException(e.args)

    def delete(self, link: 'CourseStudentLink'):
        statement = "DELETE FROM COURSE_STUDENT WHERE ID=?"
        self.cursor.execute(statement, (link.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class UnitOfWork:
    current = threading.local()

    def __init__(self):
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []
        self.connection = connection

    def register_new(self, obj):
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        self.dirty_objects.append(obj)

    def register_removed(self, obj):
        self.removed_objects.append(obj)

    def commit(self):
        self.insert_new()
        # self.update_dirty()
        self.delete_removed()

    def insert_new(self):
        for obj in self.new_objects:
            CourseStudentLinkMapper(self.connection).insert(obj)

    # def update_dirty(self):
    #     for obj in self.dirty_objects:
    #         MapperRegistry.get_mapper(obj).update(obj)

    def delete_removed(self):
        for obj in self.removed_objects:
            CourseStudentLinkMapper(self.connection).delete(obj)

    @staticmethod
    def new_current():
        __class__.set_current(UnitOfWork())

    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work

    @classmethod
    def get_current(cls):
        return cls.current.unit_of_work


class DomainObject:
    def mark_new(self):
        UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        UnitOfWork.get_current().register_removed(self)


class CourseStudentLink(DomainObject):
    def __init__(self, link_id, course_id, student_id):
        self.id = link_id
        self.course_id = course_id
        self.student_id = student_id
