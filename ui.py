#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Graphical User Interface for Accounting Invoices.
#   Python tkinter: https://docs.python.org/3/library/tk.html
###############################################################################




import tkinter as tk
import backend
import config

class Application(tk.Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.pack() # fill out the entire window
		self.createGUI()
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
		self.mainTitleLabel.grid(row=0, sticky=tk.W)
		
		# Invoice Number
		self.invoiceNumberLabel = tk.Label(self, text="Invoice number (XXXX-XXXX):")
		self.invoiceNumberLabel.grid(row=1,column=0)
		self.invoiceNumberField = tk.Entry(self)
		self.invoiceNumberField.grid(row=1,column=1)
		
		# Date
		self.dateLabel = tk.Label(self, text="Date of issue (MM-DD-YY):")
		self.dateLabel.grid(row=1,column=2)
		self.dateField = tk.Entry(self)
		self.dateField.grid(row=1,column=3)
		
		# Bill To Address
		self.billToLabel = tk.Label(self, text="Billed to:")
		self.billToLabel.grid(row=2,column=1)
		self.billToNameLabel = tk.Label(self, text="Name:")
		self.billToNameLabel.grid(row=3,column=0, sticky=tk.E)
		self.billToAddrLabel = tk.Label(self, text="Street Address:")
		self.billToAddrLabel.grid(row=4,column=0, sticky=tk.E)
		self.billToCityLabel = tk.Label(self, text="City, State, Country:")
		self.billToCityLabel.grid(row=5,column=0, sticky=tk.E)
		self.billToZipLabel = tk.Label(self, text="Zip code:")
		self.billToZipLabel.grid(row=6,column=0, sticky=tk.E)
		self.billToNameField = tk.Entry(self)
		self.billToNameField.grid(row=3,column=1)
		self.billToAddrField = tk.Entry(self)
		self.billToAddrField.grid(row=4,column=1)
		self.billToCityField = tk.Entry(self)
		self.billToCityField.grid(row=5,column=1)
		self.billToZipField = tk.Entry(self)
		self.billToZipField.grid(row=6,column=1)
	






