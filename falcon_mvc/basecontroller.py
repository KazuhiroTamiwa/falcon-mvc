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


