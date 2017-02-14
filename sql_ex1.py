import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()

	c.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 10)")
	c.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 15)")
	c.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', 30)")
	c.execute("INSERT INTO inventory VALUES('Ford', 'Avenger', 20)")