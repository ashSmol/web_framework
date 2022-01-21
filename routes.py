from controllers.index import Index
from controllers.about import About

ROUTES = {
    '/': Index(),
    '/about': About(),
    # '/contacts':contacts,
}
