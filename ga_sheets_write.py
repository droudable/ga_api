from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import csv

# If modifying thei scope, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'


from csv import reader as csvreader
with open('customdimensions.csv', 'r') as fp:
    reader = csvreader(fp)
    li = list(reader)
    print(li)
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', 'https://www.googleapis.com/auth/drive')
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    # Call the Sheets API
    sheet = service.spreadsheets()
# writing data to a spreadsheets
    values = [
                    li
    #Additional rows ...
                ]
    body = {
            'values': values
               }
    result = service.spreadsheets().values().update(
    spreadsheetId='1MOCyQ1q9Xuz6EIkW9453xlcol-W_K0wb87Ua5FfBa9U', range='write!a1:h30',
    valueInputOption='RAW', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))
