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
import datetime
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
    query = closet.Outfit.query().filter(closet.Outfit.user == users.get_current_user())
    items = query.fetch()
    logging.info(items)
    if(self.request.get("hiddenInput") == 'true'):
      for i in range(0, len(items)):
        items[i].key.delete()
        logging.info('deleted one')
      query = closet.Outfit.query().filter(closet.Outfit.user == users.get_current_user())
      items = query.fetch()
      logging.info(items)
    tomorrowsOutfit = None
    todaysOutfit = None
    today = True
    tomorrow = True
    for i in range(0, len(items)):
      logging.info(i)
      if(items[i].date < datetime.date.today()):
        items[i].key.delete()
      elif(items[i].date == datetime.date.today()):
        todaysOutfit = items[i]
        today = False
      elif(items[i].date == datetime.date.today() + datetime.timedelta(days=1)):
        tomorrowsOutfit = items[i]
        tomorrow = False
    if(today):
      todaysOutfit = closet.getOutfit("today")
      logging.info('got outfit')
      if(todaysOutfit != None):
        todaysOutfit.put()
    if(tomorrow):
      tomorrowsOutfit = closet.getOutfit("tomorrow")
      if(tomorrowsOutfit != None):
        tomorrowsOutfit.put()
    template_values['todaysRecommendation'] = todaysOutfit
    template_values['tomorrowsRecommendation'] = tomorrowsOutfit#CHANGE TO TOMORROW
    precip = None
    currWeather = closet.getWeather()
    if float(currWeather['precipProbability']) > 0.1:
      precip = 'You might want to bring a jacket because there is a ' + str(currWeather['precipProbability'] * 100) + '% chance of ' + currWeather['precipType'] + '.'
    template_values['precipitation'] = precip
    self.response.out.write(template.render(template_values))

class TheoryHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/'), "footer": header.getFooter()}
    template = closet.jinja_environment.get_template('theory.html')
    self.response.out.write(template.render(template_values))

#jinja_environment = jinja2.Environment(loader=
#      jinja2.FileSystemLoader(os.path.dirname(__file__)))


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
