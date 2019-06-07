import os
from sys import platform
from httplib2 import Http
from apiclient import discovery
from oauth2client import tools, file, client
from RasAsiVer2.Decorators.Decorators import errors_decorator, time_decorator


class GoogleSpreadsheet:
    _SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    if platform == 'win32':
        path_credential = r'C:\PycharmProjects\RasAsi\credentials'  # Laptop
        # path_credential = r'C:\PythonProject\RasAsi\credentials'  # PC
        _client_secret = path_credential + r'\client_secret.json'
    elif platform == 'linux':
        # path_credential = r'/home/pi/Downloads'  # raspbian
        path_credential = r'~/PycharmProjects/RasAsi/credential'  # Ubuntu
        _client_secret = path_credential + r'/client_secret.json'
    else:
        print(f'Платформа {platform} не поддерживается')

    store = file.Storage(os.path.join(path_credential, 'RasAsi_Spreadsheets.json'))
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(_client_secret, _SCOPES)
        creds = tools.run_flow(flow, store)

    SHEETS = discovery.build('sheets', 'v4', http=creds.authorize(Http()))

    @errors_decorator
    def __init__(self):
        self._spreadsheet = None
        self.spreadsheet_id = None


    @errors_decorator
    def create_table(self, table_name):
        spreadsheet = {
            'properties': {
                'title': table_name
            }
        }
        self._spreadsheet = self.SHEETS.spreadsheets().create(body=spreadsheet).execute()
        self.spreadsheet_id = self._spreadsheet.get('spreadsheetId')

    @errors_decorator
    def get_spreadsheets_values(self, spreadsheet_id, range_name):
        result = self.SHEETS.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        return result

    @errors_decorator
    def batchGet_spreadsheets_values(self, spreadshhet_id, range_names):
        #range_names = []
        result = self.SHEETS.spreadsheets().values().batchGet(spredsheetId=spreadshhet_id, range=range_names).execute()

    @errors_decorator
    def update_spreadsheets_values(self, values, spreadsheet_id, range_name):
        """

        :param values: [[x, y, z], [x1, y1, z1]]
        :param spreadsheet_id: '2131lsdDqq2'
        :param range_name: 'Лист1' or 'Лист1!G2' or 'Лист1!C2:D5'
        :return: Nothing
        """
        body = self.body_formation(values=values)
        result = self.SHEETS.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name, body=body,
                                                            valueInputOption="USER_ENTERED").execute()
        # r1 = result.get('updateCells')

    @errors_decorator
    def batchUpdate_spreadshets_values(self, spreadsheet_id, range_name, values):
        """
        # range_name = []
        # data = [{}, {}, {}] - используй body formation
        # vales = [[[x, y, z], [x, y, z]], [[]], [[]]] - верхний - под range'и,
        # средний - список строк заполняющий каждый диапозон
        # нижний - значения в каждую ячейку
        """
        data = []
        for i in range(len(range_name)):
            print(values[i])
            data.append({'range': range_name[i],
                         'values': values[i]})
        # data = [
        #     {
        #         'range': range_name,
        #         'values': values
        #     },
        # ]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.SHEETS.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        # r1 = result.get('updateCells')

    @errors_decorator
    def append_spreadsheets_values(self, values, spreadsheet_id, range_name, valueInputOption='USER_ENTERED'):
        """

        :param values: [[x, y, z], [x1, y1, z1]]
        :param spreadsheet_id: 'asdas2dl12knjd;S412'
        :param range_name: 'Лист1' or 'Лист1!C2'
        :param valueInputOption: Default
        :return:
        """
        body = {
            'values': values
        }
        result = self.SHEETS.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name, body=body,
                                                            valueInputOption=valueInputOption).execute()
        # r1 = result.get('updates').get('updatedCells')

    def body_formation(self, values, majorDimension = "ROWS"):  # возможно нужен для формирования списка из тел
                                                                # для заполнения нескольких диапозонов
        """

        :param values: [[x, y, z], [x1, y1, z1]]
        :param majorDimension: Default
        :return: dict
        """

        body = {
            "majorDimension": majorDimension,
            "values": values
        }
        return body

if __name__ == '__main__':
    GoogleSpreadsheet()
else:
    print(f'Подключен модуль {__name__}')