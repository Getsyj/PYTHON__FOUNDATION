import mysql.connector

# ✅ Connection Function
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="0805Fbpfk",
        database="hexaairlines"
    )

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

    # Create quizzes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quizzes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            subject VARCHAR(100)
        )
    """)

    # Create results table with foreign keys
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            quiz_id INT,
            marks_obtained INT,
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Tables created successfully.")

# Insert sample data
def insert_sample_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Insert students
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
    cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", ("Bob", "bob@example.com"))

    # Insert quizzes
    cursor.execute("INSERT INTO quizzes (subject) VALUES (%s)", ("Math",))
    cursor.execute("INSERT INTO quizzes (subject) VALUES (%s)", ("Science",))

    # Insert results
    cursor.execute("INSERT INTO results (student_id, quiz_id, marks_obtained) VALUES (%s, %s, %s)", (1, 1, 85))
    cursor.execute("INSERT INTO results (student_id, quiz_id, marks_obtained) VALUES (%s, %s, %s)", (1, 2, 90))
    cursor.execute("INSERT INTO results (student_id, quiz_id, marks_obtained) VALUES (%s, %s, %s)", (2, 1, 78))

    conn.commit()
    conn.close()
    print("✅ Sample data inserted.")

# View all students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# View all results with student names and subjects
def view_results():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.name, q.subject, r.marks_obtained
        FROM results r
        JOIN students s ON r.student_id = s.id
        JOIN quizzes q ON r.quiz_id = q.id
    """)
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Update student's email
def update_student_email(student_id, new_email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET email = %s WHERE id = %s", (new_email, student_id))
    conn.commit()
    conn.close()
    print(f"✅ Email updated for student ID {student_id}.")

# Delete student and their results
def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM results WHERE student_id = %s", (student_id,))
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    print(f" Student ID {student_id} and related results deleted.")

def view_all_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")  # For MySQL
    tables = cursor.fetchall()
    print("📁 Tables in database:")
    for table in tables:
        print(table[0])
    conn.close()

def describe_table(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"DESCRIBE {table_name}")  # For MySQL
    print(f" Structure of '{table_name}':")
    for row in cursor.fetchall():
        print(row)
    conn.close()

