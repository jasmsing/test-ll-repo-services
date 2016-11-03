"""
/*-------------------------------------------------------------------*/
/*                                                                   */
/* Copyright IBM Corp. 2016 All Rights Reserved                      */
/*                                                                   */
/*-------------------------------------------------------------------*/
/*                                                                   */
/*        NOTICE TO USERS OF THE SOURCE CODE EXAMPLES                */
/*                                                                   */
/* The source code examples provided by IBM are only intended to     */
/* assist in the development of a working software program.          */
/*                                                                   */
/* International Business Machines Corporation provides the source   */
/* code examples, both individually and as one or more groups,       */
/* "as is" without warranty of any kind, either expressed or         */
/* implied, including, but not limited to the warranty of            */
/* non-infringement and the implied warranties of merchantability    */
/* and fitness for a particular purpose. The entire risk             */
/* as to the quality and performance of the source code              */
/* examples, both individually and as one or more groups, is with    */
/* you. Should any part of the source code examples prove defective, */
/* you (and not IBM or an authorized dealer) assume the entire cost  */
/* of all necessary servicing, repair or correction.                 */
/*                                                                   */
/* IBM does not warrant that the contents of the source code         */
/* examples, whether individually or as one or more groups, will     */
/* meet your requirements or that the source code examples are       */
/* error-free.                                                       */
/*                                                                   */
/* IBM may make improvements and/or changes in the source code       */
/* examples at any time.                                             */
/*                                                                   */
/* Changes may be made periodically to the information in the        */
/* source code examples; these changes may be reported, for the      */
/* sample code included herein, in new editions of the examples.     */
/*                                                                   */
/* References in the source code examples to IBM products, programs, */
/* or services do not imply that IBM intends to make these           */
/* available in all countries in which IBM operates. Any reference   */
/* to the IBM licensed program in the source code examples is not    */
/* intended to state or imply that IBM's licensed program must be    */
/* used. Any functionally equivalent program may be used.            */
/*-------------------------------------------------------------------*/
"""

import bottle
from bottle import *
import os,sys,logging, traceback, json, string, urllib, urllib2
import graph
import constants
import urlparse

graph.initializeGraph()

#Provide all the static css and js files under the static dir to browser
@route('/static/:filename#.*#')
def server_static(filename):
	""" This is for JS files """
	return static_file(filename, root='static')

# Displays the home page
@bottle.get("/")
@bottle.get("/home")
def getHome():
	return bottle.template('home', 
						username = request.get_cookie("account", secret=constants.COOKIE_KEY), 
						prints = graph.getAllPrints())

# Displays the page for the designated print
@bottle.get("/print/<printName>")
def getPrint(printName):
	try:
		printInfo = graph.getPrintInfo(printName)
		return bottle.template('print',
						username = request.get_cookie("account", secret=constants.COOKIE_KEY),
						printInfo = printInfo)
	except ValueError:
		return bottle.template('simpleMessage',
							username = request.get_cookie("account", secret=constants.COOKIE_KEY),
							title='Oops!',
							message='We can\'t find that print. Sorry!')	

# Displays the registration page
@bottle.get("/register")
def getRegistration():
	return bottle.template('register')

@bottle.post('/register')
def registerUser():
	firstName = request.forms.get('firstName')
	lastName = request.forms.get("lastName")
	email = request.forms.get("email")
	username = request.forms.get("username")
	
	try:
		# create the user in the graph
		graph.createUser(firstName, lastName, username, email)
		# authenticate the user
		response.set_cookie("account", username, secret=constants.COOKIE_KEY)
		
		return bottle.template('simpleMessage',
							username = username,
							title='Success!',
							message='You\'re successfully registered. Now go buy something!')
	except ValueError as e:
		return bottle.template('register', 
							error=e,
							firstName=firstName,
							lastName=lastName,
							email=email)

# Displays the Sign In page
@bottle.get("/signin")
def getSignin():
    try:
        redirectUrl = urlparse.parse_qs(urlparse.urlparse(request.url).query)['redirectUrl'][0]
    except:
        redirectUrl = 'home'
    return bottle.template('signin', redirectUrl=redirectUrl)    

# Displays the Sign In page
@bottle.post('/signin')
def signIn():
	username = request.forms.get("username")
	# for simplicity, not dealing with passwords
	# if the username exists in the graph, we will authenticate the user
	username = graph.getUser(username)
	if username is not None:
		print 'Authenticating user %s' % username
		response.set_cookie("account", username, secret=constants.COOKIE_KEY)
		redirect(request.forms.get("redirectUrl"))
	else:
		print 'Unable to authenticate user %s' % username
		return bottle.template('signin', 
							error='Unable to find an account with the given username. Please try again.',
							currentUrl = request.forms.get("redirectUrl"))

@bottle.get('/signout')
def signOut():
	print 'Signing out user'
	response.delete_cookie("account")
	redirect(urlparse.parse_qs(urlparse.urlparse(request.url).query)['redirectUrl'][0])
		
# Inserts the sample data
@bottle.get("/insertSampleData")
def insertSampleData():
	try:	
		graph.insertSampleData()
		return bottle.template('simpleMessage', 
							username = request.get_cookie("account", secret=constants.COOKIE_KEY),
							title='Sample Data Created', 
							message='Woo hoo!  The sample data was created!')
	except ValueError as e:
		print e
		return bottle.template('simpleMessage', 
							username = request.get_cookie("account", secret=constants.COOKIE_KEY),
							title='Oops!  Something went wrong!', 
							message=e)

# Error Methods
@bottle.error(404)
def error404(error):
    print '404'
    return bottle.template('simpleMessage', 
						username = request.get_cookie("account", secret=constants.COOKIE_KEY),
						title='404', 
						message='We can\'t find that page.  Sorry!')


application = bottle.default_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', '8000'))
    bottle.run(host='0.0.0.0', port=port)
