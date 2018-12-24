from work_composition.my_query import *
from work_composition.queri_select import *
print('from Initial_r')


def initial_request():

    request_today = query_select(zapros5, datetime.datetime.today().date())

    print('\n{:,^47}'.format(' mark #0 from: ') + '\n{: ^47}'.format(__name__) + '\n{:,^47}'.format('') + '\n')  #<<<<_MARK_<<<<
    if not request_today:
        """СПИСОК из кортежей, возвращённый из запроса к БД, ПУСТ. В БД нет сегодняшней даты"""

        print('В таблице calendar нет сегодняшней даты')
        today = datetime.datetime.today().date()  # Note:создаёт объект today (не ссылку на вызов метода класса)

        todays_id = query_insert1(zapros1, today)
        print('{:-^47}'.format('Календарь обнавлён'), f'\nСобытие добавленно сегодняшним днём: {today}' +
              '\n{:-^47}'.format(''))
        # TODO: добавить такое форматирование в вывод "времени записи в файл?

    else:
        '''Сегодняшняя дата уже добавлена в calendar и соответствует первому элементу кортежа первого элемента списка'''

        """        
        первый 0 - из СПИСКА кортежей всех строк таблицы, пришедших из запроса, выбираем первую строку
        второй 0 - из выбранной СТРОКИ ТАБЛИЦЫ, представленной кортежем её полей, выбираем первое поле

        Note:
        все элементы пришедшие из запроса имеют вид кортежей, в не зависимости от того состоит кортеж из 1 элемента или нет
        """

        print('В таблице календарь уже существует сегодняшняя дата')
        todays_id = request_today[0][0]
        # TODO: добавить бьютефул месадж
        print('mark #1 today_id:', todays_id)

    return todays_id
