# Задание к 8му уроку:

1. Повсеместно обнаружил ___Слепую Веру___. Исправил, добавив валидацию значений, которые пишутся в базу данных, для
   всех маперов. Добавил валидацию при создании объекта студента. Имя\фамилия должны быть длиннее 3 символов и не должны содержать пробелов.
2. Anemic Domain Model. Классы модели не содержат никакой логики. Они представляют собой просто набор атрибутов. Исправил это - добавил для класса студент валидацию атрибутов объекта.
3. Jumble // Путаница. models/course_student_link.py содержит путаницу. Код в файле содержит элементы модели(класс можели связи курса и студента), взаимодействие с БД(мапер), а так же код Единицы работы и абстракнтный класс DomainObject. Исправить не успеваю. Чтобы исправить нужно разнести этот код по своим соответсвующим слоям. Пытался это сделать. При первой попытке встретил цикличность импортов.
   

# web_framework

***
Project contains ___my_db.db___, that is required for running project. In case it is corrupted or missing, run ___
create_db.py___ in the root path of the project
***

***
To start my_site (which is created via my_web_framework) use command:

```bash
gunicorn my_site
```

Open
[course page](http://127.0.0.1:8000/course?name=Python). See a form 'Sign up a student for course' at the bottom of
page. To Add a student to the current course, select a student in the deopdown list and press 'Sign up' button

```
http://127.0.0.1:8000
```

[index page link](http://127.0.0.1:8000)

```
http://127.0.0.1:8000/about
```

[about page link](http://127.0.0.1:8000/about)

```
http://127.0.0.1:8000/asdad
```

[404 not found page link](http://127.0.0.1:8000/asdad)

```
http://127.0.0.1:8000/about/
```

[about page link with final slash symbol](http://127.0.0.1:8000/about/)