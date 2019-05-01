# import threading
from RasAsiVer2.Decorators.Decorators import logging_decorator
# k = ['g', 'g', 't', 'p']
#
# def kkk():
#     for i in range(10):
#         print(9)
#         print(k[i])
#
# @logging_decorator
# def justFunc():
#     input('pause\t')
#     kkk()
#
# k1 = threading.Thread(target=justFunc, name='justFFF')
#
# k1.start()
#
# print('oe')
#

@logging_decorator
def f(k):
    return k*2

ks = f(7)
print(ks)