from student import Student

students = []


def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, age, course, marks)
    students.append(student)

    print("\n✅ Student Added Successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n========== Student List ==========")

    for student in students:
        student.display()

def search_student():
    search_id = int(input("Enter Student ID to search: "))

    for student in students:
        if student.student_id == search_id:
            print("\n✅ Student Found!")
            student.display()
            return

    print("\n❌ Student Not Found!")       


while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you ")
        break

    else:
        print("❌ Invalid Choice.") 