import requests
import json

graphID='lll16'
schemaFileLocation='schema.json'

# TODO: connect this to graph instance on bluemix
api_url='https://ibmgraph-alpha.ng.bluemix.net/5a3f6509-cbb5-420d-afb9-b6ee93912fb9'
username='b40cdf16-7160-41b8-afaa-3e598f61e588'
password='62433f76-2d6d-489d-8d0b-408bb1c058a0'

# get the gds-token
response = requests.get(api_url + '/_session', 
                 auth=(username, password))
token = 'gds-token ' + json.loads(response.content)['gds-token']
print token

# TODO: check what happens when the token expires. what is our error code? create a way to get a new token automatically when this happens

# set the headers for all of our requests to use the token
headers={'Authorization': token, 'Accept': 'application/json', 'Content-Type' : 'application/json'}

# if the graph is not already created, create it and create the schema and indexes
response = requests.get(api_url + '/' + graphID, headers=headers)
if response.status_code == 200:
    print 'Graph with id %s already exists' % (graphID)
else:
    print 'Creating graph with id %s' % (graphID)
    response = requests.post(api_url + '/_graphs/' + graphID,
                         headers=headers)
    if (response.status_code == 201):
        print 'Graph with id %s successfully created'  % (graphID)
    else:
        raise ValueError('Graph with id %s not created successfully: %s. %s' %
                         (graphID, response.status_code, response.content))
    
    print 'Creating the schema and indexes for graph %s based on %s' % (graphID, schemaFileLocation)
    schema = open('schema.json', 'rb').read()
    response = requests.post(api_url + '/' + graphID + '/schema',
                         data=schema,
                         headers=headers)
    if (response.status_code == 200):
        print 'Schema and indexes for graph %s successfully created based on %s' % (graphID, schemaFileLocation)
    else:
        raise ValueError('Schema and indexes for graph %s not created successfully: %s. %s' %
                         (graphID, response.status_code, response.content))

def insertSampleData():    
    print 'Inserting sample data'
    
    createUser('Jason', 'Schaefer', 'jason', 'jason@example.com')
    createUser('Joy', 'Haywood', 'joy', 'joy@example.com')
    createUser('Deanna', 'Howling', 'deanna', 'deanna@example.com')
    createUser('Dale', 'Haywood', 'dale', 'dale@example.com')
    
    createPrint('Alaska', 'Lauren loves this photo even though she wasn\'t present ' + 
                'when the photo was taken. Her husband took this photo on a guy\'s weekend in Alaska.',
                75.00, 'alaska.jpg')
    createPrint('Antarctica', 'Lauren\'s husband took this spectacular photo when they visited ' +
                'Antarctica in December of 2012. This is one of our hot sellers, so it rarely goes on sale. ',
                100.00, 'penguin.jpg')
    createPrint('Australia', 'Lauren loved her trip to Australia so much that she named her daughter Sydney. ',
                120.00, 'sydney.jpg')
    createPrint('Las Vegas', 'What happens in Vegas, stays in Vegas...unless you take a picture.',
                90.00, 'vegas.jpg')
    createPrint('Japan', 'Lauren and her husband babymooned in gorgeous Japan.',
                95.00, 'japan.jpg')
    
    print 'Sample data successfully inserted'
    
def createUser(firstName, lastName, username, email):
    
    # check if a user with the given username already exists
    response = requests.get(api_url + '/' + graphID + '/vertices?label=user&username=' + username, 
                             headers=headers)
    if ((response.status_code == 200) and 
        ( len(json.loads(response.content)['result']['data']) > 0)):
            print 'User with username %s already exists. User will not be created.' % username
            return
    
    # if the user does not already exist, create the user
    print 'Creating new user'
    userJson = {}
    userJson['label'] = 'user'
    userJson['firstName'] = firstName
    userJson['lastName'] = lastName
    userJson['username'] = username
    userJson['email'] = email

    response = requests.post(api_url + '/' + graphID + '/vertices', 
                             data=json.dumps(userJson), headers=headers)
    if (response.status_code == 200):
        print 'User successfully created: %s' % (json.dumps(userJson))
    else:
        raise ValueError('User not created successfully: %s. %s. %s' %
                         (json.dumps(userJson), response.status_code, response.content))
        
def createPrint(name, description, price, imgPath):
    
    # check if a print with the given name already exists
    response = requests.get(api_url + '/' + graphID + '/vertices?label=print&name=' + name, 
                             headers=headers)
    if ((response.status_code == 200) and 
        ( len(json.loads(response.content)['result']['data']) > 0)):
            print 'Print with name %s already exists. Print will not be created.' % name
            return
        
    print 'Creating new print'
    printJson = {}
    printJson['label'] = 'print'
    printJson['name'] = name
    printJson['description'] = description
    printJson['price'] = price
    printJson['imgPath'] = imgPath

    response = requests.post(api_url + '/' + graphID + '/vertices', 
                             data=json.dumps(printJson), headers=headers)
    if (response.status_code == 200):
        print 'Print successfully created: %s' % (json.dumps(printJson))
    else:
        raise ValueError('Print not created successfully: %s. %s. %s' %
                         (json.dumps(printJson), response.status_code, response.content))
    