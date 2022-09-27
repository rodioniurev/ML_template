# decorator
from abc import ABCMeta, abstractmethod


class Decor:
    def __init__(self, component):
        self.component = component.data

    @abstractmethod
    def decorate(self):
        pass


class CheckLength(Decor):
    def decorate(self):
        if isinstance(self.component, list):
            print(f'List length: {len(self.component)}')


class Decorated:
    def __init__(self, data: list):
        self.data = data


decorated = Decorated([1, 2, 3, 4, 5])
print(1)
check_length = CheckLength(decorated)
print(2)
check_length.decorate()
print(3)
