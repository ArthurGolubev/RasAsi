from RasAsiVer2.Decorators.Decorators import logging_decorator

@logging_decorator
def my_error_f():
    raise EOFError

my_error_f()


