import sqlite3


connection = sqlite3.connect("students.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")


cursor.execute("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", ("Jeel", 20, "IT"))


connection.commit()


cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)


cursor.execute(
    "SELECT * FROM students WHERE age = ?",
    (20,)
)

students = cursor.fetchall()

for student in students:
    print(student)


cursor.execute(
    "UPDATE students SET age = ? WHERE name = ?",
    (21, "Jeel")
)


cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Jeel",)
)


connection.commit()

connection.close()