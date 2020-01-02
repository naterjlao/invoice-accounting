#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#	Main running script for invoice application.
###############################################################################

import tkinter as tk

# Propietary
import ui
import config
import linker
import utils

# Wrapper for debug messages
def debug(message):
	utils.debug(message,type="main")

if __name__ == "__main__":
	# Create a Logger at startup
	logger = utils.Logger()
	# Manager
	manager = linker.Manager(logger=logger)
	# GUI
	mainWindow = tk.Tk()
	mainWindow.wm_title(config.APP_TITLE)
	mainWindow.geometry(config.GUI_DIMENSIONS)
	app = ui.Application(master=mainWindow,manager=manager,logger=logger)
	app.mainloop()
	