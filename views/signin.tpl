% redirectUrl = currentUrl
% include header currentUrl='signin'
<div><h2><em>Sign In</em><h2> </div>

% if defined('error'):
	<div class="alert alert-error">
		{{error}}
	</div>
% end

<form class="form-horizontal" action="/signin" method="POST">
	
	<div class="control-group">
		<label for="username">Username:</label>
		<input class="form-control" name="username">
	</div>
	
	<input type="hidden" name="redirectUrl" value="{{redirectUrl}}">
	
	<button value="Sign In" type="submit" class="btn btn-default">Sign In</button>

</form>

% include footer