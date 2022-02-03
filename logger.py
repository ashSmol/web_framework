import os

from patterns import Singleton


class Logger(metaclass=Singleton):
    def __init__(self, logger_name):
        self.name = logger_name

    def log(self, text):
        print(f'Logger {self.name}___: {text}')
        if not os.path.isfile(f'{self.name}.txt'):
            with open(f'{self.name}.txt', 'w') as log_file:
                log_file.write(text + '\n')
        else:
            with open(f'{self.name}.txt', 'a') as log_file:
                log_file.write(text + '\n')
