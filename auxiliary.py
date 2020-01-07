#!/usr/bin/python3
###############################################################################
# File: auxiliary.py
# Authors: Oscar Quintanilla (Oquintanilla0@gmail.com)
#          Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Defines classes and functions for PDF exports and SQL handling.
###############################################################################

# Propietary
import config
import utils
import classes

# Wrapper for debug messages
def debug(message):
	utils.debug(message,type="auxiliary")

###############################################################################
# Processes the given invoice and generates a PDF file.
# Arguments:
# - invoice: a classes.Invoice object representing the data to be exported
# - dst: an absolute path to where the PDF file will be exported to
###############################################################################
def exportPDF(invoice: classes.Invoice, dst: str):
	# TODO
	pass

###############################################################################
# Updates the SQL server on host
# Arguments:
# - invoice: a classes.Invoice object representing the data to be exported
###############################################################################
def updateSQL(invoice: classes.Invoice):
	# TODO
	pass
