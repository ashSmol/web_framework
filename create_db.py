import sqlite3

connection = sqlite3.connect('my_db.db')
cursor = connection.cursor()

create_student_table = '''
CREATE TABLE IF NOT EXISTS STUDENT 
(
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
NAME VARCHAR (32), 
SURNAME VARCHAR (32)
);
'''

create_course_table = '''CREATE TABLE  IF NOT EXISTS COURSE 
(
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
NAME VARCHAR (32), 
DESCRIPTION VARCHAR (255)
);
'''

create_course_student = '''CREATE TABLE  IF NOT EXISTS COURSE_STUDENT 
(
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
COURSE_ID INTEGER,
STUDENT_ID INTEGER, 
UNIQUE (COURSE_ID, STUDENT_ID),
FOREIGN KEY (COURSE_ID) REFERENCES COURSE (ID),
FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT (ID)
);
'''

cursor.execute(create_course_table)
cursor.execute(create_student_table)
cursor.execute(create_course_student)
