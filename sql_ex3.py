#Output specific values in SQL

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("SELECT * FROM inventory where make = 'Ford'")

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1], r[2])