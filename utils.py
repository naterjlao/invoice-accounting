#!/usr/bin/python3
###############################################################################
# File: util.py
# Authors: Oscar Quintanilla (Oquintanilla0@gmail.com)
#          Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Defines utility functions for the invoice application.
###############################################################################

# Propietary
import config

###############################################################################
# Output to terminal (if DEBUG is true in config.py)
###############################################################################
def debug(message,type=""):
	if (config.DEBUG):
		print ("%s: %s" % (type,message))


###############################################################################
# Output to log (if LOG is true in config.py)
###############################################################################
class Logger:
	def __init__(self):
		# TODO use roundrobin on log
		# TODO set designated place based on OS architect
		pass
	
	def log(self):
		pass

