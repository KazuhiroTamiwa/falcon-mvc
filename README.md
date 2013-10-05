falcon-mvc
==========

Falcon-mvc is a basic starter project to build falcon apps in a standard mvc style.
It is meant to be customized to your needs.  The goal of falcon-mvc is to make the
loading and registering of controllers within falcon a little more automatic while
maintaining a common mvc style layout.

The heart if falcom-mvc is a basic router class.  At startup, it automatically loads
any controller found in the controller directory.  It then defines a route in falcon
for each loaded controller.  It then gets out of the way and the rest of the app acts
as a normal falcon app.


controllers
===========

In falcon-mvc, a controller has a basic generic layout derived from a base controller
and then augmented as needed.  The controller can accept an opaque object at startup
to be used as needed for things like application configuration, database handles or 
whatever you need.  The object is not inspected by falcon-mvc.  It is simply passed
on to be used by user code in the controller.  The controller also defines the route
it will handle.  

Apart from these, a falcon-mvc controller acts as a normal falcon controller.  It is
left to the user to implement things like on_get(), on_post() and other falcon methods.


example controller
==================
The following example lives in controller/test.py:

import falcon
import falcon_mvc.basecontroller as basecontroller

class controller(basecontroller.basecontroller):
   def __local__(self):
      self.routePath = '/test'

   def on_get(self, req, resp):
      print 'get'
      resp.status = falcon.HTTP_200
      resp.body = 'get body'


Here, we define a new controller derived from basecontroller.  It defines the route
it will handle in falcon as '/test'.  It then implements a basic GET handler for that
route.

models
======

In falcon-mvc, a model can be anything.  The model directory is simply a standard location
to define models.  It can be used or not.

views
=====

The view directory in falcon-mvc is just like the model directory.  It is simply there
as an orginazational standard.  It can be used or not.


