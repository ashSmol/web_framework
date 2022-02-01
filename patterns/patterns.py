from model import CourseCategory, Course


class ObjectBuilder:
    def __init__(self, obj_type):
        if obj_type == 'category':
            self.obj = CourseCategory()
        elif obj_type == 'course':
            self.obj = Course()
        else:
            raise ValueError(f'Object type {obj_type} is not defined')

    def set_obj_name(self, name):
        self.obj.name = name
        return self

    def set_obj_description(self, description):
        self.obj.description = description
        return self

    def build(self):
        return self.obj
