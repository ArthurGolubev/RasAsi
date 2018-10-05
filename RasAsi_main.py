print('Hello!\nMy name is Raspberry Pi Asistent')
import RasAsiVer1
RasAsiVer1.prost()
RasAsiVer1.prost2()


"""
необходим список всех доступных операций
"""
capabilityPackeg = []
for i in dir(RasAsiVer1):
    if i.endswith('Packeg'):
        capabilityPackeg.append(i)
print(f'Список доступных пакетов (тест1)\n{capabilityPackeg}')

print(len(capabilityPackeg))
iterator1 = []
for i in range(0, len(capabilityPackeg)):
    iterator1.append(i+1)
print(iterator1)
dict1 = dict.fromkeys(capabilityPackeg, iterator1)
print(dict1)




"""
почитать документацию
dir()
"""

#добавить вывод доступных команд построено с нумерацией
#создать словарик с ключами - нумерацией и содержанием - доступными функциями


