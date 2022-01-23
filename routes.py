from controllers import Index
from controllers import About
from controllers import Contact

ROUTES = {
    '/': Index(),
    '/about': About(),
    '/contact': Contact(),
}
