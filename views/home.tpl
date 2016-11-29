% include header username = username, redirectUrl = 'home', currentUrl = 'home'
    <div><h2 class="text-center"><em>Lauren's Lovely Landscapes</em><h2> </div>
  	<br/>
  	
 		<p>
		
			Lauren's Lovely Landscapes is a collection of some of her favorite landscapes.  
			The site has recently been updated to allow you to purchase prints online.
			
		</p>
		
		<p>
			
			Please check back often to see if we have sales!!!
			
		</p>
		
		% if len(prints) == 0:
			<p>
				Sorry!  No prints are currently available for sale.
			</p>
		% end
		
		<div class='container'>
			<div class='row'>
		
				% for p in prints:				
					<div class="preview span3">
						<a href="print/{{p['properties']['name'][0]['value']}}">
							{{p['properties']['name'][0]['value']}}<br>
							<img src="/static/images/{{p['properties']['imgPath'][0]['value']}}" class="thumb">
						</a>
					</div>
				% end
			
			</div>
		</div> 

% include footer
