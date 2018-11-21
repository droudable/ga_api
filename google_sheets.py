from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID_READ = '1MOCyQ1q9Xuz6EIkW9453xlcol-W_K0wb87Ua5FfBa9U'
RANGE_NAME_READ = 'read!$A1:$B30'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials_sheet_test.json', 'https://www.googleapis.com/auth/drive')
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID_READ,
                                range=RANGE_NAME_READ).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:

        sheets_data=[]
        for row in values:
             sheets_data.append((row[0], row[1]))
        print(sheets_data)
        #for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
        #    print('%s, %s' % (row[0], row[1]))

# writing data to a spreadsheets

    #    values = [
    #                [
    #                sheets_data
    #                ],
    # Additional rows ...
    #            ]
        body = {
            'values': sheets_data
               }
        result = service.spreadsheets().values().update(
        spreadsheetId='1MOCyQ1q9Xuz6EIkW9453xlcol-W_K0wb87Ua5FfBa9U', range='write!A1:B30',
        valueInputOption='RAW', body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))


# appending data to a spreadsheets

if __name__ == '__main__':
    main()
