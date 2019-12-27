#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Graphical user interface for invoice application.
#   Python tkinter: https://docs.python.org/3/library/tk.html
###############################################################################

import tkinter as tk
import tkinter.ttk as ttk
import classes
import config

class Application(tk.Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.pack() # fill out the entire window
		self.createGUI()
		self.layoutGUI()
	
	###############################################################################
	# An invoice form is comprised of the following elements:
	# - Header:
	#	- Invoice number
	#	- Date of Issue
	#	- Billed to address:
	#		- Name
	#		- Street Addr
	#		- City, State and Country
	#		- ZIP
	#	- Company Name
	#		- Street Addr
	#		- City, State and Country
	#		- ZIP
	#		- phone number
	#		- email
	#		- website
	# - Body:
	#	- Table of bills with the following columns:
	#		- Description | Unit Cost | Qty/Rate | Amount
	#		- At the bottom is:
	#			- Subtotal
	#			- Discount
	#			- Tax rate
	#			- Tax
	#			- Total Balance Cost
	# - Footer:
	#	- Terms and conditions
	#	- Legal statements
	###############################################################################
	def createGUI(self):
	
		# Main Title
		#self.mainTitleLabel = tk.Label(self, text="INVOICE GENERATOR", anchor=tk.W, justify=tk.LEFT)
		
		# Invoice Number
		self.invoiceNumberLabel = tk.Label(self, text=("Invoice number (%s):" % classes.InvoiceNum.returnFormatString()))
		self.invoiceNumberField = tk.Entry(self)
		
		# Date
		self.dateLabel = tk.Label(self, text=("Date of issue (%s):" % classes.Date.returnFormatString()))
		self.dateField = tk.Entry(self)
		
		# Bill To Address
		self.billToLabel = tk.Label(self, text="Billed to:")
		self.billToNameLabel = tk.Label(self, text="Name:")
		self.billToAddrLabel = tk.Label(self, text="Street Address:")
		self.billToCityLabel = tk.Label(self, text="City, State, Country:")
		self.billToZipLabel = tk.Label(self, text="Zip code:")
		self.billToNameField = tk.Entry(self)
		self.billToAddrField = tk.Entry(self)
		self.billToCityField = tk.Entry(self)
		self.billToZipField = tk.Entry(self)
		
		# Company Info
		self.companyNameLabel = tk.Label(self, text=config.COMPANY_NAME)
		self.companyAddrLabel = tk.Label(self, text=config.COMPANY_ADDR)
		self.companyCSCLabel = tk.Label(self, text=("%s, %s, %s" % (config.COMPANY_CITY, config.COMPANY_STATE, config.COMPANY_COUNTRY)))
		self.companyZipLabel = tk.Label(self, text=config.COMPANY_ZIP)
		self.companyPhoneLabel = tk.Label(self, text=config.COMPANY_PHONE)
		self.companyEmailLabel = tk.Label(self, text=config.COMPANY_EMAIL)
		self.companyWebsiteLabel = tk.Label(self, text=config.COMPANY_WEBSITE)
	

		# Enter Fields
		self.fieldsEntryLabel = tk.Label(self, text="Enter Fields")
		self.fieldsEntriesLabel = {}
		self.fieldsEntries = {}
		for f in config.TABLE_COLUMNS.keys():
			self.fieldsEntriesLabel[f] = tk.Label(self, text=str(f)+":")
			self.fieldsEntries[f] = tk.Entry(self)
		
		# Enter Button
		self.fieldsEnterButton = tk.Button(self,text="Enter",command=self.fieldsEnterButtonHandler)

		# Bill Table
		self.createTable()
	
	def createTable(self):
		self.table = ttk.Treeview(self, columns=tuple(config.TABLE_COLUMNS.keys()), show='headings')

		# set the headings to the appropriate name, else they will be empty
		for key in config.TABLE_COLUMNS.keys():
			self.table.heading(key,text=config.TABLE_COLUMNS.get(key))


	def layoutGUI(self):
		# TODO - right now using grid as our layout manager, might need to resort to something more aesthetically pleasing
		#self.mainTitleLabel.grid(row=0, sticky=tk.W)
		self.invoiceNumberLabel.grid(row=1,column=0)
		self.invoiceNumberField.grid(row=1,column=1)
		self.dateLabel.grid(row=1,column=2)
		self.dateField.grid(row=1,column=3)
		self.billToLabel.grid(row=2,column=1)
		self.billToNameLabel.grid(row=3,column=0, sticky=tk.E)
		self.billToAddrLabel.grid(row=4,column=0, sticky=tk.E)
		self.billToCityLabel.grid(row=5,column=0, sticky=tk.E)
		self.billToZipLabel.grid(row=6,column=0, sticky=tk.E)
		self.billToNameField.grid(row=3,column=1)
		self.billToAddrField.grid(row=4,column=1)
		self.billToCityField.grid(row=5,column=1)
		self.billToZipField.grid(row=6,column=1)
		self.companyNameLabel.grid(row=2,column=2)
		self.companyAddrLabel.grid(row=3,column=2)
		self.companyCSCLabel.grid(row=4,column=2)		
		self.companyZipLabel.grid(row=5,column=2)
		self.companyPhoneLabel.grid(row=6,column=2)
		self.companyEmailLabel.grid(row=7,column=2)
		self.companyWebsiteLabel.grid(row=8,column=2)	
		self.fieldsEntryLabel.grid(row=9)
		r = 10
		c = 0
		for f in config.TABLE_COLUMNS.keys():
			self.fieldsEntriesLabel.get(f).grid(row=r,column=c)
			self.fieldsEntries.get(f).grid(row=r+1,column=c)
			c += 1
		self.fieldsEnterButton.grid(row=12)
		self.layoutTable()
		
	def layoutTable(self):
		self.table.grid(row=13, columnspan=4)
		
	def updateTable(self):
		# The Invoice objecft must be updated alongside the table.
		# Since there is overhead associated with clearing out the entire
		# GUI table, we will opt to support deletion and additions concurrently
		pass


	##############################################################################
	# Handler Functions
	##############################################################################

	def fieldsEnterButtonHandler(self):
		# TODO tester
		# Note that there is a 'text' argument and that unique id's need to be utilized for syncronize deletions
		# and subsequent additions
		# TODO get() function to pull text from Entries
		'''
		self.table.insert('','end',values=("ffdfd","fdfd","fdfdf","Fdfdf"))
		'''
		pass
		
		
	
