% include header username = username, redirectUrl = 'home', currentUrl='orderSuccess'
  <div><h2><em>Thanks for your order, {{username}}!</em><h2> </div>
  <br/>

<p>
	We're working hard on your order!  Please print this order confirmation for your records.
</p> 

<div class="container">
	<div class="row">
		<div class="span6"> 
			<h3>Shipping address:</h3>
			{{firstName}} {{lastName}}<br>
			{{address1}}<br>
			% if len(address2) > 0:
				{{address2}}<br>
			% end
			{{city}}, {{state}} {{zip}}
			
			<h3>Payment method:</h3>
			{{payment}}
			
		</div>
		
		<div class="span4">
			<h3>Print:</h3>
			{{printInfo['properties']['name'][0]['value']}}: 
			${{printInfo['properties']['price'][0]['value']}}
			<img src="/static/images/{{printInfo['properties']['imgPath'][0]['value']}}" class="thumb">
	
		</div>
	</div>
</div>
 
% include footer