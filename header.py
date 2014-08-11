header = '''
<header class="navbar navbar-static-top bs-docs-nav" id="top" role="banner" style="background-color:rgba(2,132,130,0.7);">
    <div class="container">
      <div class="navbar-header">
        <a style="color: white !important;" href="../" class="navbar-brand">What To Wear</a>
      </div>
      <nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">
        <ul class="nav navbar-nav" >
          <li><a style="color: white !important;" href="/createItemForm">New Item</a></li>
          <li><a style="color: white !important;" href="/viewItems">Closet</a></li>  
          <li><a style="color: white !important;" href="/about">About</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a style="color: white !important;" href="/logout">Logout</a></li>
        </ul>
      </nav>
    </div>


  </header>
  '''
def getHeader(pageRoute):
	return header
