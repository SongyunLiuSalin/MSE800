from database4 import (
    create_student_table,
    create_enrollment_table,
    create_lecture_table,
    create_lecturer_table,
    create_subjects_table
)

from student_manager import (
    add_student,
    view_students,
    search_student,
    delete_student,
    add_enrolment,
    view_enrolments,
    add_lecturer,
    add_subject,
    students_per_course,
    students_more_than_one_course
)


def menu():
    print("\n==== Student Enrolment System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Add Enrolment")
    print("6. View All Enrolments")
    print("7. Add Lecturer")
    print("8. Add Subject")
    print("9. Students per Course")
    print("10. Students Enrolled in More Than One Course")
    print("11. Exit")


def main():
    create_student_table()
    create_enrollment_table()
    create_lecture_table()
    create_lecturer_table()
    create_subjects_table()

    while True:
        menu()

        choice = input("Select an option (1-11): ")

        if choice == '1':
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            b_date = input("Enter birth date: ")

            add_student(f_name, l_name, b_date)

        elif choice == '2':
            students = view_students()

            for student in students:
                print(student)

        elif choice == '3':
            name = input("Enter name to search: ")

            students = search_student(name)

            for student in students:
                print(student)

        elif choice == '4':
            student_id = int(input("Enter student ID: "))

            delete_student(student_id)

        elif choice == '5':
            student_code = int(input("Enter student ID: "))
            date_of_enrollment = input("Enter enrolment date: ")
            course_name = input("Enter course name: ")
            cc_number = int(input("Enter CC#: "))

            add_enrolment(
                student_code,
                date_of_enrollment,
                course_name,
                cc_number
            )

        elif choice == '6':
            enrolments = view_enrolments()

            for enrolment in enrolments:
                print(enrolment)

        elif choice == '7':
            l_firstname = input("Enter first name: ")
            l_lastname = input("Enter last name: ")
            l_email = input("Enter email: ")
            l_address = input("Enter address: ")

            add_lecturer(
                l_lastname,
                l_firstname,
                l_email,
                l_address
            )

        elif choice == '8':
            subject_unit = input("Enter subject name: ")
            subject_udsc = input("Enter subject description: ")

            add_subject(
                subject_unit,
                subject_udsc
            )

        elif choice == '9':
            results = students_per_course()

            print("\nStudents registered in each course:")

            for result in results:
                print(result)

        elif choice == '10':
            results = students_more_than_one_course()

            print("\nStudents enrolled in more than one course:")

            for result in results:
                print(result)

        elif choice == '11':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()