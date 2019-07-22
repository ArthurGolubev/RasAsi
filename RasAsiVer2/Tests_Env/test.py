from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


    FILES = (
        (r'C:\Users\ArthurGo\Downloads\test.jpg', None),
        (r'C:\Users\ArthurGo\Downloads\test.jpg', 'application/vnd.google-apps.document'),
    )


    for filename, mimeType in FILES:
        metadata = {'name': filename}
        res = service.files().create(body=metadata, media_body=filename).execute()
        if res: print('SUCCESS')

    print(res)
    input('pause\t')
    # if res:
    #     MIMETYPE = 'application/jpeg'
    #     res, data = service._http.request(res['exportLinks'][MIMETYPE])
    #     if data:
    #         fn = '%s.pdf' % os.path.splitext(filename)[0]
    #         with open(fn, 'wb') as fh:
    #             fh.write(data)
    #         print('Download "%s" (%s)' % (fn, MIMETYPE))

if __name__ == '__main__':
    main()