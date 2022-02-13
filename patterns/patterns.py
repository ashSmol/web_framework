from model import CourseCategory, Course


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']
        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class ObjectBuilder:
    def __init__(self, obj_type):
        if obj_type == 'category':
            self.obj = CourseCategory()
        elif obj_type == 'course':
            self.obj = Course(None, None, None)
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
