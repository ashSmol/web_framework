from urllib.parse import unquote

from jinja2 import Environment, FileSystemLoader


class BaseController:
    def get_rendered_template(self, template_name):
        template = Environment(loader=FileSystemLoader('templates')).get_template(template_name)
        return template.render().encode('utf8')

    def get_request_method(self, env: dict) -> str:
        return env['REQUEST_METHOD']

    def get_get_params(self, env) -> dict:
        request_params = {}
        query = env['QUERY_STRING']
        if len(query) > 0:
            request_params = self.parse_request_params(query)
        return request_params

    def get_post_params(self, env) -> dict:
        request_params = {}
        content_length_param = env['CONTENT_LENGTH']
        if content_length_param:
            content_length = int(content_length_param)
            request_params_bytes: str = env['wsgi.input'].read(content_length) if content_length > 0 else b''
            request_params = self.parse_request_params(unquote(request_params_bytes.decode('utf-8')))
        return request_params

    def parse_request_params(self, query) -> dict:
        request_params = {}
        dict_items = query.split('&')
        for item in dict_items:
            key, val = item.split('=')
            request_params.update({key: val})
        return request_params
