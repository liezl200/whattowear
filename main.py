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
import header
import closet
from google.appengine.ext import ndb
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {"header": header.getHeader('/')}
    template = closet.jinja_environment.get_template('home.html')
    self.response.out.write(template.render(template_values))


#jinja_environment = jinja2.Environment(loader=
#      jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/createItem', closet.CreateItemHandler),
  ('/createItemForm', closet.CreateItemFormHandler),
  ('/viewItems', closet.ViewItemsHandler),
  ('/about', closet.AboutHandler),
], debug=True)
