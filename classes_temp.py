#!/usr/bin/python3
###############################################################################
# TEMPORARY FILE FOR TESTING
###############################################################################

# Propietary
import config
import utils

# Wrapper for debug messages
def debug(message):
	utils.debug(message,type="classes")

###############################################################################
# Class definition of an invoice. Contains subfields of data types that
# define an invoice.
###############################################################################
class Invoice:
	def __init__(self):
		self.id = InvoiceNum()
		self.po_num = PONumber()  # used for company tracking -- different from in house invoice number
		self.date = Date()
		self.company = Company()  # contains Address
		self.client = Company()  # contains Address
		# Table of Transactions
		self.bill_table = BillTable()
		
	def enterFields(self,descrip,cost,quant):
		self.bill_table.add(descrip,cost,quant)

###############################################################################
# Class definition of an invoice number. Invoice numbers need to a unique
# identifier for each invoice created. May be strictly numeric or alphanumeric
# depending on implementation.
###############################################################################
class InvoiceNum:
	def __init__(self):
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
	def __init__(self):
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
# - PO Number
###############################################################################
class Address:
	def __init__(self):
		self.name = "business name"
		self.address = "18824 Bent Willow"
		self.city_state_country = "XXX, XXX, XXX"
		self.zipcode = "XXXXX"

class PONumber:
	def __init__(self):
		self.po_num = "ABCDEF"

class PhoneNumber:
	def __init__(self):
		self.phone = "123-456-7890"

class Website:
	def __init__(self):
		self.website = "www.xxx.com"

###############################################################################
# Class definition of company. Includes fields for:
###############################################################################
class Company:
	def __init__(self):
		self.name = "FBI"
		self.address = Address()
		self.phone = PhoneNumber()
		self.website = Website()
		#TODO
		
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
	def __init__(self):
		self.table = []
		self.tableMutate = False
		self.taxRate = 0
		self.totatBalance = 0
		self.subtotal = 0
		
	class Entry:
		def __init__(self,descrip,cost,quant):
			self.descrip=descrip
			self.cost=cost
			self.quant=quant
			self.updateAmount()
			
		def __str__(self):
			print("%s: %d x %d = %d" % (self.descrip,self.cost,self.quant))
			
		def updateDescription(self,descrip):
			self.descript = descript
			
		def updateCost(self,cost):
			self.cost = cost
		
		def updateQuant(self,quant):
			self.quant = quant
			
		def updateAmount(self):
			self.amount = self.cost * self.quant
	
	# Adds an element to the table.
	# Amount is calculated with cost x quant
	def add(self,descrip,cost,quant):
		self.tableMutate = True
		self.table.append(Entry(descrip,cost,quant))
		
	# Removes an element at an index
	def remove(self,idx):
		self.tableMutate = True
		return self.table.pop(idx)
	
	# Sets the tax rate of the table
	# Validates if the given rate is valid
	def setTaxRate(self,rate):
		self.taxRate = rate
	
	# Sets the discount rate of the table
	# Validates if the given rate is valid
	def setDiscountRate(self,rate):
		self.discountRate = rate
		
	# Calculate subtotal of all cost amounts before taxes and discounts
	def calcSubtotal(self):
		if (self.tableMutate):			
			self.subtotal = 0
			for entry in self.table:
				self.subtotal += entry.amount
		self.tableMutate = False
		return self.subtotal
	
	# Calculate the tax from the subtotal and the tax rate
	def calcTax(self):
		return self.calcSubtotal() * self.taxRate
	
	# Calculate the discount amount from the subtotal and the dicount rate
	def calcDiscount(self):
		return self.calcSubtotal() * self.discountRate
	
	# Calculate the total balance based on the calculated tax and discount amount
	def calcTotalBalance(self):
		return self.calcSubtotal - self.calcDiscount() + self.calcTax()