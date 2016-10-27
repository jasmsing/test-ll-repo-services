import requests
import json
import time
import datetime
import constants

schemaFileLocation='schema.json'

# get the gds-token
response = requests.get(constants.API_URL + '/_session', 
                 auth=(constants.USERNAME, constants.PASSWORD))
token = 'gds-token ' + json.loads(response.content)['gds-token']
print token

#TODO remove this
#print time.strftime("%Y-%m-%d %H:%M:%S")
#mytime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
#newtime = datetime.datetime.strptime(mytime, "%Y-%m-%d %H:%M:%S")
#print newtime
#print newtime.year

# TODO: check what happens when the token expires. what is our error code? create a way to get a new token automatically when this happens
# from the api reference:
# Once the token expires, you get a 401 error response when trying to use it. The token can also be invalidated when you unbind the credentials that are being used, which results in a 403 error response.

# set the headers for all of our requests to use the token
headers={'Authorization': token, 'Accept': 'application/json', 'Content-Type' : 'application/json'}

# if the graph is not already created, create it and create the schema and indexes
response = requests.get(constants.API_URL + '/' + constants.GRAPH_ID, headers=headers)
if response.status_code == 200:
    print 'Graph with id %s already exists' % (constants.GRAPH_ID)
else:
    print 'Creating graph with id %s' % (constants.GRAPH_ID)
    response = requests.post(constants.API_URL + '/_graphs/' + constants.GRAPH_ID,
                         headers=headers)
    if (response.status_code == 201):
        print 'Graph with id %s successfully created'  % (constants.GRAPH_ID)
    else:
        raise ValueError('Graph with id %s not created successfully: %s. %s' %
                         (constants.GRAPH_ID, response.status_code, response.content))
    
    print 'Creating the schema and indexes for graph %s based on %s' % (constants.GRAPH_ID, schemaFileLocation)
    schema = open(schemaFileLocation, 'rb').read()
    response = requests.post(constants.API_URL + '/' + constants.GRAPH_ID + '/schema',
                         data=schema,
                         headers=headers)
    if (response.status_code == 200):
        print 'Schema and indexes for graph %s successfully created based on %s' % (constants.GRAPH_ID, schemaFileLocation)
    else:
        raise ValueError('Schema and indexes for graph %s not created successfully: %s. %s' %
                         (constants.GRAPH_ID, response.status_code, response.content))

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
    
    buyPrint('jason', 'Alaska', "2016-10-15 13:13:17", '123 Sweet Lane', 'Apt #5', 'Valentine', 'NE', 69201, 'Paypass' )
    buyPrint('jason', 'Las Vegas', "2016-02-03 16:05:02", '123 Sweet Lane', 'Apt #5', 'Valentine', 'NE', 69201, 'Paypass' )
    buyPrint('jason', 'Australia', "2016-06-09 06:45:42", '529 Green St', '', 'Omaha', 'NE', 68104, 'Credit card' )
    buyPrint('joy', 'Alaska', "2015-12-24 04:34:52", '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('joy', 'Antarctica', "2015-12-29 16:25:02", '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('joy', 'Las Vegas', "2016-04-22 14:48:30", '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('joy', 'Japan', "2016-04-06 09:55:48", '423 Purple St', '', 'Honolulu', 'HI', 96818, 'Credit card' )
    buyPrint('deanna', 'Alaska', "2016-01-17 08:46:20", '2 Flamingo Lane', '', 'Chicago', 'IL', 60629, 'Credit card' )
    buyPrint('deanna', 'Antarctica', "2016-06-09 12:05:30", '529 Green St', '', 'Omaha', 'NE', 68104, 'Credit card' )
    buyPrint('deanna', 'Las Vegas', "2016-10-20 13:50:00", '2 Flamingo Lane', '', 'Chicago', 'IL', 60629, 'Paypass' )
    buyPrint('dale', 'Las Vegas', "2016-05-05 22:15:45", '25 Takeflight Ave', '', 'Houston', 'TX', 77036, 'Paypass' )
    buyPrint('dale', 'Australia', "2016-05-06 10:15:25", '25 Takeflight Ave', '', 'Houston', 'TX', 77036, 'Paypass' )
    buyPrint('dale', 'Las Vegas', "2016-05-06 10:18:30", '25 Takeflight Ave', '', 'Houston', 'TX', 77036, 'Paypass' )
    print 'Sample data successfully inserted'
    
def createUser(firstName, lastName, username, email):
    
    # check if a user with the given username already exists
    response = requests.get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=user&username=' + username, 
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

    response = requests.post(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices', 
                             data=json.dumps(userJson), headers=headers)
    if (response.status_code == 200):
        print 'User successfully created: %s' % (json.dumps(userJson))
    else:
        raise ValueError('User not created successfully: %s. %s. %s' %
                         (json.dumps(userJson), response.status_code, response.content))
        
def createPrint(name, description, price, imgPath):
    
    # check if a print with the given name already exists
    response = requests.get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=print&name=' + name, 
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

    response = requests.post(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices', 
                             data=json.dumps(printJson), headers=headers)
    if (response.status_code == 200):
        print 'Print successfully created: %s' % (json.dumps(printJson))
    else:
        raise ValueError('Print not created successfully: %s. %s. %s' %
                         (json.dumps(printJson), response.status_code, response.content))
        
def buyPrint(username, printName, date, address1, address2, city, state, zip, paymentMethod):

    # get the user vertex id
    response = requests.get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=user&username=' + username, 
                             headers=headers)
    if ((response.status_code == 200) and 
        ( len(json.loads(response.content)['result']['data']) > 0)):
            userVertexId = json.loads(response.content)['result']['data'][0]['id']
    else:
        raise ValueError('Could not find user with username %s. %s: %s' %
                         (username, response.status_code, response.content)) 
            
    # get the print vertex id
    response = requests.get(constants.API_URL + '/' + constants.GRAPH_ID + '/vertices?label=print&name=' + printName, 
                             headers=headers)
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
    buysJson['properties']['address1'] = address1
    buysJson['properties']['address2'] = address2
    buysJson['properties']['city'] = city
    buysJson['properties']['state'] = state
    buysJson['properties']['zip'] = zip
    buysJson['properties']['paymentMethod'] = paymentMethod

    response = requests.post(constants.API_URL + '/' + constants.GRAPH_ID + '/edges', data=json.dumps(buysJson), headers=headers)
    print json.dumps(buysJson)
    if (response.status_code == 200):
        print 'Print successfully bought: %s' % (json.dumps(buysJson))
    else:
        raise ValueError('Print not successfully bought: %s. %s: %s' %
                         (json.dumps(buysJson), response.status_code, response.content))
    