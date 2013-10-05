#!/usr/bin/python
import os
import sys

# figure out where the script is so we can setup paths relative to it
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))

# account for where we live
sys.path.append(scriptPath)
#sys.path.append(scriptPath + '/lib')

import falcon_mvc.router as router

# the router can be loaded in a couple of different ways

# Either load it without an argument
#router.Router.load()

# Or load it with an argument which is then passed to each
# controller as it is instantiated
d = {}
d['test1'] = 'bob'
d['test2'] = 'fred'
router.Router.load(d)

# Now we can fire up a basic wsgi app server listening on port 8080
router.Router.listen()

