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
    template_values = {"header": header.getHeader('/')}
    template = closet.jinja_environment.get_template('settings.html')
    self.response.out.write(template.render(template_values))

#jinja_environment = jinja2.Environment(loader=
#      jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/createItem', closet.CreateItemHandler),
  ('/createItemForm', closet.CreateItemFormHandler),
  ('/Logout', LogoutHandler),
  ('/Login', LoginHandler),
  ('/viewItems', closet.ViewItemsHandler),
  ('/about', closet.AboutHandler),
  ('/settings', SettingsHandler),
], debug=True)
