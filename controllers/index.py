from my_web_framework import BaseController, Debug

from my_site import application


@application.url('/')
class Index(BaseController):
    @Debug()
    def __call__(self, request, model):
        status_code = '200 OK'
        template_params = {}
        body = self.get_rendered_template('index.html', template_params)
        return status_code, body
