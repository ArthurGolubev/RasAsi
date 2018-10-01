def be():
    b='poka'
#
# # import os
# #
# # with open('F:\REMOTE SENSING DATA\logFileTransfer.txt', 'a'):
# #     os.chdir('F:\REMOTE SENSING DATA')
# #     listDirPC = set(os.listdir())
# #     os.chdir('G:\REMOTE SENSING IMG\DigitalGlobe')
# #     listDirPortableHDD = set(os.listdir())
# #     print(listDirPortableHDD)
# #     print(listDirPC)
# #     print(listDirPortableHDD.difference(listDirPC))
# #     print(listDirPC)
# #     print(listDirPortableHDD, 'mark #1')
# #     listDirPortableHDD.difference_update(listDirPC)
# #     print(listDirPC)
# #     print(listDirPortableHDD, 'mark #2')
# # # help(set)
# # a = [3, 3, 4, 52, 2]
# # b = [3, 3, 4, 5, 52, 2, 2]
# # print(a)
# # print(b)
# # # c = a.count()
# # # print(c)
# # # set1 = set(a)
# # # set2 = set(b)
# # # print(set1)
# # # print(set2)
# # # c = set1.__isub__(set2)
# # # print('\n',c)
#
# import os, shutil, time
#
# os.chdir(r'G:\REMOTE SENSING IMG\DigitalGlobe')
# listDirPHDD = set(os.listdir())
# os.chdir(r'F:\REMOTE SENSING DATA')
# listDirPC = set(os.listdir())
# newDirInPHHD = listDirPHDD.difference(listDirPC)
# os.chdir(r'G:\REMOTE SENSING IMG\DigitalGlobe')
#
# for i2 in os.walk(r'G:\REMOTE SENSING IMG\DigitalGlobe'):
#     print(i2)
# numberFile = 0
#
# # for i in newDirInPHHD:
# #     st = time.time()
# #     shutil.copytree(rf'G:\REMOTE SENSING IMG\DigitalGlobe\{i}', rf'F:\REMOTE SENSING DATA\{i}', ignore=shutil.ignore_patterns('*.rrd', '*.aux'))
# #     et = time.time() - st
# #     print(et)
