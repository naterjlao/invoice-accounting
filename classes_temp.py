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

	def __str__(self):
		delim = "\n\n"
		result = ""
		result+= "Invoice ID: " + str(self.id) + delim
		result+= "PO Number: " + str(self.po_num) + delim
		result+= "Date: " + str(self.date) + delim
		result+= "Company:\n" + str(self.company) + delim
		result+= "Client:\n" + str(self.client)
		result+= "Bill Table:\n" + str(self.bill_table)
		return result

	def setDate(self,day,month,year):
		self.date.setDate(day,month,year)
	
	def setCompany(self):
		pass
		# TODO

	def enterFields(self,descrip,cost,quant):
		self.bill_table.add(descrip,cost,quant)

###############################################################################
# Class definition of an invoice number. Invoice numbers need to a unique
# identifier for each invoice created. May be strictly numeric or alphanumeric
# depending on implementation.
###############################################################################
class InvoiceNum:
	def __init__(self):
		self.invoiceNum = (12345,67890)
	
	def __str__(self):
		return "%d-%d" % self.invoiceNum

	# Returns the format string of an invoice number (ie. "XXXX-XXXX")
	def returnFormatString():
		return "XXXX-XXXX"
		
	
###############################################################################
# Class definition of a date.
###############################################################################
class Date:
	def __init__(self):
		self.day = 0
		self.month = 0
		self.year = 0
		
	def __str__(self):
		return "%d-%d-%d" % (self.month,self.day,self.year)

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
		self.street_address = "12345 Placeholder Address"
		self.city_state_country = "Placeholder City, State, Country"
		self.zipcode = "12345"

	def __str__(self):
		return "%s\n%s\n%s" % (self.street_address,self.city_state_country,self.zipcode)

class PONumber:
	def __init__(self):
		self.po_num = 12345

	def __str__(self):
		return str(self.po_num)

class PhoneNumber:
	def __init__(self):
		self.phone = "123-456-7890"

	def __str__(self):
		return self.phone

class Website:
	def __init__(self):
		self.website = "www.placeholder.com"

	def __str__(self):
		return self.website


###############################################################################
# Class definition of company. Includes fields for:
###############################################################################
class Company:
	def __init__(self):
		self.name = "Placeholder Company"
		self.address = Address()
		self.phone = PhoneNumber()
		self.website = Website()
		#TODO
		
	def __str__(self):
		result = ""
		result+= self.name + "\n"
		result+= str(self.address) + "\n"
		result+= str(self.phone) + "\n"
		result+= str(self.website)
		
		return result
	
###############################################################################
# Class definition of a table of bills. Includes columns for:
#	- Description | Unit Cost | Qty/Rate | Amount
#	- At the bottom is:
#		- Subtotal
#		- Discount
#		- Tax rate
#		- Tax
#		- Total Balance Cost
# The way that discount rate and tax rate is calculated is done through the
# the subtotals of items before any final value is calculated.
# Therefore, the discount amount and tax amount are independent of each other.
# The difference (sum amount) is only calculated once requested by the user.
###############################################################################
class BillTable:
	def __init__(self):
		self.table = []
		self.tableMutate = False
		self.taxRate = 0
		self.totalBalance = 0
		self.discountRate = 0
		self.subtotal = 0
		
	def __str__(self):
		result = ""
		for e in self.table:
			result += str(e)
			result += '\n'
		return result
			
	class Entry:
		def __init__(self,descrip,cost,quant):
			self.descrip=descrip
			self.cost=cost
			self.quant=quant
			self.amount=self.getAmount()
			
		def __str__(self):
			return ("%s: cost=%f quantity=%f amount=%f" % (self.descrip,self.cost,self.quant,self.amount))
			
		def updateDescription(self,descrip):
			self.descript = descript
			
		def updateCost(self,cost):
			self.cost = cost
		
		def updateQuant(self,quant):
			self.quant = quant
			
		def getAmount(self):
			return self.cost * self.quant
	
	# Adds an element to the table.
	# Amount is calculated with cost x quant
	def add(self,descrip,cost,quant):
		self.tableMutate = True
		self.table.append(BillTable.Entry(descrip,cost,quant))
		
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
		return self.calcSubtotal() - self.calcDiscount() + self.calcTax()
