<!DOCTYPE html>
<html>
<head>
	<title> Lauren's Lovely Landscapes </title>
	<meta charset="utf8">  
  	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
   <link href="/static/bootstrap.min.css" rel="stylesheet" media="screen">
   <link href="/static/bootstrap-responsive.css" rel="stylesheet">
   <link href="/static/bootstrap.css" rel="stylesheet">

  <style type="text/css">
	body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
	
      }
  .preview {
  	float: left;
	margin-right: 20px;
	margin-bottom: 30px;
  }    
  .preview .thumb {
    border: 0 none;
    margin-top: 5px;
    max-height: 125px;
  }
	
	/* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 900px;
	border-style: solid;
	border-color: transparent;
	background-color: #D8D8D8	;
	z-index: 9;
	height : 100%;
	-moz-border-radius: 15px;
	border-radius: 15px;
	
      }
      .container-narrow > hr {
        margin: 30px 0;
      }

	.sidebar-nav {
        padding: 20px 0;
      }

      @media (max-width: 980px) {
        /* Enable use of floated navbar text */
        .navbar-text.pull-right {
          float: none;
          padding-left: 5px;
          padding-right: 5px;
        }
       
	
  </style>

</head>
<body>

  <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          
          <a class="brand pull-left" href="/"><em>Lauren's Lovely Landscapes </em></a>
          
	  
          <div class="nav-collapse collapse">
           	<ul class="nav navbar-nav pull-right">           		
           		% if not defined('redirectUrl'):
           		%   print 'Warning: redirectUrl not set and redirects may not work as expected'
           		%   redirectUrl = ''
           		% end
           		
           		% if not defined('currentUrl'):
           		%   print 'Warning: currentUrl not set and the navbar will not indicate the current page'
           		%   currentUrl = ''
           		% end
           		
           		% if not defined('username'):
           		%    print 'Warning: username is not defined on this page and the navbar may not act as expected'
           		%    username = None
           		% end
           		% if username is None:      		
	           		% if 'signin' in currentUrl: 
	           			<li class="active">
	           		% else:
	           			<li>
	           		% end
	           		<a href="/signin/{{redirectUrl}}">Sign In</a></li>
	           		
	           		% if 'register' in currentUrl: 
	           			<li class="active">
	           		% else:
	           			<li>
	           		% end
	           		<a href="/register">Register</a></li>	           	   	
	           	
	           	% else:
	           		<li><a href="/signout">Sign Out</a></li>
	            
	            % end
           		
           	</ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>  <!-- end of div for nav bar-->
  
  <div class="container">
  <!-- <table class="table table-hover">
  <tr> -->
  <div class="hero-unit">
