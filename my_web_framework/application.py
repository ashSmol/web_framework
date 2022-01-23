from pprint import pprint


class Application:
    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ: dict, start_response):

        rq = {}
        print('*' * 50)
        print(f'Request before front controller:\n {rq}')

        for front_controller in self.front_controllers:
            front_obj = front_controller(rq)
            rq = front_obj()
        print(f'Request after front controller:\n {rq}')
        page_controller = self.get_controller(environ)
        status, body = page_controller(rq)
        headers = [
            ('Content-type', 'text/html'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, headers)
        pprint(environ)
        return [body]

    def get_controller(self, environ: dict):
        class NotFoundPage:
            def __call__(self, request):
                status_code = '404 Not Found'
                body = b'<h1>!Page not found. 404 Error !!!</h1>'
                return status_code, body

        path = environ['PATH_INFO']
        # remove final slash from the path
        if len(path) > 1:
            if path[-1] == '/':
                path = path[:- 1]

        return self.routes[path] if path in self.routes else NotFoundPage()

    def get_request_method(self, environ: dict):
        return environ['REQUEST_METHOD']
