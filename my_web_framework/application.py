class Application:
    def __init__(self, front_controllers: list, model):
        self.urls = {}

        self.front_controllers = front_controllers
        self.model = model

    def __call__(self, environ: dict, start_response):
        self.env = environ
        for front_controller in self.front_controllers:
            front_obj = front_controller(self.env)
            self.env = front_obj()
        page_controller = self.get_controller()
        status, body = page_controller(self.env, self.model)
        headers = [
            ('Content-type', 'text/html'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, headers)
        return [body]

    def get_controller(self):
        class NotFoundPage:
            def __call__(self, request, model):
                status_code = '404 Not Found'
                body = b'<h1>!Page not found. 404 Error !!!</h1>'
                return status_code, body

        path = self.env['PATH_INFO']
        # remove final slash from the path
        if len(path) > 1:
            if path[-1] == '/':
                path = path[:- 1]

        return self.urls[path] if path in self.urls else NotFoundPage()

    def url(self, route):
        def wrapper(controller):
            self.urls[route] = controller()
            return controller

        return wrapper
