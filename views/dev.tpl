% include header username = username, redirectUrl='home', currentUrl='simpleMessage'

  <div><h2><em>Hello, developers!</em><h2> </div>
  
  <p>
	  This is version 2 of Lauren's Lovely Landscapes.  Version 1 is a static sample 
	  app that demonstrates how easy it is to deploy an app using IBM Bluemix. Version 2 
	  expands Lauren's Lovely Landscapes to dynamically display prints as well as allow users 
	  to register, sign in, sign out, and buy prints. 
  </p>
  
  <p>
  	Version 1 is hosted at <a href="http://laurenslovelylandscapes.mybluemix.net">
  	http://laurenslovelylandscapes.mybluemix.net</a>.  The tutorial associated with 
  	Version 1 is posted at <a href="https://www.ibm.com/developerworks/cloud/library/cl-intro1-app">
  	https://www.ibm.com/developerworks/cloud/library/cl-intro1-app</a>.
  </p>
  
  <p>
  	The rest of the information on this page pertains to Version 2.
  </p>
  
  <h3>No prints listed on the home page?</h3>
  <a href="insertSampleData">Insert the sample data</a>.
  
  <h3>Like videos?</h3>
  Me too!  Get the inside scoop on how I developed the app in my <a href="https://developer.ibm.com/clouddataservices/docs/graph/how-to/e2e-use-case/">video series</a>.

  <h3>Want the code?</h3>
  I thought you might.  Get a copy of my code <a href="https://hub.jazz.net/project/lhayward/Laurens%20Lovely%20Landscapes%20%28IBM%20Graph%29/overview">here</a>.		

  </div> <!-- end of the hero-unit-->
  </div> <!-- end of the container-->
  
<div class="container">
<div class="hero-unit">
  
  <div><h2><em>The Data</em><h2> </div>
  
  <h3>Insert sample data</h3>
  Click <a href="insertSampleData">here</a> to insert the sample data.  Note that it may take a minute or two.
  
  <h3>Delete the data</h3>
  To start over with a fresh graph, click <a href="deleteData">here</a> to delete the data.
  
  <h3>Users</h3>
  <table class="table">
  	<thead>
  		<tr>
	  		<th>
	  			Username
	  		</th>
	  		<th>
	  			First Name
	  		</th>
	  		<th>
	  			Last Name
	  		</th>
	  		<th>
	  			Email
	  		</th>
  		</tr>
  	</thead>
  	<tbody>
  	% for user in users:
  		<tr>
  			<td>
  				{{user['properties']['username'][0]['value']}}
  			</td>
  			<td>
  				{{user['properties']['firstName'][0]['value']}}
  			</td>
  			<td>
  				{{user['properties']['lastName'][0]['value']}}
  			</td>
  			<td>
  				{{user['properties']['email'][0]['value']}}
  			</td>
  		</tr>
  	% end
  	</tbody>
  </table>

% include footer