


##
##
## läuft noch nicht. aber keine fehlermeldung.
##
##
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_service(api_name, api_version, scopes, key_file_location):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)
    return service

def patch_profiles(service):
    try:
      service.management().profiles().patch(
        accountId='18536901',
        webPropertyId='UA-18536901-1',
        profileId='74816901',
        body={'eCommerceTracking': True,'enhancedECommerceTracking': True}).execute()
      print(service)
    except error:
    # Handle errors in constructing a query.
      print ('There was an error in constructing your query : %s',  error)
    except error:
     # Handle API errors.
      print ('There was an API error : %s : %s',  (error.resp.status, error.resp.reason))


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

#    profile_id = patch_profiles(service)

if __name__ == '__main__':
    main()
