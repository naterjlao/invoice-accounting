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
import classes_temp as classes

# Propietary
import config

def createPDFFileName(po_num):
	return "%s_%s.%s" % (config.PDF_FILE_PREFIX,str(po_num),config.PDF_FILE_EXTENS)

def generatePDFFile(invoice: classes.Invoice):
	pdf = fpdf.FPDF()
	pdf.add_page()
	pdf.set_font("Arial", size=12)
	pdf.cell(200,10,txt=invoice.returnString(),ln=1,align="C")
	pdf.output(createPDFFileName(invoice))
	# TODO untested


# Tester Function
if __name__ == '__main__':
	# Create sample Invoice
	invoice = classes.Invoice()
	print(invoice.returnString())

