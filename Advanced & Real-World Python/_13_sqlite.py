import sqlite3


connection = sqlite3.connect("college.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")


students = [
    ("Jeel", 20, "IT"),
    ("Aman", 21, "CS"),
    ("Rahul", 20, "IT")
]

cursor.executemany(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    students
)

connection.commit()


cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute(
    "SELECT name, course FROM students WHERE age = ?",
    (20,)
)

rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.execute(
    "UPDATE students SET course = ? WHERE name = ?",
    ("AI", "Jeel")
)

connection.commit()


cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Rahul",)
)

connection.commit()


cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)


connection.close()