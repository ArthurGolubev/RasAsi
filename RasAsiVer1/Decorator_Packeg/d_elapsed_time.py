import datetime


def elapsed_time(analysis_function):
    sTime = datetime.datetime.now()
    analysis_function()
    eTime = datetime.datetime.now()
    print(f'Время выполнения:\t{eTime-sTime}')
    input('pause\t')
    return analysis_function
