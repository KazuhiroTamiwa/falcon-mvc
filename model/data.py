# define a very basic model
class model:
   def __init__(self, data=False):
      self.dataHandle = data
      print 'model loaded'

   def get(self, arg):
      print 'model:get: %s' % arg
      print 'model:get: %s' % str(self.dataHandle)
