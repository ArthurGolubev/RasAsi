
def errors_decorator(func):
    from apiclient import errors

    def wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
        except errors.HttpError as error:
            print('ERRRRRRR\n\n' ,error)
            ret = None
        return ret
    return wrapper


def time_decorator(func):
    from time import time

    def wrapper(*args, **kwargs):
        start_time = time()
        ret = func(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f'{func.__name__} выполнено за {elapsed_time} секунд')
        return ret
    return wrapper
