
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_service(api_name, api_version, scopes, key_file_location):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
            key_file_location, scopes=scopes)
    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)
    return service

def get_profiles(service):
    profiles_result=[]
    profiles = service.management().profiles().list(
    accountId='18536901',
    webPropertyId='UA-18536901-1').execute()
    for profile in profiles.get('items', []):
        profiles_result.append((profile.get('accountId'), profile.get('webPropertyId'), profile.get('internalWebPropertyId'), profile.get('id'), profile.get('name'), profile.get('defaultPage'), profile.get('excludeQueryParameters'), profile.get('siteSearchCategoryParameters'), profile.get('siteSearchQueryParameters'), profile.get('currency'), profile.get('timezone'), profile.get('created'), profile.get('updated'), profile.get('eCommerceTracking'), profile.get('enhancedECommerceTracking')))
    print('profiles_result:', profiles_result)

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
