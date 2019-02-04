from sys import platform
from bs4 import BeautifulSoup
import requests
import os, datetime
from RasAsiVer1.WOrk_Packeg.LightDetailing.GetAU24.create_table import reportTable


def getAU24(classification_usr, userSearch):
    # TODO: добавить функционал выбора пользователя для анализа
    if platform == 'win32':
        path1 = 'F:\WOrk'
    elif platform == 'linux':
        path1 = '/media/pi/PORTABLE HDD'
    else:
        print('Платформа не поддерживается')
    if classification_usr == 'пользователь':
        link1 = f'https://au.ru/user/{userSearch}/lots/'
        link2 = f'https://au.ru/user/{userSearch}/lots/?page='
    elif classification_usr == 'магазин':
        link1 = f'https://au.ru/user/{userSearch}/shop/'
        link2 = f'https://au.ru/user/{userSearch}/shop/?group=active&page='

    # userSearch = 'ice23'
    # userSearch = 'ProFara'
    # userSearch = 'lightdetailing'
    # userSearch = 'sho21'


    startTime = datetime.datetime.now()
    # TODO: переименовать someDict
    someDict = runPages(GetSOMETHING_SHEET(getHTML(link1)), link2, userSearch, path1)
    cTime = datetime.datetime.now()
    formTime = cTime - datetime.timedelta(microseconds=cTime.microsecond)
    reportTable(f'{userSearch} - {formTime}', someDict)
    elapsedTime = datetime.datetime.now() - startTime
    elapsedTime = elapsedTime - datetime.timedelta(microseconds=elapsedTime.microseconds)
    print(f'Время выполнение программы {elapsedTime}')


def getHTML(url_1):
    responds1 = requests.get(url_1)
    return responds1.text


def GetSOMETHING_SHEET(HTML_1):
    '''Узнаём количество страниц'''
    soup = BeautifulSoup(HTML_1, 'html.parser')
    amountLots = int(soup.find('div', class_='au-micropager__title').text.replace('\xa0', ' ').split(' ')[2])
    print(f'Лотов - {amountLots}')
    if amountLots % 50:
        totalPages = int(amountLots / 50) + 1
    else:
        totalPages = int(amountLots / 50)
    return totalPages


def runPages(totalP, link2, userSearch, path1):
    someDict = {}
    justVar = 0
    for i in range(1, totalP + 1):
        externalPageHTML = getHTML(f'{link2}{i}')
        soup = BeautifulSoup(externalPageHTML, 'html.parser')
        lotsOnPage = soup.find('div', id='itemList_0').find_all('div', 'au-lots-item au-card-list-item')
        for i2 in lotsOnPage:
            justVar = justVar + 1
            print(f'Лот {justVar}')
            lotID = i2.get('data-lamber-object').split(':')[1]
            lotLink = f'https://krsk.au.ru/{lotID}/'
            someDict = lotParer(getHTML(lotLink), lotLink, someDict, userSearch, path1)
    return someDict


def lotParer(HTML, lotLink, someDict, userSearch, path1):
    soup = BeautifulSoup(HTML, 'html.parser')
    allPageContent = soup.find('div', class_='au-item-page-content au-item-page-content-vertical')

    contentTopRight = allPageContent.find('div', class_='au-item-page-content-vertical__top')
    contentLeftColumn = allPageContent.find('div', class_='au-item-page-content-vertical__lcol')
    contentRightColumn = allPageContent.find('div', class_='au-item-page-content-vertical__rcol')

    lotName = contentTopRight.find('h1').text.replace('/', ' ').replace('\\', ' ').replace('"', '').replace('*', 'x')

    print('TYPE\t', type(lotName), f'\t{lotName}')
    tagPath = contentTopRight.find('div', class_='au-breadcrumbs au-breadcrumbs_size_normal')
    lotGallery = contentLeftColumn.find('div', class_='au-item-page-gallery')

    if platform == 'linux':
        tagPath = path1 + r'/' + userSearch + r'/' + tagPath.get_text()
    elif platform == 'win32':
        tagPath = path1 + r'\ ' + userSearch + r'\ ' + tagPath.get_text().replace('/', '\\')
        try:
            os.makedirs(tagPath)
            os.chdir(tagPath)
        except FileExistsError:
            os.chdir(tagPath)

    lotPrice = str(contentRightColumn.find('span', class_='au-price__value').string).replace('\xa0', '')

    try:
        lotParametrs = lotParam(contentRightColumn.find('table', class_='au-lot-parameters__table').find_all('tr'),
                                tagPath, someDict, lotName, lotPrice, lotLink)
    except:
        lotParametrs = [['параметры', 'отсутствуют']]
        ifNoParametrs(someDict, lotName, lotPrice, lotLink, tagPath)
    try:
        lotPlace = contentRightColumn.find('div', class_='au-item-page-location-conditions').text
    except:
        lotPlace = 'Неуказано'

    try:
        downloadImg(lotName, lotGallery, tagPath)
    except:
        print('Фотографии лота отсутствуют')

    nameParam = f'{lotName}_{lotPrice}руб.txt'
    pathLen = 260 - len(os.getcwd())
    if len(nameParam) >= pathLen - 10:
        nameParam = nameParam[0:pathLen - 6] + '.txt'
    with open(nameParam, 'w') as file:
        file.write('ПАРАМЕТРЫ:\n')

        for i4 in lotParametrs:
            file.write(i4[0] + ' - ' + i4[1] + '\n')
        file.write(f'\n\nЦЕНА - {lotPrice} руб.\n')
        file.write(f'\nУСЛОВИЯ ПЕРЕДАЧИ:\n{lotPlace}')

    try:
        lotDescription = contentRightColumn.find('div', itemprop='description')
        open(f'description.html', 'wb').write(bytes(str(lotDescription).encode()))
    except:
        print('Описание лота отсутствует')
        open(f'description.html', 'wb').write(bytes('ОПИСАНИЕ ЛОТА ОТСУТСТВУЕТ'))
    return someDict


def downloadImg(lotName, lotGallery, tagPath):
    try:
        os.mkdir('фотографии')
        os.chdir(os.path.join(tagPath, 'фотографии'))
    except FileExistsError:
        os.chdir(os.path.join(tagPath, 'фотографии'))
    img = lotGallery.find_all('a')
    for i in range(len(img)):
        link = img[i].get('href')
        link = 'http:' + link
        r = requests.get(link, allow_redirects=True)
        namePic = f'{i + 1}_{lotName}.jpg'
        pathLen = 260 - len(os.getcwd())
        if len(namePic) >= pathLen - 10:
            namePic = namePic[0:pathLen - 6] + '.jpg'
        open(namePic, 'wb').write(r.content)
    os.chdir(tagPath)


def ifNoParametrs(someDict, lotName, lotPrice, lotLink, tagPath):
    tagPath = tagPath.split('\\')
    # print(tagPath)
    # print(tagPath[-3])
    # input('rop')
    if tagPath[-3] not in someDict:
        someDict[tagPath[-3]] = [[lotLink, lotName, lotPrice]]
    else:
        justVar = someDict.get(tagPath[-3])
        justVar.append([lotLink, lotName, lotPrice])
        someDict[tagPath[-3]] = justVar


def lotParam(lotParametrs, tagPath, someDict, lotName, lotPrice, lotLink):
    lotParametr = []
    os.chdir(tagPath)
    for i2 in lotParametrs:
        titlePar = i2.find('td', class_='au-lot-parameter__title').text
        valuePar = i2.find('td', class_='au-lot-parameter__value au-lot-parameter-value').text
        if titlePar == 'Элемент оптики':
            if valuePar not in someDict:
                someDict[valuePar] = [[lotLink, lotName, lotPrice]]
            else:
                justVar = someDict.get(valuePar)
                justVar.append([lotLink, lotName, lotPrice])
                someDict[valuePar] = justVar
        else:
            ifNoParametrs(someDict, lotName, lotPrice, lotLink, tagPath)
        lotParametr.append([titlePar, valuePar])
    return lotParametr


if __name__ != '__main__':
    print(f'ЗАПУСК МОДУЛЯ - {__name__}')
else:
    print('ВЫ ТЕСТИРУЕТЕ МОДУЛЬ')
    getAU24(classification_usr='магазин', userSearch=None)
