from model import Student, Course


class RecordNotFoundException(Exception):
    def __init__(self, msg):
        raise Exception(f'Record not found! \n {msg}')


class DbCommitException(Exception):
    def __init__(self, msg):
        raise Exception(f'Fail to commit! \n {msg}')


class DbUpdateException(Exception):
    def __init__(self, msg):
        raise Exception(f'Fail to update! \n {msg}')


class DbDeleteException(Exception):
    def __init__(self, msg):
        raise Exception(f'Fail to delete! \n {msg}')


class StudentMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_all(self):
        statement = "SELECT * FROM STUDENT"
        self.cursor.execute(statement, )
        results = self.cursor.fetchall()
        if results:
            return [Student(*result) for result in results]
        else:
            return []

    def find_by_id(self, student_id):
        statement = "SELECT ID, NAME, SURNAME FROM STUDENT WHERE ID=?"
        self.cursor.execute(statement, (student_id,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFoundException(f'record with id={student_id} not found')

    def insert(self, student):
        statement = "INSERT INTO STUDENT (NAME, SURNAME) VALUES (?, ?)"
        self.cursor.execute(statement, (student.name, student.surname))
        try:
            self.connection.commit()
            result = self.cursor.execute('select last_insert_rowid()',
                                         ).fetchone()
            student.id = result[0]

        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, student):
        statement = "UPDATE STUDENT SET NAME=?, SURNAME=? WHERE ID=?"
        self.cursor.execute(statement, (student.name, student.surname, student.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, student: Student):
        statement = "DELETE FROM STUDENT WHERE ID=?"
        self.cursor.execute(statement, (student.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class CourseMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_all(self):
        statement = "SELECT * FROM COURSE"
        self.cursor.execute(statement, )
        results = self.cursor.fetchall()
        if results:
            return [Course(*result) for result in results]
        else:
            return []

    def find_by_id(self, course_id):
        statement = "SELECT ID, NAME, DESCRIPTION FROM COURSE WHERE ID=?"
        self.cursor.execute(statement, (course_id,))
        result = self.cursor.fetchone()
        if result:
            return Course(*result)
        else:
            raise RecordNotFoundException(f'record with id={course_id} not found')

    def insert(self, course: Course):
        statement = "INSERT INTO COURSE (NAME, DESCRIPTION) VALUES (?, ?)"
        self.cursor.execute(statement, (course.name, course.description))
        try:
            self.connection.commit()
            result = self.cursor.execute('select last_insert_rowid()',
                                         ).fetchone()
            course.id = result[0]
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, course: Course):
        statement = "UPDATE COURSE SET NAME=?, DESCRIPTION=? WHERE ID=?"
        self.cursor.execute(statement, (course.name, course.description, course.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, course: Course):
        statement = "DELETE FROM COURSE WHERE ID=?"
        self.cursor.execute(statement, (course.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)
