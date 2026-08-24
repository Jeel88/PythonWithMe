import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college"
)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
""")


cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
    ("Jeel", 20, "IT")
)

connection.commit()


cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)


cursor.execute(
    "SELECT * FROM students WHERE age = %s",
    (20,)
)

students = cursor.fetchall()

for student in students:
    print(student)


cursor.execute(
    "UPDATE students SET course = %s WHERE name = %s",
    ("AI", "Jeel")
)

connection.commit()


cursor.execute(
    "DELETE FROM students WHERE name = %s",
    ("Jeel",)
)

connection.commit()


cursor.close()
connection.close()