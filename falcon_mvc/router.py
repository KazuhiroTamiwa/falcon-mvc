#
# Copyright 2013 Mitchell Broome
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

#
# Changes:
#
#   Author:   <mitchell.broome@gmail.com>
#   Version:  v0.1
#   Date:     10/5/2013
#   Desc:     Initial public release
#
#

import os
import sys
import imp
import glob

import falcon

# for testing, we just use the simple wsgi server
from wsgiref import simple_server

# the router class loads up all of the controllers and configures
# falcon to use the routes defined in the controllers
class router():
   def __init__(self):
      self.controllers = {}
      self.app = self.api = falcon.API()

   # look through the controller directory for any *.py files
   # and load the modules adding routes to falcon
   def load(self, data=False):
      scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
      controllerDir = scriptPath + '/controller/*.py'

      # get a file listing
      fl = glob.glob(controllerDir)
      for i in range(len(fl)):
          # split the path to the controller apart
          filename = fl[i]
          modpath = fl[i].split('/')
          fl[i] = modpath[len(modpath)  - 1]
          if fl[i] != '__init__.py': # don't try to load the __init__.py file
             # remove the '.py' from the end of the filename
             fl[i] = fl[i][0:(len(fl[i])-3)]

             worker = fl[i]
             workerDir = scriptPath + '/controller'
             f, filename, desc = imp.find_module(worker, [workerDir])

             # actually load the controller
             self.controllers[worker] = imp.load_module(worker, f, filename, desc)

             # create an instance of the new controller passing in
             # an opaque object for use by the controller as needed
             c = self.controllers[worker].controller(data)

             # call a localized version of __init__()
             c.__local__()
             print 'loading route: %s' % c.routePath

             # add the route to falcon
             self.api.add_route(c.routePath, c)

   def listen(self):
      httpd = simple_server.make_server('0.0.0.0', 8080, self.app)
      httpd.serve_forever()

# create an instance of our router
Router = router()

