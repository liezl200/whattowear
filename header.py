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
    
    <h1 class="logo"><a href="#weather-wrap">WEATHER</a></h1>
    <i class="fa fa-arrow-right menu-close"></i>
    <p>{{{insert weather}}}</p>
   
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
  <div class="col-lg-4" style="background-color: #333; z-index: 4; height: 245px;">
    <p style="color:white;">
      Created by Stud Squad: Alice Ma, Liezl Puzon, and Lukas Munoz. CSSI 2014.
    </p>

  </div>
</footer>
<script src="/static/jquery-1.11.1.min.js"></script>
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