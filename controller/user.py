import os
import sys
import falcon

import falcon_mvc.basecontroller as basecontroller
import model.data

# define a new controller derived from basecontroller.
# all controller class names should be called 'controller'
# as that is how the router instantiates them
class controller(basecontroller.basecontroller):
   # rather than override __init__(), we create a
   # local version of init that allows us to define things
   # like the route this controller will handle
   def __local__(self):
      self.routePath = '/{user}/test'

   # now we get into standard falcon methods
   def on_get(self, req, resp, user):
      a = req.get_param('cd')

      # self.dataHandle is an object that was handed to the
      # controller automatically at initialization
      print self.dataHandle
      print 'get user: %s => %s' % (user, a)

      m = model.data.model(self.dataHandle)
      m.get('fred')
      resp.status = falcon.HTTP_200
      resp.body = 'get body'


   def on_post(self, req, resp, user):
      try:
         raw_json = req.stream.read()
      except Exception, e:
         print 'get exception: %s' % str(e)

      print 'post: %s' % user
      resp.status = falcon.HTTP_200
      resp.body = 'post body'

