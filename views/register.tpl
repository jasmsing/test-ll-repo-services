%# todo: think through redirects for the register page
% include header redirectUrl='home'
<div><h2><em>Register</em><h2> </div>

% if defined('error'):
	<div class="alert alert-error">
		{{error}}
	</div>
% end

<form class="form-horizontal" action="/register" method="POST">

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
		<label for="email">Email address:</label>
		<input class="form-control" name="email"
			% if defined('email'):
					value="{{email}}"
				% end
		>
	</div>
	
	<div class="control-group">
		<label for="username">Username:</label>
		<input class="form-control" name="username">
	</div>
	
	<button value="Register" type="submit" class="btn btn-default">Submit</button>

</form>

% include footer