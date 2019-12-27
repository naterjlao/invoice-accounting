#!/usr/bin/python3
###############################################################################
# File: ui.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#	Main running script for invoice application.
###############################################################################

import tkinter as tk
import ui
import config

if __name__ == "__main__":
	# Main runner
	root = tk.Tk()
	root.wm_title(config.TITLE)
	root.geometry(config.GUI_DIMENSIONS)
	app = ui.Application(master=root)
	app.mainloop()
	
