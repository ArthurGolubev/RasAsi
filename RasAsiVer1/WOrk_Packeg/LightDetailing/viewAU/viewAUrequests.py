import time
import random
from RasAsiVer1.WOrk_Packeg.LightDetailing.GetAU24.getAU24 import GetSOMETHING_SHEET, getHTML
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from sys import platform
from os import remove


def vievAUrequests():
    userSearch = 'lightdetailing'
    link1 = f'https://au.ru/user/{userSearch}/lots/'
    link2 = f'https://au.ru/user/{userSearch}/lots/?page='

    if platform == 'win32':
        path0 = r'C:\PythonProject\RasAsi\RasAsiVer1\WOrk_Packeg\LightDetailing\viewAU\{}.txt'
        path1 = path0.format(datetime.today().date())
    elif platform == 'linux':
        path0 = r'/home/pi/RasAsi/RasAsiVer1/WOrk_Packeg/LightDetailing/viewAU/{}.txt'
        path1 = path0.format(datetime.today().date())
    else:
        print('Платформа не поддерживается')
        raise SystemExit
    print(f'viewAU: Task completed {datetime.today().time()}')

    def getlinklist():
        totalP = GetSOMETHING_SHEET(getHTML(link1))
        print(f'Станиц - {totalP}')
        lotLink = []
        for i in range(1, totalP + 1):
            externalPageHTML = getHTML(f'{link2}{i}')
            soup = BeautifulSoup(externalPageHTML, 'html.parser')
            lotsOnPage = soup.find('div', id='itemList_0').find_all('div', 'au-lots-item au-card-list-item')
            for i2 in lotsOnPage:
                lotID = i2.get('data-lamber-object').split(':')[1]
                lotLink.append(f'https://krsk.au.ru/{lotID}/')
        return lotLink

    def getTodaylistlink():
        yesterday = datetime.today().date() - timedelta(days=1)
        print(yesterday)
        try:
            remove(path0.format(yesterday))
        except FileNotFoundError:
            print('ок')
        with open(path1, 'w') as file1:
            links = getlinklist()
            for i2 in links:
                file1.write(i2 + '\n')
        with open(path1, 'r') as file1:
            listlink1 = file1.readlines()
        return listlink1

    try:
        with open(path1, 'r') as file:
            listlink = file.readlines()
    except:
        listlink = getTodaylistlink()

    for i in range(int(len(listlink) / 3)):
        rlink = random.choice(listlink).replace('\n', '')
        getHTML(rlink)
        time.sleep(random.randint(1, 11))


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    vievAUrequests()
