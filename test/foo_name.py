def test_foo():
    print('test')


class TestName:
    def start(self):
        print('Class TestName')


class Facade:
    def __init__(self, name: str):
        self.model = eval(f'{name}()')

    def run(self):
        self.model.start()

test_name = TestName

facade = Facade('test_name')
facade.run()

