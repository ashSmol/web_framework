from controllers.not_found import NotFoundPage
from routes import ROUTES

class Application:
    def __init__(self) -> None:
        self.routes = ROUTES


    def __call__(self, environ:dict, start_response):
        headers = [('Content-type', 'text/plain')]
        controller = self.get_controller(environ)
        print('----------------------')
        print(controller)
        print('----------------------')
        status, body = controller()
        start_response(status, headers)
        return [body]

    def get_controller(self, environ:dict):
        path = environ['PATH_INFO']
        print('!!!!!!!PATH!!!!!!!!!!!')
        print(path)
        print(f'path in routes: {path in ROUTES}')
        print('!!!!!!!PATH!!!!!!!!!!!')
        return ROUTES[path] if path in ROUTES else NotFoundPage()

application = Application()