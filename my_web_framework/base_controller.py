from jinja2 import Environment, FileSystemLoader


class BaseController:

    def get_rendered_template(self, template_name):
        template = Environment(loader=FileSystemLoader('templates')).get_template(template_name)
        return template.render().encode('utf8')
