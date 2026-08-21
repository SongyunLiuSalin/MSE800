import sqlite3


def create_connection():
    conn = sqlite3.connect("student_enrolment.db")
    return conn


def create_student_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            nid INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            b_date TEXT
        )
    ''')

    conn.commit()
    conn.close()


def create_enrollment_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollment (
            student_code INTEGER NOT NULL,
            date_of_enrollment TEXT NOT NULL,
            course_name TEXT NOT NULL,
            "CC#" INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def create_lecture_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecture (
            "CC#" INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            lecture_name TEXT NOT NULL,
            subject TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def create_lecturer_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer (
            lecture_id INTEGER PRIMARY KEY AUTOINCREMENT,
            l_lastname TEXT NOT NULL,
            l_firstname TEXT NOT NULL,
            l_email TEXT NOT NULL,
            l_address TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def create_subjects_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            subject_code INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_unit TEXT NOT NULL,
            subject_udsc TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()