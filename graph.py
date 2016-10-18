import requests
import json

graphID='lll3'

# TODO: connect this to graph instance on bluemix
api_url='https://ibmgraph-alpha.ng.bluemix.net/5a3f6509-cbb5-420d-afb9-b6ee93912fb9'
username='b40cdf16-7160-41b8-afaa-3e598f61e588'
password='62433f76-2d6d-489d-8d0b-408bb1c058a0'

# get the gds-token
response = requests.get(api_url + '/_session', 
                 auth=(username, password))
token = 'gds-token ' + json.loads(response.content)['gds-token']
print token

headers={'Authorization': token, 'Accept': 'application/json', 'Content-Type' : 'application/json'}

# if the graph is not already created, create it and create the schema and indexes
response = requests.get(api_url + '/' + graphID, headers=headers)
if response.status_code != 200:
    print 'creating the graph'
    response = requests.post(api_url + '/_graphs/' + graphID,
                         headers=headers)
    print response
    print response.content
    
    print 'creating the schema and indexes for the graph'
    schema = open('schema.json', 'rb').read()
    response = requests.post(api_url + '/' + graphID + '/schema',
                         data=schema,
                         headers=headers)
    print response
    print response.content
else:
    print 'else' + response.content

