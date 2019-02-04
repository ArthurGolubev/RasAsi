import os

'''О, Чудо из чудес! Создание 10 папок)'''
path1 = 'F:\ФОТО\Work'
print(len(os.listdir(path1)))
amount1 = len(os.listdir(path1))

try:
    for i1 in reversed(range(1, amount1 + 1)):
        os.removedirs(f'{path1}\Sample {i1}')
except OSError:
    print(f'В папке было {amount1 - i1} пустой элемент\nДобавляю 10 папок\nОбщее количество:\t{i1 + 10} папок')
    for i2 in range(len(os.listdir(path1)) + 1, len(os.listdir(path1)) + 11):
        os.makedirs(f'{path1}/Sample {i2}')
