#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Configuration settings for invoice application.
###############################################################################

# Main window dimensions
GUI_WIDTH = 1200
GUI_HEIGHT = 800
GUI_DIMENSIONS = str(GUI_WIDTH)+"x"+str(GUI_HEIGHT)

# Fields
COMPANY_NAME = "XYZ Inc"
COMPANY_ADDR = "1234 Street"
COMPANY_CITY = "city"
COMPANY_STATE = "state"
COMPANY_COUNTRY = "U.S."
COMPANY_ZIP = "12345"
COMPANY_PHONE = "123-456-7890"
COMPANY_EMAIL = "admin@XYZ.com"
COMPANY_WEBSITE = "www.XYZ.com"
LEGAL_NOTICE = "--- legal notice placeholder ---"

# Define a tuple that will describe the column headers of the table
# Putting this here should set the design of the bill table
# Length of the table and any references to fields should use this tuple
TABLE_COLUMNS = ("Description", "Unit Cost", "Qty/Rate", "Amount")


# SQL Configuration
# TODO Define any necessary configurations for linking the application
# TODO to the SQL server. In the future, this may be user configurable.
# TODO But for now, we will use a strict configuration setting for this
# TODO implementation
