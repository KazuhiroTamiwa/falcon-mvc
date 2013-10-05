import falcon

# the base controller other controllers are derived from
class basecontroller:
   # accept an opaque data object that we don't inspect
   # for use by the controller
   def __init__(self, data=False):
      self.dataHandle = data

      # define the route this controller will handle
      self.routePath = '/basecontroller'
      print 'loaded basecontroller'


