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
import random
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
    template = jinja_environment.get_template('createItem.html')
    self.response.out.write(template.render(template_values))
class ViewItemsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/viewItems'), "footer":header.getFooter()}
    query = Item.query().filter(Item.user == users.get_current_user())
    items = query.fetch()
    template_values['items'] = items
    template = jinja_environment.get_template('viewItems.html')
    self.response.out.write(template.render(template_values))
class DeleteItemsHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/deleteItems'), "footer":header.getFooter()}
    checkboxArray = self.request.get_all('checkbox')
    query = Item.query().filter(Item.user == users.get_current_user())
    items = query.fetch()
    for id in checkboxArray:
      item = Item.get_by_id(int(id))
      if item in items:
        item.key.delete()
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

def GenerateColors(color):
  generated = []
  R = color[:2]
  G = color[3:5]
  B = color[4:]
  #color0 = R + G + B
  #generated = generated.append(color0)
  color1 = B + G + R
  generated = generated.append(color1)
  color2 = G + B + R
  generated = generated.append(color2)
  return generated

def ColorSimilarity(test_color, target_color): #used to calculate similarity of colours from matching colours returned by GenerateColors
  diff_R = abs(int(test_color[:2], 16) - int(target_color[:2], 16))
  diff_G = abs(int(test_color[3:5], 16) - int(target_color[3:5], 16))
  diff_B = abs(int(test_color[4:], 16) - int(target_color[4:], 16))
  sim_score = diff_R + diff_G + diff_B
  return sim_score 

def MatchColors(): #returns a list of similar colours based on randomly selected first colour
  results = list(Item.query().filter(Item.user == users.get_current_user()).fetch())
  startWith = results[random.randint(0,len(results))] #randomly select the first color to start with
  compatible = {startsWith.key : GenerateColors(startsWith.hexValue)}
  for item in results:
    for  in compatible[each_color]:
      ColorSimilarity(startWith, result)
      closest_match.append()




jinja_environment = jinja2.Environment(loader=
      jinja2.FileSystemLoader(os.path.dirname(__file__)))
