print('Hello!\nMy name is Raspberry Pi Asistent')
import RasAsiVer1
print(dir())
RasAsiVer1.prost()
RasAsiVer1.prost2()


"""
необходим список всех доступных операций
"""


def test1():
    print(1)
print(dir(RasAsiVer1))
capabilities_1 = dir(RasAsiVer1)
print(len(capabilities_1))
for i in range(len(capabilities_1)-1):
    print(i)
    if capabilities_1[i].endswith('__'):
        capabilities_1.remove(capabilities_1[i])
    print(capabilities_1[i])
print(f'{capabilities_1} mark #1')

"""
почитать документацию
dir()
"""
# help(list)


