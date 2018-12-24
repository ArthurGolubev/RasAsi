import datetime
import urllib.request, time, os, datetime, subprocess
import mysql.connector, datetime
from mysql.connector import Error
from work_composition.queri_select import query_select
from work_composition.query_insert import query_insert1
from sys import platform
from .config import config
from work_composition.my_query import *
# TODO создать и открыть тут локальный файл с аргументами для подключения к DateBase
print('print from __init__')