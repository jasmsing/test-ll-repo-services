% include header currentUrl='signin', redirectUrl=redirectUrl, username=None
<div><h2><em>Sign In</em><h2> </div>

% if defined('error'):
	<div class="alert alert-error">
		{{error}}
	</div>
% end

<form class="form-horizontal" action="/signin" method="POST">

	<p>
		You must be a registered user to purchase a print.  Please sign in below or <a href="/register?redirectUrl={{redirectUrl}}">register</a>.
	</p>
	
	<div class="control-group">
		<label for="username">Username:</label>
		<input class="form-control" name="username">
	</div>
	
	<input type="hidden" name="redirectUrl" value="{{redirectUrl}}">
	
	<button value="Sign In" type="submit" class="btn btn-default">Sign In</button>

</form>

% include footer