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
import webapp2
from google.appengine.ext import ndb

def dropItems():
  for i in Item.query().fetch():
      i.key.delete()
class Item(ndb.Model):
  name = ndb.StringProperty(required=True)
  availability = ndb.StringProperty(required=True)
class MainHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))

class CreateItemFormHandler(webapp2.RequestHandler):
  def get(self): 
    template_values = {}
    template = jinja_environment.get_template('createItem.html')
    self.response.out.write(template.render(template_values))
class CreateItemHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    name = self.request.get('itemName')
    availability = "available" if self.request.get('available') == 'available' else "unavailable"
    template_values = {'name' : name, 'availability' : availability}
    item = Item(name=name, availability=availability)
    item.put()
    template = jinja_environment.get_template('createItem.html')
    self.response.out.write(template.render(template_values))
class ViewItemsHandler(webapp2.RequestHandler):
  def get(self):
    #template_values = {}
    template_values = {'items' : Item.query().fetch()} 
    template = jinja_environment.get_template('viewItems.html')
    self.response.out.write(template.render(template_values))


jinja_environment = jinja2.Environment(loader=
      jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/createItem', CreateItemHandler),
  ('/createItemForm', CreateItemFormHandler),
  ('/viewItems', ViewItemsHandler),
  #('/updateItem', UpdateItemHandler),
  #('/deleteItem', DeleteItemHandler),
  #('/choose', ChooseHandler),
], debug=True)
