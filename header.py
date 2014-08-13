header = '''
<header class="navbar navbar-static-top bs-docs-nav" id="top" role="banner" style="background-color:rgba(2,132,130,0.7);">
    <div class="container">
      <div class="navbar-header">
        <a href="../" class="navbar-brand">WHAT TO WEAR</a>
      </div>
      <nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">
        <ul class="nav navbar-nav" >
          <li><a href="/createItemForm">+ ITEM</a></li>
          <li><a href="/viewItems">CLOSET</a></li>  
          <li><a href="/outfits">OUTFITS</a></li> 
          <li><a href="/theory">COLOUR THEORY</a></li>  
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="/settings">SETTINGS</a></li>
          <li><a href="/Logout">LOGOUT</a></li>
        </ul>
      </nav>
    </div>


  </header>
  '''
def getHeader(pageRoute):
	return header
