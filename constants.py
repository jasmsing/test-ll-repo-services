import os
import json


# A string that is unique in your IBM Graph instance
GRAPH_ID = 'landscapes_graph'

# If you are running the app locally and using an IBM Graph instance
#   - navigate to your Graph instance on Bluemix
#   - click Service Credentials
#   - expand the credentials so you can view them
#   - paste the values below.
# Note: these values will be overwritten if the app is able find the
#   VCAP_SERVICES because you are deploying through Bluemix
API_URL=''
USERNAME=''
PASSWORD=''

# Get the VCAP_SERVICES from Bluemix
vcap_config = os.environ.get('VCAP_SERVICES')
if (vcap_config):
    decoded_config = json.loads(vcap_config)
    for key, value in decoded_config.iteritems():
        if key.startswith('IBM Graph'):
            graph_creds = decoded_config[key][0]['credentials']
            API_URL = graph_creds['apiURL'][:-2] #remove /g from the end of the url
            USERNAME = graph_creds['username']
            PASSWORD = graph_creds['password']
    
else:
    print 'Unable to access VCAP_SERVICES. Will use service credentials set manually in constants.py'