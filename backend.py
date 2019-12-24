#!/usr/bin/python3
###############################################################################
# File: backend.py
# Author: <NAME> (<EMAIL>)
# Language: python3
# Description:
#   Obtains data from the Invoice GUI and processes information.
###############################################################################

# TODO
# - SQL management
# - PDF exporting

###############################################################################
# Class definition of an invoice number. Invoice numbers need to a unique
# identifier for each invoice created. May be strictly numeric or alphanumeric
# depending on implementation.
###############################################################################
class InvoiceNum:
	def __init__():
		# TODO
		pass
	
	# Returns the format string of an invoice number (ie. "XXXX-XXXX")
	def returnFormatString():
		return "XXXX-XXXX"
		
	# TODO
	
###############################################################################
# Class definition of a date.
###############################################################################
class Date:
	def __init__():
		# TODO
		pass
		
	# Returns the format string of a date (ie. "MM-DD-YY")
	def returnFormatString():
		return "MM-DD-YY"

###############################################################################
# Class definition of an address. Includes fields for:
# - Name
# - Street Address
# - City, State, Country
# - Zip code
###############################################################################
class Address:
	def __init__():
		# TODO
		pass
		
	# TODO
	
###############################################################################
# Class definition of company. Includes fields for:
#	- Company Name
#	- Street Addr
#	- City, State and Country
#	- ZIP
#	- phone number
#	- email
#	- website
###############################################################################
class Company:
	def __init__():
		# TODO
		pass
		
	# TODO
	
###############################################################################
# Class definition of a table of bills. Includes columns for:
#	- Description | Unit Cost | Qty/Rate | Amount
#	- At the bottom is:
#		- Subtotal
#		- Discount
#		- Tax rate
#		- Tax
#		- Total Balance Cost
###############################################################################
class BillTable:
	def __init__():
		# TODO
		pass
	
	# Adds an element to the table.
	# Amount is calculated with cost x quant
	def add(self,descrip,cost,quant):
		# TODO
		pass
		
	# Removes an element at an index
	def remove(self,idx)
		# TODO
		pass
	
	# Sets the tax rate of the table
	# Validates if the given rate is valid
	def setTaxRate(self,rate)
		# TODO
		pass
	
	# Sets the discount rate of the table
	# Validates if the given rate is valid
	def setDiscountRate(self,rate)
		# TODO
		pass
		
	# Calculate subtotal of all cost amounts before taxes and discounts
	def calcSubtotal(self):
		# TODO
		pass
	
	# Calculate the tax from the subtotal and the tax rate
	def calcTax(self)
		# TODO
		pass
	
	# Calculate the discount amount from the subtotal and the dicount rate
	def calcDiscount(self)
		# TODO
		pass
	
	# Calculate the total balance based on the calculated tax and discount amount
	def calcTotalBalance(self):
		# TODO
		pass
