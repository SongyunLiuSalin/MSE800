"""
This program defines a Student class with attributes for name, age, address, and student ID. It creates a list of Student objects, sorts them by age in descending order, and prints their names and ages.

"""

class Student:
    name: str
    age: int
    address: str
    student_id: str

    def __init__(self, name, age, address, student_id):
        self.name = name
        self.age = age
        self.address = address
        self.student_id = student_id


    

def main():
    students = []

    student1 = Student("Alice Johnson", 20, "123 Main St", "S001")
    student2 = Student("Bob Smith", 22, "456 Elm St", "S002")

    students.append(student1)
    students.append(student2)
    students.append(Student("Jane Smith", 22, "789 Oak St", "S003"))
    students.append(Student("Alice Johnson", 20, "321 Pine St", "S004"))
    students.append(Student("Bob Brown", 23, "654 Maple St", "S005"))

    students.sort(key=lambda student: student.age, reverse=True)


    for student in students:
        print(f"Name: {student.name}, Age: {student.age}")

if __name__ == "__main__":
    main()