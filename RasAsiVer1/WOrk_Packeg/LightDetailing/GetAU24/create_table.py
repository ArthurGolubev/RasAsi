from apiclient import discovery
from httplib2 import Http
from oauth2client import tools, file, client
from sys import platform
from RasAsiVer1.WOrk_Packeg.LightDetailing.GetAU24.payload.sheetFunc import sheetFunc
from RasAsiVer1.WOrk_Packeg.LightDetailing.GetAU24.payload.dataFunc import dataFunc


def reportTable(nameTable, dictValues=None):
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    if platform == 'win32':
        # store = file.Storage(r'C:\PythonProject\storage_LightDetailing.json')
        store = file.Storage(r'C:\PythonProject\storage_RaspberryAssistant.json')
    elif platform == 'linux':
        print('УКАЖИ ПУТЬ')
    creds = store.get()

    if not creds or creds.invalid:
        if not creds or creds.invalid:
            if platform == 'linux':
                input('УКАЖИ ПУТЬ В КОДЕ')
                path1 = 'sdsdss'
            if platform == 'win32':
                path1 = r'C:\Users\arthu\Downloads\credentials.json'
        flow = client.flow_from_clientsecrets(path1, SCOPES)
        creds = tools.run_flow(flow, store)

    HTTP = creds.authorize(Http())
    SHEETS = discovery.build('sheets', 'v4', http=HTTP)

    spreadsheet = {
        'properties': {
            'title': nameTable
        },
        'sheets': sheetFunc(dictValues.keys())

    }
    spreadsheet = SHEETS.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute().get('spreadsheetId')

    data = {
        'valueInputOption': 'USER_ENTERED',
        'data': dataFunc(dictValues)
    }
    spreadsheet = SHEETS.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet, body=data).execute()
