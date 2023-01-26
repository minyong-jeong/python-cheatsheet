class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    class_a = TestClass()
    class_b = TestClass()

    print(class_a)
    print(class_b)
