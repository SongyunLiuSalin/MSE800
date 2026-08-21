from database4 import create_connection

import sqlite3


def add_student(f_name, l_name, b_date):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (f_name, l_name, b_date) VALUES (?, ?, ?)",
            (f_name, l_name, b_date)
        )

        conn.commit()
        print("Student added successfully.")

    except sqlite3.IntegrityError:
        print("Student could not be added.")

    conn.close()


def view_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()
    return rows


def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE f_name LIKE ? OR l_name LIKE ?",
        ('%' + name + '%', '%' + name + '%')
    )

    rows = cursor.fetchall()

    conn.close()
    return rows


def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE nid = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    print("Student deleted.")


def add_enrolment(student_code, date_of_enrollment, course_name, cc_number):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO enrollment
        (student_code, date_of_enrollment, course_name, "CC#")
        VALUES (?, ?, ?, ?)
        ''',
        (student_code, date_of_enrollment, course_name, cc_number)
    )

    conn.commit()
    conn.close()

    print("Enrolment added successfully.")


def view_enrolments():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM enrollment")
    rows = cursor.fetchall()

    conn.close()
    return rows


def add_lecturer(l_lastname, l_firstname, l_email, l_address):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO lecturer
        (l_lastname, l_firstname, l_email, l_address)
        VALUES (?, ?, ?, ?)
        """,
        (l_lastname, l_firstname, l_email, l_address)
    )

    conn.commit()
    conn.close()

    print("Lecturer added successfully.")


def add_subject(subject_unit, subject_udsc):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO subjects
        (subject_unit, subject_udsc)
        VALUES (?, ?)
        """,
        (subject_unit, subject_udsc)
    )

    conn.commit()
    conn.close()

    print("Subject added successfully.")


# Query 1:
# How many students are registered in each course?
def students_per_course():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT course_name, COUNT(DISTINCT student_code)
        FROM enrollment
        GROUP BY course_name
    """)

    rows = cursor.fetchall()

    conn.close()
    return rows


# Query 2:
# List the names and student IDs of students
# who have enrolled in more than one course.
def students_more_than_one_course():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.nid, s.f_name, s.l_name
        FROM students s
        JOIN enrollment e
        ON s.nid = e.student_code
        GROUP BY s.nid, s.f_name, s.l_name
        HAVING COUNT(DISTINCT e.course_name) > 1
    """)

    rows = cursor.fetchall()

    conn.close()
    return rows