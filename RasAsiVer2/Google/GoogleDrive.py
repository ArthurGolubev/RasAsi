import pickle
import os.path
from sys import platform
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class GoogleDrive:
    _SCOPES = [
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.file'
    ]

    if platform == 'win32':
        print(1)
        _path = r'..\..\credentials\GoogleDrive_token.pickle'
    elif platform == 'linux':
        _path = r''  # TODO Написать путь
    else:
        print('Платформа не поддерживаетя')

    _creds = None
    if os.path.exists(_path):
        with open(_path, 'rb') as _token:
            _creds = pickle.load(_token)
    if not _creds or not _creds.valid:
        if _creds and _creds.expired and _creds.refresh_token:
            _creds.refresh(Request())
        else:
            _flow = InstalledAppFlow.from_client_secrets_file(r'..\..\credentials\client_secret.json', _SCOPES)
            _creds = _flow.run_local_server(port=0)
            with open(r'..\..\credentials\GoogleDrive_token.pickle', 'wb') as _token:
                pickle.dump(_creds, _token)

    _GoogleDrive = build('drive', 'v3', credentials=_creds)

    def upload(self, files):
        """

        :param files: files = (('/path/to/file', None), ('/path/to/file', application/vnd.google-apps.document), (...))
        :return: Nothing
        """
        name = os.path.basename(files)
        print(name)
        files = ((files, None),)
        for filename, mimeType in files:
            metadata = {'name': name}
            respond = self._GoogleDrive.files().create(body=metadata, media_body=filename).execute()

            if respond:
                print('SUCCESS')


if __name__ == '__main__':
    GoogleDrive().upload(r'C:\Users\ArthurGo\Downloads\test.jpg')