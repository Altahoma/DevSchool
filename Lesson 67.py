class Name:
    def __init__(self, f_name, l_name):
        self.first_name = f_name.title()
        self.last_name = l_name.title()
        self.full_name = f'{self.first_name} {self.last_name}'
        self.initials = f'{self.first_name[0]}.{self.last_name[0]}'


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


class Employee:
    def __init__(self, f_name, l_name, salary):
        self.first_name = f_name.title()
        self.last_name = l_name.title()
        self.salary = int(salary)

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary = string.split('-')
        return cls(f_name, l_name, salary)
