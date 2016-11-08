% include header username = username, redirectUrl = 'print/' + printInfo['properties']['name'][0]['value'], currentUrl = 'print/' + printInfo['properties']['name'][0]['value'] 
  <div><h2><em>{{printInfo['properties']['name'][0]['value']}}</em><h2> </div>
  <br/>
  
		<img src="/static/images/{{printInfo['properties']['imgPath'][0]['value']}}" class="sale-photo">
	
		<h3>
			About this landscape:
		</h3>
	
		<div id="description">
			{{printInfo['properties']['description'][0]['value']}}
		</div>
		
		<h3>
			Price: 
		</h3>
		
		<div id="price">${{printInfo['properties']['price'][0]['value']}}</div>

		<p></p>
  		<form class="form-horizontal" action="/orderPrint/{{printInfo['properties']['name'][0]['value']}}" method="GET">
			
			<button value="Buy" type="submit" class="btn btn-default">Order Print</button>
		
		</form>

 
% include footer