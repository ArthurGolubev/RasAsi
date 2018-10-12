import os

"""
для быстрого доступа к документации
"""
def help1():
    # help(subprocess)
    # print(os.getppid('11856'))
    # raise SystemExit
    # print('mark #1')
    os.chdir(r'F:\REMOTE SENSING DATA\hurricane-florence\pre-event\2018-09-06')
    n = os.path.getsize('153_0203323.tif.ovr')
    n = n//1024//1024
    print(n)
    # n = n/1024
    # n = n/1024
    # print(n)
    # return map(int, check_output(["pidof", name], shell=True))
    raise SystemExit