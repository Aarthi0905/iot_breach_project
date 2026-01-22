import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM breaches")
count = cursor.fetchone()[0]

print("Rows in breaches table:", count)

conn.close()