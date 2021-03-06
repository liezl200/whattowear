import urllib2
import json
header = '''
<header class="navbar navbar-static-top bs-docs-nav" id="top" role="banner" style="background-color:rgba(2,132,130,0.7); z-index: 9;">
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
<!-- Menu -->
<nav class="menu" id="theMenu">
  <div class="menu-wrap">
    
    <h1 class="logo"><a href="#weather-wrap">LATE SUMMER</a></h1>
    <i class="fa fa-arrow-right menu-close"></i>
    <p>Printed tops are warm enough to wear in autumn weather, and always look great with dark pants!</p>
    <p>Jeans look crisp in darker washes, especially when they fit well.</p>
    <p>Cardigans and hoodies are a staple of any season-transitioning wardrobe.</p>
    <p>Always be on the lookout for end of season sales!</p>
    <h1 class="logo"><a href="/theory">TRENDING HUES</a></h1>
    <ul>
      <li style="color: #8A4396";>Eggplant</li>
      <li style="color: #C19A6B";>Camel</li>
      <li style="color: #800000";>Maroon</li>
      <li style="color: #D3D3D3";>Greys</li>
      <li style="color: #FFC0CB";>Pinks</li>
    </ul>

  </div>
  
  <!-- Menu button -->
  <div id="menuToggle"><i class="fa fa-bars"></i></div>
</nav>

'''

footer = '''
<footer class="bs-docs-footer">
  <div class="col-lg-8">
    <div id="weather-wrap">
      <div id="white-cover">
      </div>
      <iframe id="forecast_embed" type="text/html" frameborder="0" height="245" width="100%" src="http://forecast.io/embed/#lat=47.6097&lon=122.3331&name=Seattle&color=teal"> </iframe>
    </div>
  </div>
  <div class="col-lg-4" style="background-color: white; z-index: 4; height: 288px;">
    <p style="color:grey;">
      </br>
      Hello, there!</br>
      </br>We are a group of rising college freshmen who understand the struggle of picking each day's outfit and want to do our part to relieve the world's fashion-related dilemmas. 
      </br></br>This project was created by Stud Squad: Alice Ma, Liezl Puzon, and Lukas Munoz. Enjoy! </br></br>
      <img src="http://www.google.com/edu/images/programs/cssilogo.png" width="150px" style="display:inline;"></img></p>

  </div>
</footer>
<script src="/static/bootstrap.min.js"></script>
<script src="static/main.js"></script>
<script src="static/masonry.pkgd.min.js"></script>
<script src="static/imagesloaded.js"></script>
<script src="static/classie.js"></script>
'''
def getHeader(pageRoute):
  header2 = getWeather()
  return header2
def getFooter():
  return footer
def getWeather():
  response = urllib2.urlopen('https://api.forecast.io/forecast/4d13f73fd2b725c8f2030bca99019789/47.6097,122.3331')
  data = json.load(response)
  forecastTxt = ''
  forecastList = []
  for i in xrange(0, 7):
    forecastList.append(data['daily']['data'][i]['summary'])
    forecastTxt += forecastList[i] + '<br><br>'
  return header.replace('{{{insert weather}}}', forecastTxt)
  '''
  response = urllib2.urlopen('http://api.wunderground.com/api/86959302e6145cbe/forecast/q/WA/Seattle.json')
  data = json.load(response)
  forecastText = ''
  forecastList = []
  for i in xrange(0, 7):
    forecastList.append(data['forecast']['txt_forecast']['forecastday'][i]['fcttext'])
    forecastText += forecastList[i] + '<br><br>'
  return header.replace('{{{insert weather}}}', forecastText)
  '''
