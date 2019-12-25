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
import backend
import config

class Application(tk.Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.pack() # fill out the entire window
		self.createGUI()
		self.layoutGUI()
		'''
		# Labels
		self.firstNameLabel = tk.Label(self, text="First Name:")
		self.lastNameLabel = tk.Label(self, text="Last Name:")
		self.firstNameLabel.grid(row=0)
		self.lastNameLabel.grid(row=1)
		
		# Entry fields
		self.firstNameEntry = tk.Entry(self)
		self.lastNameEntry = tk.Entry(self)
		self.firstNameEntry.grid(row=0,column=1)
		self.lastNameEntry.grid(row=1,column=1)
		
		# Buttons
		self.button = tk.Button(self,text="Hello World\n",command=self.message)
		self.button.grid(row=3)		
		self.quit = tk.Button(self,text="QUIT", fg = "red", command = self.master.destroy)
		self.quit.grid(row=4)
		'''
		
	'''	
	def message(self):
		print("Hello, %s %s.\n" % (self.firstNameEntry.get(),self.lastNameEntry.get()))
	'''	
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
		self.mainTitleLabel = tk.Label(self, text="INVOICE GENERATOR", anchor=tk.W, justify=tk.LEFT)
		
		# Invoice Number
		self.invoiceNumberLabel = tk.Label(self, text=("Invoice number (%s):" % backend.InvoiceNum.returnFormatString()))
		self.invoiceNumberField = tk.Entry(self)
		
		# Date
		self.dateLabel = tk.Label(self, text=("Date of issue (%s):" % backend.Date.returnFormatString()))
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
		
		# Bill table
		self.table = ttk.Treeview(self, columns=config.TABLE_COLUMNS)
		
		
		
	def layoutGUI(self):
		# TODO - right now using grid as our layout manager, might need to resort to something more aesthetically pleasing
		self.mainTitleLabel.grid(row=0, sticky=tk.W)
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
		self.table.grid(row=9, columnspan=4)
		
		
		
		
		
		
		
		
		
		
		
	