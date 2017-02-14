#import sqlite

import sqlite3

#using with keyword to prevent quotation errors

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

cities = [
		('Boston', 'MA', 'US', 1231231),
		('Chicago', 'IL', 'US', 1231231),
		('Houston', 'TX', 'US', 1234433)
]

c.executemany('INSERT INTO population VALUES(?, ?, ?, ?)', cities)

