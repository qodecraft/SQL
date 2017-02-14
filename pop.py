#INSET command practice

#import the sqlite3 library
import sqlite3

#creat the connectiong object
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 'US',80001)")

cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 'US', 85000)")

#commit the changes

conn.commit()

#Close the database connection
conn.close()