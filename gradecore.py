import os
import sqlite3

DATABASE_FILE = "grades.db"

def check_database():
	if os.path.isfile(DATABASE_FILE):
		return
	else:
		db = sqlite3.connect(DATABASE_FILE)
		cursor = db.cursor()
		cursor.execute("""CREATE TABLE grades(id INTEGER PRIMARY KEY,
			name TEXT)""")
		db.commit()
		db.close()

def add_student(name):
	db = sqlite3.connect(DATABASE_FILE)
	cursor = db.cursor()
	cursor.execute("""INSERT INTO grades(name) VALUES(?)""", (name,))
	db.commit()
	db.close()

def print_all_students():
	db = sqlite3.connect(DATABASE_FILE)
	cursor = db.cursor()
	cursor.execute("""SELECT id, name FROM grades""")
	records = cursor.fetchall()
	for r in records:
		print(r)
	db.close()

check_database()
db = sqlite3.connect(DATABASE_FILE)
