"""
Импортируется пакет (библиотека) RasAsiVer1
Это инициализирует в ней файл __init__.py (RasAsiVer1/__init__.py)
1_В котором импортируется пакет (библиотека) Download_Packeg -> Download_Packeg/__init__.py
2_Это инициализирует в нём файл __init__.py (Download_Packeg/__init__.py)
3_Файл __init__.py (Download_Packeg/__init__.py) импортирует из файла downloadScript.py переменную a2
4_таким образом в Download_Packeg, а именно в его __init__.py содержится переменная a2
5_БЛАГОДАРЯ ЭТОМУ текущий файл __init__.py (RasAsiVer1->__init__.py) имеет возможность
импортировать переменную a2 из пакета Download_Packeg, которую он, в свою очередь, импортировал
в себя (в свой файл __init__.py) из файла downloadScript_03.py
6_Таким образом вместо обращения к переменной a2 через

RasAsiVer1.Download_Packeg.downloadScript.a2

мы можем обращатся к переменной просто
RasAsiVer1.a2
"""
from .Download_Packeg import listOfOrder, download, prost, copyfun, prost2

