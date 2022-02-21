from pprint import pprint

from my_web_framework import BaseController, Debug
from patterns import ObjectBuilder

from my_site import application


@application.url('/create_category')
class CreateCategory(BaseController):
    @Debug()
    def __call__(self, request, model):
        status_code = '200 OK'
        template_params = {}

        print('*' * 100)
        pprint(self.get_request_method(request))
        print('*' * 100)

        if self.get_request_method(request) == 'GET':
            pprint(self.get_get_params(request))

        if self.get_request_method(request) == 'POST':
            template_params.update(self.get_post_params(request))
            print(f'template params: {template_params}')

            new_category = ObjectBuilder('category')
            new_category.set_obj_name(template_params['category_name'])
            new_category.set_obj_description(template_params['category_description'])
            new_category = new_category.build()
            model.course_categories.append(new_category)
            template_params.update({'category': new_category})

            body = self.get_rendered_template('create_category.html', template_params)
            return status_code, body

        template_params.update({'categories': model.course_categories})
        body = self.get_rendered_template('create_category.html', template_params)

        return status_code, body
