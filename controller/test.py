import falcon

import falcon_mvc.basecontroller as basecontroller

class controller(basecontroller.basecontroller):
   def __local__(self):
      self.routePath = '/test'

   def on_get(self, req, resp):
      print 'get'
      resp.status = falcon.HTTP_200
      resp.body = 'get body'

