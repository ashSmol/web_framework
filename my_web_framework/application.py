from urllib.parse import unquote

class Application:
    def __init__(self, routes: dict, front_controllers: list):
        self.routes = routes
        self.front_controllers = front_controllers

    def __call__(self, environ: dict, start_response):
        self.env = environ
        rq = self.get_request_params()
        for front_controller in self.front_controllers:
            front_obj = front_controller(rq)
            rq = front_obj()
        page_controller = self.get_controller()
        status, body = page_controller(rq)
        headers = [
            ('Content-type', 'text/html'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, headers)
        return [body]

    def get_controller(self):
        class NotFoundPage:
            def __call__(self, request):
                status_code = '404 Not Found'
                body = b'<h1>!Page not found. 404 Error !!!</h1>'
                return status_code, body

        path = self.env['PATH_INFO']
        # remove final slash from the path
        if len(path) > 1:
            if path[-1] == '/':
                path = path[:- 1]

        return self.routes[path] if path in self.routes else NotFoundPage()

    def get_request_method(self):
        return self.env['REQUEST_METHOD']

    def get_request_params(self) -> dict:
        request_params = {}
        if self.get_request_method() == 'GET':
            query = self.env['QUERY_STRING']
            if len(query) > 0:
                request_params = self.parse_request_params(query)
        else:
            content_length_param = self.env['CONTENT_LENGTH']
            if content_length_param:
                content_length = int(content_length_param)
                request_params_bytes:str = self.env['wsgi.input'].read(content_length) if content_length > 0 else b''
                request_params = self.parse_request_params(unquote(request_params_bytes.decode('utf-8')))
        return request_params

    def parse_request_params(self, query) -> dict:
        request_params={}
        dict_items = query.split('&')
        for item in dict_items:
            key, val = item.split('=')
            request_params.update({key: val})
        return request_params