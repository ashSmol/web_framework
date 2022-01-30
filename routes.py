from controllers import Index
from controllers import About
from controllers import Contact
from controllers import CourseCategories

ROUTES = {
    '/': Index(),
    '/about': About(),
    '/contact': Contact(),
    '/course_categories': CourseCategories()
}
