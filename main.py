#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import urllib2
import json
import os
import random
import webapp2
import header
import closet
import logging
from google.appengine.ext import ndb
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
  def get(self):
    renderedHeader = header.getHeader('/')
    if(users.get_current_user() == None):
      renderedHeader = renderedHeader.replace('<li><a href="/settings">SETTINGS</a></li>', '')
      renderedHeader = renderedHeader.replace('Logout', 'Login')
      renderedHeader = renderedHeader.replace('LOGOUT', 'LOGIN')
    template_values = {"header": renderedHeader, "footer":header.getFooter()}
    jpgs = [177, 187, 207, 317, 322, 357, 404, 433]

    template_values['randomImg'] = '/static/' + str(jpgs[random.randint(0,7)]) + '.jpg'
    template = closet.jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    loginurl = users.create_login_url(dest_url='/', _auth_domain=None, federated_identity=None)
    self.redirect(loginurl)
class LogoutHandler(webapp2.RequestHandler):
  def get(self):
    dest_url = '/'
    logouturl = users.create_logout_url(dest_url)
    self.redirect(logouturl)
    #template_values = {'logouturl' : logouturl}
    #template = closet.jinja_environment.get_template('about.html')
    #self.response.out.write(template.render(template_values))

    logging.info(logouturl)

class SettingsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/'), "footer": header.getFooter()}
    template = closet.jinja_environment.get_template('settings.html')
    self.response.out.write(template.render(template_values))

class OutfitsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/'), "footer": header.getFooter()}
    template = closet.jinja_environment.get_template('outfits.html')

    self.response.out.write(template.render(template_values))

class TheoryHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/'), "footer": header.getFooter()}
    template = closet.jinja_environment.get_template('theory.html')
    self.response.out.write(template.render(template_values))

#jinja_environment = jinja2.Environment(loader=
#      jinja2.FileSystemLoader(os.path.dirname(__file__)))
def getWeather():
  response = urllib2.urlopen('https://api.forecast.io/forecast/4d13f73fd2b725c8f2030bca99019789/47.6097,122.3331')
  data = json.load(response)
  return data['currently']

def selectOutfit():
  currWeather = getWeather()
  if float(currWeather['temperature']) < 67: #later on let the user change this in settings
    pass #select long
  elif float(currWeather['temperature']) < 83:
    pass #select short
  else:
    pass #select short short
  if float(currWeather()['precipProbability']) > 0.1:
    pass # display a warning to bring a jacket
    currWeather()['precipType'] #display this value
  return None #return the outfit combination

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/createItem', closet.CreateItemHandler),
  ('/createItemForm', closet.CreateItemFormHandler),
  ('/deleteItems', closet.DeleteItemsHandler),
  ('/Logout', LogoutHandler),
  ('/Login', LoginHandler),
  ('/viewItems', closet.ViewItemsHandler),
  ('/about', closet.AboutHandler),
  ('/settings', SettingsHandler),
  ('/outfits', OutfitsHandler),
  ('/theory', TheoryHandler)
], debug=True)
