from datetime import datetime, timedelta
from time import sleep


print(datetime.strftime(datetime.now(), '%B'))


def initTime():
    startTimeRasAsi = datetime.now()
    return startTimeRasAsi


def timeHasPassed(inittime):
    sleep(2)
    t1 = datetime.now() - inittime
    print(t1)
    t2 = t1 - timedelta(microseconds=t1.microseconds)
    print(t2)
    return t2

if __name__ == '__main__':
    print(timeHasPassed(initTime()))