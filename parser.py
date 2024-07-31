
#use glob for Unix style pathname pattern expansion
import glob

#import json for json files
import json

#import pathlib to remove the .json file extension
from pathlib import Path

def process_domain(jsonfilename):
    # Open JSON file
    #print(jsonfilename)
    f = open(jsonfilename,)

    # Convert JSON object to a dictionary
    try:
        fulljson = json.load(f)
    except:
        #print("Error loading JSON file")
        return

    # Iterating through the json
    if not 'privacy_sandbox_api_attestations' in fulljson:
        return
    
    for attestations in fulljson['privacy_sandbox_api_attestations']:
        if 'enrollment_site' in attestations:
            site = attestations['enrollment_site']
        else:
            site = ""

        api=attestations['platform_attestations'][0]['attestations']

        if 'topics_api' in api:
            topics = 'Topics'
        else: 
            topics = ""

        if 'protected_audience_api' in api:
            protected = 'Protected-Audience'
        else:
            protected = ""

        if 'attribution_reporting_api' in api:
            reporting = 'Attribution-Reporting'
        else:
            reporting = ""
        
        if 'shared_storage_api' in api:
            storage = 'Shared-Storage'
        else:
            storage = ""
        
        if 'private_aggregation_api' in api:
            aggregation = 'Private-Aggregation'
        else:
            aggregation = ""

        try:
            api_android=attestations['platform_attestations'][1]['attestations']
        except:
            api_android = []

        if 'topics_api' in api_android:
            topics2 = 'Topics'
        else: 
            topics2 = ""

        if 'protected_audience_api' in api_android:
            protected2 = 'Protected-Audience'
        else:
            protected2 = ""

        if 'attribution_reporting_api' in api_android:
            reporting2 = 'Attribution-Reporting'
        else:
            reporting2 = ""
        
        if 'shared_storage_api' in api_android:
            storage2 = 'Shared-Storage'
        else:
            storage2 = ""    
        
        if 'private_aggregation_api' in api_android:
            aggregation2 = 'Private-Aggregation'
        else:
            aggregation2 = ""


        #print(attestations['platform_attestations'][0]['platform'], ',', attestations['attestation_parser_version'], ',', attestations['attestation_version'], ',', attestations['enrollment_id'], ',', site,',' , reporting, ',', storage, ',', aggregation, ',', topics, ',', protected, ',', attestations['platform_attestations'][1]['platform'], ',', attestations['attestation_parser_version'], ',', attestations['attestation_version'], ',', attestations['enrollment_id'], ',', site, ',', reporting2, ',', storage2, ',', aggregation2, ',', topics2, ',', protected2)
        print(attestations['enrollment_id'], ',',reporting2, storage2, aggregation2, topics2, protected2 ,',', reporting, storage, aggregation, topics, protected, ',', site)

    # Close the file
    f.close()

#header 
print('Enrollment Id, Android APIs, Chrome APIs, Site')

for filename in glob.glob("*.json"):
    # do something with the file
    process_domain(filename)
