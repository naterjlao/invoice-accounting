#!/usr/bin/python3
###############################################################################
# File: pdfGen.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Constructs, designs and generates a PDF for invoices.
###############################################################################

import fpdf
import classes

# Propietary
import config

def createPDFFileName(po_num):
	return "%s_%s.%s" % (config.PDF_FILE_PREFIX,str(po_num),config.PDF_FILE_EXTENS)

def generatePDFFile(invoice: classes.Invoice):
	pass
