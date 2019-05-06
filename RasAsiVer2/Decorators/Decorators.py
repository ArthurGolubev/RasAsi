def errors_decorator(func):
    from apiclient import errors

    def wrapper(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
        except errors.HttpError as error:
            print('ERRRRRRR\n\n', error)
            ret = None
        return ret
    return wrapper


def time_decorator(func):
    from time import time

    def wrapper(*args, **kwargs):
        start_time = time()
        ret = func(*args, **kwargs)
        elapsed_time = time() - start_time
        print(f'{func.__name__} выполнено за {elapsed_time} сек')
        return ret
    return wrapper


def logging_decorator(func):
    import logging
    from RasAsiVer2.Google.GoogleGmail import GoogleGmail
    from datetime import datetime

    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='logfile.txt', level=logging.ERROR, filemode='w')
        try:
            ret = func(*args, **kwargs)
        except:
            logging.getLogger().exception(f'name:\t\t{func.__name__}\t\t {datetime.now().strftime("%d.%m.%Y %HH:%MM:%SS")}')
            ret = None
            with open('logfile.txt', 'r') as file:
                GoogleGmail().send_message(topic=f'😒 Error from {func.__name__}',
                                           message_text=file.read())
        return ret
    return wrapper

