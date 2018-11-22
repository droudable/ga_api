
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_service(api_name, api_version, scopes, key_file_location):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)
    return service

def get_dimensions(service):
    dimensions = service.management().customDimensions().list(accountId='18536901', webPropertyId='UA-18536901-1').execute()
    dimensions_result=[]
    for dimension in dimensions.get('items', []):
        dimensions_result.append((dimension.get('kind'), dimension.get('id'), dimension.get('accountId'), dimension.get('webPropertyId'), dimension.get('name'), dimension.get('index'), dimension.get('scope'), dimension.get('active'), dimension.get('created'), dimension.get('updated')))
    print('dimensions_result:', dimensions_result)

def main():
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'client_secrets2.json'
    # Authenticate and construct service.
    service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=['https://www.googleapis.com/auth/analytics.readonly'],
            key_file_location= key_file_location)
    dimensions2 = get_dimensions(service)

if __name__ == '__main__':
    main()
