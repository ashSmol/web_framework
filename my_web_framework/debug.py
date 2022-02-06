import time


class Debug:

    def __call__(self, controller):
        def wrapper(*args, **kwargs):
            star_time = time.time()
            result = controller(*args, **kwargs)
            print(f'Running {controller.__module__} took {time.time() - star_time}')
            return result

        return wrapper
