#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Graphical User Interface for Accounting.
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
		
	def message(self):
		print("Hello, %s %s.\n" % (self.firstNameEntry.get(),self.lastNameEntry.get()))
		
