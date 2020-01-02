#!/usr/bin/python3
###############################################################################
# File: linker.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Defines the Manager class that links GUI and Classes.
###############################################################################

# Propietary
import config
import utils

# Wrapper for debug messages
def debug(message):
	utils.debug(message,type="linker")

class Manager:
	def __init__(self,logger=None):
		pass
		
	def fieldsEnterButtonHandler(self):
		debug("Entering fieldsEnterButtonHandler")
		pass