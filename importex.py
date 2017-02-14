#import from CSV
import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#open CSV file and asign it to a variable
	employees = csv.reader(open("employees.csv", "rU"))

	#create a new table called employees
	c.execute("CREATE TABlE IF NOT EXISTS employees(firstname TEXT, lastname TEXT)")

	#insert data into table
	c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?, ?)", (employees))

