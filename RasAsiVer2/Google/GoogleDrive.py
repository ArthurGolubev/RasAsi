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
        _path_token = r'..\..\credentials\GoogleDrive_token.pickle'
        _path_client_secret = r'..\..\credentials\client_secret.json'
    elif platform == 'linux':
        _path_token = r'/../../credentials/GoogleDrive_token.pickle'
        _path_client_secret = r'/../../credentials/client_secret.json'
    else:
        print('Платформа не поддерживаетя')

    _creds = None
    if os.path.exists(_path_token):
        with open(_path_token, 'rb') as _token:
            _creds = pickle.load(_token)
    if not _creds or not _creds.valid:
        if _creds and _creds.expired and _creds.refresh_token:
            _creds.refresh(Request())
        else:
            _flow = InstalledAppFlow.from_client_secrets_file(_path_client_secret, _SCOPES)
            _creds = _flow.run_local_server(port=0)
            with open(_path_token, 'wb') as _token:
                pickle.dump(_creds, _token)

    _GoogleDrive = build('drive', 'v3', credentials=_creds)

    def upload(self, files, folder_id=None):
        """

        :param folder_id: sds
        :param files: files = (('/path/to/file', None), ('/path/to/file', application/vnd.google-apps.document), (...))
        :return: Nothing
        """
        name = os.path.basename(files)
        print(name)
        files = ((files, None),)
        for filename, mimeType in files:
            metadata = {'name': name}
            if folder_id:
                metadata.update({'parents': [folder_id]})

            respond = self._GoogleDrive.files().create(body=metadata, media_body=filename).execute()

            if respond:
                print('SUCCESS')


if __name__ == '__main__':
    GoogleDrive().upload(r'C:\Users\ArthurGo\Downloads\test.jpg', folder_id='1CpsaUbjn2_4Zm6Sog05BBQwf3MEqQ2Vk')