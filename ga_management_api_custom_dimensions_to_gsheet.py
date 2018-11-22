
from __future__ import print_function
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def get_service_ga(api_name, api_version, scopes, key_file_location):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    # Build the service object.
    service_ga = build(api_name, api_version, credentials=credentials)
    return service_ga

def get_service_sheets(api_name, api_version, credentials):
    store = file.Storage('token.json')
    sheet = service.spreadsheets()
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secrets.json', 'https://www.googleapis.com/auth/drive')
        creds = tools.run_flow(flow, store)
        service_sheets = build('sheets', 'v4', http=creds.authorize(Http()))
        return service_sheets

def get_dimensions(service_ga):
    dimensions_result=[]
    dimensions = service.management().customDimensions().list(accountId='18536901', webPropertyId='UA-18536901-1').execute()
    for dimension in dimensions.get('items', []):
        dimensions_result.append((dimension.get('kind'), dimension.get('id'), dimension.get('accountId'), dimension.get('webPropertyId'), dimension.get('name'), dimension.get('index'), dimension.get('scope'), dimension.get('active'), dimension.get('created'), dimension.get('updated')))
    print('dimensions_result:', dimensions_result)
#-------------------------------
#-------------------------------
def write_data(service_sheets):
    values = dimensions_result
    print ('values_=', values)
    body = {'values': 0}
    result = service.spreadsheets().values().update(
    spreadsheetId='1MOCyQ1q9Xuz6EIkW9453xlcol-W_K0wb87Ua5FfBa9U', range='write!A1:B30',
    valueInputOption='RAW', body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))

def main():
    # Define the auth scopes to request.
    scope_ga = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'client_secrets2.json'

    # Authenticate and construct service.
    service_ga = get_service_ga(
            api_name='analytics',
            api_version='v3',
            scopes=['https://www.googleapis.com/auth/analytics.readonly'],
            key_file_location= key_file_location
            )
    service_sheets = get_service_sheets(
            api_name='analytics',
            api_version='v3',
            credentials= 'http=creds.authorize(Http())')
    dimensions2 = get_dimensions(service_ga)
    dimensions3 = write_data(service_sheets)


if __name__ == '__main__':
    main()
