class Application:
    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ: dict, start_response):
        rq = {}
        headers = [('Content-type', 'text/plain')]
        for front_controller in self.front_controllers:
            front_controller(rq)
        page_controller = self.get_controller(environ)
        status, body = page_controller()
        start_response(status, headers)
        return [body]

    def get_controller(self, environ: dict):
        class NotFoundPage:
            def __call__(self):
                status_code = '404 Error'
                body = b'Page not found. 404 Error'
                return status_code, body

        path = environ['PATH_INFO']
        return self.routes[path] if path in self.routes else NotFoundPage()
