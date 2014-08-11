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
from google.appengine.ext import ndb
from google.appengine.api import users

def dropItems():
  for i in Item.query().fetch():
      i.key.delete()
class Item(ndb.Model):
  name = ndb.StringProperty(required=True)
  availability = ndb.StringProperty(required=True)
class CreateItemFormHandler(webapp2.RequestHandler):
  def get(self): 
    template_values = {"header": header.getHeader('/createItem')}
    template = jinja_environment.get_template('createItem.html')
    self.response.out.write(template.render(template_values))
class CreateItemHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/createItemForm')}
    name = self.request.get('itemName')
    availability = "available" if self.request.get('available') == 'available' else "unavailable"
    template_values['name'] = name
    template_values['availability'] = availability
    item = Item(name=name, availability=availability)
    item.put()
    template = jinja_environment.get_template('createItem.html')
    self.response.out.write(template.render(template_values))
class ViewItemsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/viewItems')}
    template_values['items'] = Item.query().fetch()
    template = jinja_environment.get_template('viewItems.html')
    self.response.out.write(template.render(template_values))
class AboutHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/about')}
    template = jinja_environment.get_template('about.html')
    self.response.out.write(template.render(template_values))
class ProfileHandler (webapp2.RequestHandler):
  def get(self): 
    template_values['current_user'] = users.get_current_user()

app = webapp2.WSGIApplication([
  ('/createItem', CreateItemHandler),
  ('/createItemForm', CreateItemFormHandler),
  ('/viewItems', ViewItemsHandler),
  ('/about', AboutHandler),
  #('/updateItem', UpdateItemHandler),
  #('/deleteItem', DeleteItemHandler),
  #('/choose', ChooseHandler),
], debug=True)
