
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_service(api_name, api_version, scopes, key_file_location):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)
    return service

def get_profiles(service):
   ga_account='18536901'
  # filters = service.management().filters().get(accountId='18536901').execute()
# The results of the list method are stored in the filters object.
   filters = service.management().filters().list(
      accountId=ga_account
   ).execute()
# The following code shows how to iterate through them.
   filter_results = []
   for filter in filters.get('items', []):
       filter_results.append((filter.get('accountId'), filter.get('id'), filter.get('kind'), filter.get('type'), filter.get('name'), filter.get('created'), filter.get('updated')))
   print('filter_results:', filter_results)
    #print('profiles_result:', profiles_result)
    #print ('Account Id = %s' % filter.get('accountId'))
    #print ('Filter Id = %s' % filter.get('id'))
    #print ('Filter Kind = %s' % filter.get('kind'))
    #print ('Filter Name = %s' % filter.get('name'))
    #print ('Filter Created = %s' % filter.get('created'))
    #print ('Filter Updated = %s' % filter.get('updated'))




def main():
    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/analytics.readonly'
    key_file_location = 'c:\ga_api\client_secrets2.json'

    # Authenticate and construct service.
    service = get_service(
            api_name='analytics',
            api_version='v3',
            scopes=['https://www.googleapis.com/auth/analytics.readonly'],
            key_file_location= key_file_location)

    profile_id = get_profiles(service)

if __name__ == '__main__':
    main()
