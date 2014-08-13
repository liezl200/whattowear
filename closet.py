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
import header
import webapp2
import logging
from main import *
from google.appengine.ext import ndb
from google.appengine.api import users

def dropItems():
  for i in Item.query().fetch():
      i.key.delete()
class Item(ndb.Model):
  hexValue = ndb.StringProperty(required=True)
  topBottom = ndb.StringProperty(required=True)
  longShort = ndb.StringProperty(required=True)
  pattern = ndb.StringProperty(required=True)
  user = ndb.UserProperty(required=True)
class CreateItemFormHandler(webapp2.RequestHandler):
  def get(self): 
    template_values = {"header": header.getHeader('/createItemForm'), "footer": header.getFooter()}
    template = jinja_environment.get_template('createItem.html')
    #template = jinja_environment.get_template('createItem.html')
    self.response.out.write(template.render(template_values))
class CreateItemHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/createItem'), "footer": header.getFooter()}
    color = self.request.get('color')
    topBottom = self.request.get('topbottom')
    longShort = self.request.get('longshort')
    pattern = self.request.get('patternSelector')

    user = users.get_current_user()
    logging.info(user)

    template_values['toporbottom'] = topBottom
    template_values['longorshort'] = longShort

    item = Item(hexValue = color, topBottom = topBottom, longShort = longShort, pattern = pattern, user = user)
    item.put()
    template = jinja_environment.get_template('temporary.html')
    self.response.out.write(template.render(template_values))
class ViewItemsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/viewItems'), "footer":header.getFooter()}
    query = Item.query().filter(Item.user == users.get_current_user())
    items = query.fetch()
    template_values['items'] = items
    template = jinja_environment.get_template('viewItems.html')
    self.response.out.write(template.render(template_values))
class AboutHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/about'), "footer":header.getFooter()}
    template = jinja_environment.get_template('about.html')
    self.response.out.write(template.render(template_values))
class ProfileHandler (webapp2.RequestHandler):
  def get(self): 
    template_values['current_user'] = users.get_current_user()

jinja_environment = jinja2.Environment(loader=
      jinja2.FileSystemLoader(os.path.dirname(__file__)))
