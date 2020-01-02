#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Configuration settings for invoice application.
###############################################################################

DEBUG = True # Set to true to output to terminal
LOG = True # Set to true to output to log file

# Application information
APP_TITLE = "Outvoice"

# Main window dimensions
GUI_WIDTH = 900
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

# Define a Dictionary that will describe the column id and header names of the table
# Definition: {<id>:<header name>, ...}
TABLE_COLUMNS = {"des":"Description", "cost":"Unit Cost", "qty":"Qty/Rate", "amt":"Amount"}


# SQL Configuration
# TODO Define any necessary configurations for linking the application
# TODO to the SQL server. In the future, this may be user configurable.
# TODO But for now, we will use a strict configuration setting for this
# TODO implementation
