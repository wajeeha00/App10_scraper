import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('select * from events')
rows = cursor.fetchall()
print(rows)