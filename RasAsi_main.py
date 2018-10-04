print('Hello!\nMy name is Raspberry Pi Asistent')
import RasAsiVer1
print(dir())
RasAsiVer1.prost()
RasAsiVer1.prost2()


"""
необходим список всех доступных операций
"""
capabilities1 = []
for i in dir(RasAsiVer1):
    if i.startswith('_') == false:
        capabilities1.append(i)
print(f'Список доступных команд (тест1)\n{capabilities1}')

"""
почитать документацию
dir()
"""

#добавить вывод доступных команд построено с нумерацией
#создать словарик с ключами - нумерацией и содержанием - доступными функциями


