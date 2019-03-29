class kl:
    @staticmethod
    def decorator_errors( func):
        def try_():
            print(1)
            func()

        return try_

    def sp(self):
        print('hello')


if __name__ == '__main__':
    a = kl
    @kl.decorator_errors
    a.sp()