#!/usr/bin/python3

import fpdf

pdf = fpdf.FPDF()
pdf.add_page()
pdf.set_font("Arial",size=12)
pdf.cell(200,10,txt="Welcome to demo!", ln=1, align="C")
pdf.output("simple_demo.pdf")

