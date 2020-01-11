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
			
	def newInvoiceHandler(self):
		debug("Entering newInvoiceHandler")
		
		# TODO Ask the user to save and close the current invoice instance
		
		
		
		pass
		
	def openInvoiceHandler(self):
		debug("Entering openInvoiceHandler")
		
		# TODO may changed to refer to the SQL storage
		pass
	
	def saveInvoiceHandler(self):
		debug("Entering saveInvoiceHandler")
		
		# TODO filesystem browser
		pass
	
	def saveAsInvoiceHandler(self):
		debug("Entering saveAsInvoiceHandler")
		
		# TODO filesystem browser
		pass	
	
	def exportInvoiceHandler(self):
		debug("Entering exportInvoiceHandler")
		
		# TODO filesystem browser
		pass
	
	def fieldsEnterButtonHandler(self):
		debug("Entering fieldsEnterButtonHandler")
		
		# TODO push to the invoice instance and
		# TODO update the table GUI from here
		pass