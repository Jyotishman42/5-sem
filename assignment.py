import mysql.connector
from mysql.connector import Error

# ---------------------------
# CONNECT TO DATABASE
# ---------------------------
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ParamjitSQL",
            database="assignment_python"
        )
        print("Database connection successful.")
        return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None


# ---------------------------
# INSERT OPERATION
# ---------------------------
def insert_student(connection, student_id, name, sessional, class_test, assignment):
    try:
        cursor = connection.cursor()
        total = sessional + class_test + assignment

        query = """
        INSERT INTO student_marks (student_id, name, sessional_exam, class_test, assignment, total_marks)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (student_id, name, sessional, class_test, assignment, total))
        connection.commit()  # COMMIT
        print("Record inserted successfully.")

    except Error as e:
        connection.rollback()  # ROLLBACK
        print("Insert failed. ROLLBACK executed.", e)


# ---------------------------
# READ - FETCH ONE STUDENT
# ---------------------------
def get_student(connection, student_id):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM student_marks WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        print("Student Record:", result)

    except Error as e:
        print("Error reading data:", e)


# ---------------------------
# READ - FETCH ALL STUDENTS
# ---------------------------
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student_marks")
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("Error reading all students:", e)


# ---------------------------
# UPDATE STUDENT MARKS
# ---------------------------
def update_marks(connection, student_id, new_sessional):
    try:
        cursor = connection.cursor()

        query = "UPDATE student_marks SET sessional_exam = %s WHERE student_id = %s"
        cursor.execute(query, (new_sessional, student_id))

        connection.commit()  # COMMIT
        print("Marks updated successfully.")

    except Error as e:
        connection.rollback()
        print("Update failed. ROLLBACK executed.", e)


# # ---------------------------
# # DELETE STUDENT RECORD
# # ---------------------------
def delete_student(connection, student_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM student_marks WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        connection.commit()
        print("Record deleted successfully.")
    except Error as e:
        connection.rollback()
        print("Delete failed. ROLLBACK executed.", e)


# ---------------------------
# MAIN PROGRAM
# ---------------------------
connection = create_connection()

if connection:
    # SAMPLE OPERATIONS
    # insert_student(connection, 2, "Joy Khura", 80,40, 25)
    # get_student(connection, 2)
    # update_marks(connection, 1, 35)
    get_all_students(connection)
    delete_student(connection, 2)
    get_all_students(connection)


    connection.close()