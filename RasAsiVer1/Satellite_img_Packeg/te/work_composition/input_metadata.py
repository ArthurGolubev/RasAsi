# from .queri_select import query_select
# from .query_insert import query_insert1
# from .my_query import *
# from . import config

from work_composition.queri_select import query_select
from work_composition.query_insert import query_insert1
from work_composition.config import *
from work_composition.my_query import *

def input_metadata(plist, titledict):
    # TODO: написать документацию к модулю
    print('MY DICT IS BIG', titledict)
    if plist[0].startswith('http'):
    # TODO: добавить if если это путь в файловой системе (/home/....)
        if plist[2] == 'opendata.digitalglobe.com':
            SOURSE = 'DigitalGlobe'
            print('\n{:,^47}'.format(' mark #ЭТО ДИДЖИТАЛГЛОБ from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<<
            if plist[3] not in titledict.keys():
                print(f'Ищу {plist[3]} в таблице metadata')
                ok = query_select(DBq5, plist[3])
                if not ok:
                    print(f'ВСТАВЛЯЮ {plist[3]}')
                    last_id = query_insert1(DBq6, (plist[3], SOURSE))
                    # dict1 = {plist[3]: last_id}
                    titledict.update({plist[3]: last_id})
                    print('PRINT DICT OT SUDA   :', titledict)
                    return titledict
                else:
                    print('OKOKOKOKOKKOKOK', ok)
                    # TODO: удалить лишние dict
                    titledict.update({plist[3]: ok[0][0]})
                    print('PRINT DICT OT SUDA   :', titledict)
                    return titledict
            else:
                print(f'ТАКОЙ КЛЮЧ УЖЕ ЕСТЬ {plist[3]}')
                print('\n{:,^47}'.format(' mark #1 from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<< 0
                return titledict