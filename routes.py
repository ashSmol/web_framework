from controllers import Index
from controllers import About

ROUTES = {
    '/': Index(),
    '/about': About(),
    # '/contacts':contacts,
}
