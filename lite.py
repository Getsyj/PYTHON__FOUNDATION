import sqlite3
 
# ------------------------------------
# Step 1: Database Connection
# ------------------------------------
def create_connection():
    conn = sqlite3.connect("student_quiz.db")
    return conn
 
# ------------------------------------
# Step 2: Create Tables
# ------------------------------------
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
 
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL
                    )''')
 
    cursor.execute('''CREATE TABLE IF NOT EXISTS quizzes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER,
                        subject TEXT NOT NULL,
                        score INTEGER,
                        FOREIGN KEY (student_id) REFERENCES students(id)
                    )''')
 
    conn.commit()
    conn.close()
 
# ------------------------------------
# Step 3: CRUD Operations
# ------------------------------------
# Create / Insert
def insert_student(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Email already exists.")
    conn.close()
 
def insert_quiz(student_id, subject, score):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quizzes (student_id, subject, score) VALUES (?, ?, ?)",
                   (student_id, subject, score))
    conn.commit()
    print("Quiz record added successfully!")
    conn.close()
 
# Read
def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("---- Students ----")
    for s in students:
        print(s)
    conn.close()
 
def view_quizzes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT quizzes.id, students.name, subject, score
                      FROM quizzes
                      JOIN students ON quizzes.student_id = students.id''')
    quizzes = cursor.fetchall()
    print("---- Quizzes ----")
    for q in quizzes:
        print(q)
    conn.close()
 
# Update
def update_student_email(student_id, new_email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET email = ? WHERE id = ?", (new_email, student_id))
    conn.commit()
    print("Student email updated.")
    conn.close()
 
# Delete
def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quizzes WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student and their quiz records deleted.")
    conn.close()
 
# ------------------------------------
# Step 4: Sample Usage / Menu
# ------------------------------------
def menu():
    create_tables()
    while True:
        print("\n--- Student Quiz Management ---")
        print("1. Add Student")
        print("2. Add Quiz")
        print("3. View Students")
        print("4. View Quizzes")
        print("5. Update Student Email")
        print("6. Delete Student")
        print("7. Exit")
        choice = input("Enter choice: ")
 
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            insert_student(name, email)
        elif choice == '2':
            view_students()
            student_id = int(input("Enter Student ID: "))
            subject = input("Enter subject: ")
            score = int(input("Enter score: "))
            insert_quiz(student_id, subject, score)
        elif choice == '3':
            view_students()
        elif choice == '4':
            view_quizzes()
        elif choice == '5':
            student_id = int(input("Enter Student ID: "))
            new_email = input("Enter new email: ")
            update_student_email(student_id, new_email)
        elif choice == '6':
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
 
# Run the program
if __name__ == "__main__":
    menu()
 