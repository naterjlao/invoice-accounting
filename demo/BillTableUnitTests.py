#!/usr/bin/python3
###############################################################################
# File: BillTableUnitTests.py
# Author: Nate Lao (lao.nathan95@gmail.com)
# Language: python3
# Description:
#   Unit Test for the BillTable class.
###############################################################################

import sys
import os
sys.path.append(os.getcwd() + '/..')
import random
import classes_temp as classes

def randomItem():
	cost = random.randint(0,255) + random.uniform(0.0,1.0)
	quant = random.randint(0,255)
	
	return (cost,quant)
	
# Generate random values for the table, discount rate and tax rate
# Check to see if the values calculate appropriately
if __name__ == "__main__":
	table = classes.BillTable()
	
	sum = 0
	# Generate a list of random items
	for i in range(0,10):
		item = randomItem()
		table.add("item"+str(i),item[0],item[1])
		sum += item[0]*item[1]
	
	taxRate = random.randint(0,255) + random.uniform(0.0,1.0)
	discountRate = random.randint(0,255) + random.uniform(0.0,1.0)
	taxAmount = taxRate * sum
	discountAmount = discountRate * sum
	finalAmount = sum - discountAmount + taxAmount
	
	print(str(table))
	table.setDiscountRate(discountRate)
	table.setTaxRate(taxRate)	
	print("Expected total balance = " + str(finalAmount))
	print("Actual total balance = " + str(table.calcTotalBalance()))
	
	assert finalAmount == table.calcTotalBalance()
	
	
# TODO
# test remove()
