import requests
import json
import time
import datetime
import constants

schemaFileLocation='schema.json'
headers=''

def post (url, data, headers):
    response = requests.post(url, data=data, headers=headers)
    if (response.status_code == 401):
        print 'Expired token. Requesting a new token...'
        getToken()
        response = requests.post(url, data=data, headers=headers)
    return response
    
def get (url, headers):
    response = requests.get(url, headers=headers)
    if (response.status_code == 401) or (response.status_code == 403):
        print 'Expired token. Requesting a new token...'
        getToken()
        response = requests.get(url, headers=headers)
    return response

def getAllPrints():
    print 'Getting the prints...'
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=print&type=print', 
                             headers)
    prints = {}
    if (response.status_code == 200):
        prints = json.loads(response.content)['result']['data']
        print 'Successfully got the prints'
    else:
        raise ValueError('An error occurred while getting the prints: %s. %s' %
                         (response.status_code, response.content))
    return prints

def insertSampleData():    
    print 'Inserting sample data...'
    
    try: 
        createUser('Jason', 'Schaefer', 'jason', 'jason@example.com')
    except ValueError as e:
        print e
    
    try:
        createUser('Joy', 'Haywood', 'joy', 'joy@example.com')
    except ValueError as e:
        print e
    
    try:
        createUser('Deanna', 'Howling', 'deanna', 'deanna@example.com')
    except ValueError as e:
        print e
    
    try:
        createUser('Dale', 'Haywood', 'dale', 'dale@example.com')
    except ValueError as e:
        print e
    
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
    createPrint('Israel', 'Lauren and her husband were able to tour Israel after Lauren spoke at IBM Business Connect in Tel Aviv in 2014.',
                80.00, 'israel.jpg')
    createPrint('Kenya', 'Jason and Lauren went on safari in Kenya after Lauren spent 4 weeks working in Nairobi as part of the IBM Corporate Service Corps.',
                120.00, 'kenya.jpg')
    
    buyPrint('jason', 'Alaska', "2016-10-15 13:13:17", 'Jason', 'Schaefer', '123 Sweet Lane', 'Apt #5', 'Valentine', 'NE', 69201, 'Paypass' )
    buyPrint('jason', 'Las Vegas', "2016-02-03 16:05:02", 'Jason', 'Schaefer', '123 Sweet Lane', 'Apt #5', 'Valentine', 'NE', 69201, 'Paypass' )
    buyPrint('jason', 'Australia', "2016-06-09 06:45:42", 'Chuck', 'Howling', '529 Green St', '', 'Omaha', 'NE', 68104, 'Credit card' )
    buyPrint('joy', 'Alaska', "2015-12-24 04:34:52", 'Joy', 'Haywood', '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('joy', 'Antarctica', "2015-12-29 16:25:02", 'Joy', 'Haywood', '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('joy', 'Las Vegas', "2016-04-22 14:48:30", 'Joy', 'Haywood', '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('joy', 'Japan', "2016-04-06 09:55:48", 'Joy', 'Haywood', '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('deanna', 'Alaska', "2016-01-17 08:46:20", 'Deanna', 'Howling', '2 Flamingo Lane', '', 'Chicago', 'IL', 60629, 'Credit card' )
    buyPrint('deanna', 'Antarctica', "2016-06-09 12:05:30", 'Chuck', 'Howling', '529 Green St', '', 'Omaha', 'NE', 68104, 'Credit card' )
    buyPrint('deanna', 'Las Vegas', "2016-10-20 13:50:00", 'Deanna', 'Howling', '2 Flamingo Lane', '', 'Chicago', 'IL', 60629, 'Paypass' )
    buyPrint('dale', 'Las Vegas', "2016-05-05 22:15:45", 'Dale', 'Haywood', '25 Takeflight Ave', '', 'Houston', 'TX', 77036, 'Paypass' )
    buyPrint('dale', 'Australia', "2016-05-06 10:15:25", 'Dale', 'Haywood', '25 Takeflight Ave', '', 'Houston', 'TX', 77036, 'Paypass' )
    buyPrint('dale', 'Las Vegas', "2016-05-06 10:18:30", 'Dale', 'Haywood', '25 Takeflight Ave', '', 'Houston', 'TX', 77036, 'Paypass' )
    print 'Sample data successfully inserted'

def getUser(username):    
    print 'Getting user with username %s from the graph' % username
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=user&username=' + username, 
                             headers)
    if len(json.loads(response.content)['result']['data']) > 0 :
        return username
    return None

def getAllUsers():
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?type=user', 
                             headers)
    if len(json.loads(response.content)['result']['data']) > 0 :
        return json.loads(response.content)['result']['data']
    return {}
    
def createUser(firstName, lastName, username, email):
    
    # check if a user with the given username already exists
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=user&username=' + username, 
                             headers)
    if ((response.status_code == 200) and 
        ( len(json.loads(response.content)['result']['data']) > 0)):
            raise ValueError('The username \'%s\' is already taken. Get creative and try again.' % username)
            return
    
    # if the user does not already exist, create the user
    print 'Creating new user'
    userJson = {}
    userJson['label'] = 'user'
    userJson['firstName'] = firstName
    userJson['lastName'] = lastName
    userJson['username'] = username
    userJson['email'] = email
    userJson['type'] = 'user'

    response = post(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices', 
                             json.dumps(userJson), headers)
    if (response.status_code == 200):
        print 'User successfully created: %s' % (json.dumps(userJson))
    else:
        raise ValueError('User not created successfully: %s. %s. %s' %
                         (json.dumps(userJson), response.status_code, response.content))
        
def getPrintInfo(name):
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=print&name=' + name, 
                             headers)
    
    if (response.status_code == 200):  
        results = json.loads(response.content)['result']['data'] 
        if len(results) > 0:
            printInfo = results[0]
            print 'Found print with name %s.' % name
            return printInfo

    raise ValueError('Unable to find user with name %s' % name)

def createPrint(name, description, price, imgPath):
    
    # check if a print with the given name already exists
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=print&name=' + name, 
                             headers)
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
    printJson['type'] = 'print'

    response = post(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices', 
                             json.dumps(printJson), headers)
    if (response.status_code == 200):
        print 'Print successfully created: %s' % (json.dumps(printJson))
    else:
        raise ValueError('Print not created successfully: %s. %s. %s' %
                         (json.dumps(printJson), response.status_code, response.content))
        
def buyPrint(username, printName, date, firstName, lastName, address1, address2, city, state, zip, paymentMethod):

    # get the user vertex id
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=user&username=' + username, 
                             headers)
    if ((response.status_code == 200) and 
        ( len(json.loads(response.content)['result']['data']) > 0)):
            userVertexId = json.loads(response.content)['result']['data'][0]['id']
    else:
        raise ValueError('Could not find user with username %s. %s: %s' %
                         (username, response.status_code, response.content)) 
            
    # get the print vertex id
    response = get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=print&name=' + printName, 
                             headers)
    if ((response.status_code == 200) and 
        ( len(json.loads(response.content)['result']['data']) > 0)):
            printVertexId = json.loads(response.content)['result']['data'][0]['id']
    else:
        raise ValueError('Could not find print with name %s. %s: %s' %
                         (printName, response.status_code, response.content))
            
    # create the "buys" edge between the user and print
    buysJson = {}
    buysJson['label'] = 'buys'
    buysJson['outV'] = userVertexId
    buysJson['inV'] = printVertexId
    buysJson['properties'] = {}
    buysJson['properties']['date'] = date
    buysJson['properties']['firstName'] = firstName
    buysJson['properties']['lastName'] = lastName
    buysJson['properties']['address1'] = address1
    buysJson['properties']['address2'] = address2
    buysJson['properties']['city'] = city
    buysJson['properties']['state'] = state
    buysJson['properties']['zip'] = zip
    buysJson['properties']['paymentMethod'] = paymentMethod
    buysJson['type'] = 'buys'

    response = post(constants.API_URL + '/' + constants.GRAPH_ID + '/edges', json.dumps(buysJson), headers)
    print json.dumps(buysJson)
    if (response.status_code == 200):
        print 'Print successfully bought: %s' % (json.dumps(buysJson))
    else:
        raise ValueError('Print not successfully bought: %s. %s: %s' %
                         (json.dumps(buysJson), response.status_code, response.content))
        
def getToken():
    # get the gds-token
    response = requests.get(constants.API_URL + '/_session', 
                     auth=(constants.USERNAME, constants.PASSWORD))
    token = 'gds-token ' + json.loads(response.content)['gds-token']
    print token
    
    # set the headers for all of our requests to use the token
    global headers
    headers={'Authorization': token, 'Accept': 'application/json', 'Content-Type' : 'application/json'}

def initializeGraph():
    getToken()

    # if the graph is not already created, create it and create the schema and indexes
    print 'Checking to see if graph with id %s exists...' % (constants.GRAPH_ID)
    response = get(constants.API_URL + '/' + constants.GRAPH_ID, headers)
    if response.status_code == 200:
        print 'Graph with id %s already exists' % (constants.GRAPH_ID)
    else:
        print 'Creating graph with id %s' % (constants.GRAPH_ID)
        response = post(constants.API_URL + '/_graphs/' + constants.GRAPH_ID, '', headers)
        if (response.status_code == 201):
            print 'Graph with id %s successfully created'  % (constants.GRAPH_ID)
        else:
            raise ValueError('Graph with id %s not created successfully: %s. %s' %
                             (constants.GRAPH_ID, response.status_code, response.content))
        
        print 'Creating the schema and indexes for graph %s based on %s. This may take a minute or two...' % (constants.GRAPH_ID, schemaFileLocation)
        schema = open(schemaFileLocation, 'rb').read()
        response = post(constants.API_URL + '/' + constants.GRAPH_ID + '/schema',
                             schema,
                             headers)
        if (response.status_code == 200):
            print 'Schema and indexes for graph %s successfully created based on %s' % (constants.GRAPH_ID, schemaFileLocation)
        else:
            raise ValueError('Schema and indexes for graph %s not created successfully: %s. %s' %
                             (constants.GRAPH_ID, response.status_code, response.content))

# Deletes 'Buys' edges, 'User' vertexes, and 'Print' vertexes
# Does not delete the graph itself            
def dropGraph():
    data = {
        "gremlin":  "def g = graph.traversal();" + 
                    "g.E().has('type', 'buys').drop().count();" + 
                    "g.V().has('type', within('print','user')).drop();" 
        }
    response = post(constants.API_URL + '/' + constants.GRAPH_ID + '/gremlin' , json.dumps(data), headers)
    if response.status_code == 200:
        print 'Successfully deleted Buys edges, Print vertexes, and User vertexes'
    else:
        raise ValueError('An error occurred while deleting the vertexes and/or edges for the graph %s: %s. %s'%
                             (constants.GRAPH_ID, response.status_code, response.content))