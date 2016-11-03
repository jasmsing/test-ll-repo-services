% include header username = username, redirectUrl = 'home', currentUrl = 'home'
    <div><h2 class="text-center"><em>Lauren's Lovely Landscapes</em><h2> </div>
  	<br/>
  	
 		<p>
		
			Lauren's Lovely Landscapes is a collection of some of her favorite landscapes.  
			If you would like to purchase a print, please <a href="mailto:lauren@example.com">
			e-mail Lauren</a> with the name	of the print.
			
		</p>
		
		<p>
			
			Please check back often to see if we have sales!
			
		</p>
		
		<div class='container'>
			<div class='row'>
			
				% if len(prints) == 0:
					Sorry!  No prints are currently available for sale.
				% end
		
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
