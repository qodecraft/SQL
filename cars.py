#import SQLite3 library
import sqlite3

#create a new database if database doesn't exist
conn = sqlite3.connect("cars.db")

#creates a cursor object so that we can execute sql commands
cursor = conn.cursor()

#create a new table
cursor.execute("CREATE TABLE inventory (make TEXT, model TEXT, quantity INT) ")

#close connection
conn.close()
