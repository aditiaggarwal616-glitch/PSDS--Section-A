import mysql.connector

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor = con.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS CollegeDB")

# Select Database
cursor.execute("USE CollegeDB")

# Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    email VARCHAR(100)
)
""")

# Create Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    credits INT
)
""")

# Create Enrollment table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
)
""")

print("Database and tables created successfully!")

cursor.close()
con.close()