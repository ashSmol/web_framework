from controllers import Index
from controllers import About
from controllers import Contact
from controllers import CourseCategories
from controllers import Courses
from controllers import Students
from controllers import CreateCategory

ROUTES = {
    '/': Index(),
    '/about': About(),
    '/contact': Contact(),
    '/categories': CourseCategories(),
    '/courses': Courses(),
    '/students': Students(),
    '/create_category': CreateCategory(),

}
