% include header redirectUrl='home', currentUrl='orderForm', username=username
<div><h2><em>Order Print</em><h2> </div>

% #TODO: Add some form validation
% #TODO: should only send clean error messages to user
% if defined('error'):
	<div class="alert alert-error">
		{{error}}
	</div>
% end

<div class="container">
<div class="row">
	<div class="span6">
		<form class="form-horizontal" action="/orderPrint" method="POST">
		
			<div class="control-group">
				<label for="firstName">First name:</label>
				<input class="form-control" name="firstName"
					% if defined('firstName'):
						value="{{firstName}}"
					% end
				>
			</div>
				
			<div class="control-group">
				<label for="lastName">Last name:</label>
					<input class="form-control" name="lastName"
						% if defined('lastName'):
								value="{{lastName}}"
							% end
					>
			</div>
			
			<div class="control-group">
				<label for="address1">Address:</label>
				<input class="form-control" name="address1"
					% if defined('address1'):
						value="{{address1}}"
					% end
				>
			</div>
			
			<div class="control-group">
				<label for="address2">Address line two:</label>
				<input class="form-control" name="address2"
					% if defined('address2'):
						value="{{address2}}"
					% end
				>
			</div>
			
			<div class="control-group">
				<label for="city">City:</label>
				<input class="form-control" name="city"
					% if defined('city'):
						value="{{city}}"
					% end
				>
			</div>
			
			<div class="control-group">
				<label for="state">State:</label>
				<select class="form-control" name="state">
					% if not defined('state'):				
					%	state=None
					% end
				
					<option value="AL" 
						% if state=="AL":
							selected
						% end
					>	Alabama</option>
					<option value="AK"
						% if state=="AK":
							selected
						% end
					> Alaska</option>
					<option value="AZ"
						% if state=="AZ":
							selected
						% end
					>	Arizona</option>
					<option value="AR"
						% if state=="AR":
							selected
						% end
					>	Arkansas</option>
					<option value="CA"
						% if state=="CA":
							selected
						% end
					>	California</option>
					<option value="CO"
						% if state=="CO":
							selected
						% end
					>	Colorado</option>
					<option value="CT"
						% if state=="CT":
							selected
						% end
					>	Connecticut</option>
					<option value="DE"
						% if state=="DE":
							selected
						% end
					>	Delaware</option>
					<option value="FL"
						% if state=="FL":
							selected
						% end
					>	Florida</option>
					<option value="GA"
						% if state=="GA":
							selected
						% end
					>	Georgia</option>
					<option value="HI"
						% if state=="HI":
							selected
						% end
					>	Hawaii</option>
					<option value="ID"
						% if state=="ID":
							selected
						% end
					>	Idaho</option>
					<option value="IL"
						% if state=="IL":
							selected
						% end
					>	Illinois</option>
					<option value="IN"
						% if state=="IN":
							selected
						% end
					>	Indiana</option>
					<option value="IA"
						% if state=="IA":
							selected
						% end
					>	Iowa</option>
					<option value="KS"
						% if state=="KS":
							selected
						% end
					>	Kansas</option>
					<option value="KY"
						% if state=="KY":
							selected
						% end
					>	Kentucky</option>
					<option value="LA"
						% if state=="LA":
							selected
						% end
					>	Louisiana</option>
					<option value="ME"
						% if state=="ME":
							selected
						% end
					>	Maine</option>
					<option value="MD"
						% if state=="MD":
							selected
						% end
					>	Maryland</option>
					<option value="MA"
						% if state=="MA":
							selected
						% end
					>	Massachusetts</option>
					<option value="MI"
						% if state=="MI":
							selected
						% end
					>	Michigan</option>
					<option value="MN"
						% if state=="MN":
							selected
						% end
					>	Minnesota</option>
					<option value="MS"
						% if state=="MS":
							selected
						% end
					>	Mississippi</option>
					<option value="MO"
						% if state=="MO":
							selected
						% end
					>	Missouri</option>
					<option value="MT"
						% if state=="MT":
							selected
						% end
					>	Montana</option>
					<option value="NE"
						% if state=="NE":
							selected
						% end
					>	Nebraska</option>
					<option value="NV"
						% if state=="NV":
							selected
						% end
					>	Nevada</option>
					<option value="NH"
						% if state=="NH":
							selected
						% end
					>	New Hampshire</option>
					<option value="NJ"
						% if state=="NJ":
							selected
						% end
					>	New Jersey</option>
					<option value="NM"
						% if state=="NM":
							selected
						% end
					>	New Mexico</option>
					<option value="NY"
						% if state=="NY":
							selected
						% end
					>	New York</option>
					<option value="NC"
						% if state=="NC":
							selected
						% end
					>	North Carolina</option>
					<option value="ND"
						% if state=="ND":
							selected
						% end
					>	North Dakota</option>
					<option value="OH"
						% if state=="OH":
							selected
						% end
					>	Ohio</option>
					<option value="OK"
						% if state=="OK":
							selected
						% end
					>	Oklahoma</option>
					<option value="OR"
						% if state=="OR":
							selected
						% end
					>	Oregon</option>
					<option value="PA"
						% if state=="PA":
							selected
						% end
					>	Pennsylvania</option>
					<option value="RI"
						% if state=="RI":
							selected
						% end
					>	Rhode Island</option>
					<option value="SC"
						% if state=="SC":
							selected
						% end
					>	South Carolina</option>
					<option value="SD"
						% if state=="SD":
							selected
						% end
					>	South Dakota</option>
					<option value="TN"
						% if state=="TN":
							selected
						% end
					>	Tennessee</option>
					<option value="TX"
						% if state=="TX":
							selected
						% end
					>	Texas</option>
					<option value="UT"
						% if state=="UT":
							selected
						% end
					>	Utah</option>
					<option value="VT"
						% if state=="VT":
							selected
						% end
					>	Vermont</option>
					<option value="VA"
						% if state=="VA":
							selected
						% end
					>	Virginia</option>
					<option value="WA"
						% if state=="WA":
							selected
						% end
					>	Washington</option>
					<option value="WV"
						% if state=="WV":
							selected
						% end
					>	West Virginia</option>
					<option value="WI"
						% if state=="WI":
							selected
						% end
					>	Wisconsin</option>
					<option value="WY"
						% if state=="WY":
							selected
						% end
					>	Wyoming</option>
					
				</select>
			</div>
		
			<div class="control-group">
				<label for="zip">Zip:</label>
				<input class="form-control" name="zip"
					% if defined('zip'):
						value="{{zip}}"
					% end
				>
			</div>
			
			<div class="control-group">
				<label for="payment">Payment method:</label>
				<input class="form-control" name="payment"
					% if defined('payment'):
							value="{{payment}}"
						% end
				>
			</div>
			
			<input type="hidden" name="print" value="{{printInfo['properties']['name'][0]['value']}}">
			
			<button value="placeOrder" type="submit" class="btn btn-default">Place Order</button>
		
		</form>
	</div>
	
	<div class="span4">
		{{printInfo['properties']['name'][0]['value']}}: 
		${{printInfo['properties']['price'][0]['value']}}
		<img src="/static/images/{{printInfo['properties']['imgPath'][0]['value']}}" class="thumb">
	
	</div>
</div>
</div>

% include footer