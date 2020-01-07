#!/usr/bin/python3
###############################################################################
# File: pdfGen.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Constructs, designs and generates a PDF for invoices.
#   https://www.blog.pythonlibrary.org/2018/06/05/creating-pdfs-with-pyfpdf-and-python/
#   https://pyfpdf.readthedocs.io/en/latest/index.html
###############################################################################

import fpdf
import classes

# Propietary
import config

def createPDFFileName(po_num):
	return "%s_%s.%s" % (config.PDF_FILE_PREFIX,str(po_num),config.PDF_FILE_EXTENS)

def generatePDFFile(invoice: classes.Invoice):
	pass
