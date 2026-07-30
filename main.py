from auth import login
from database import save_students, load_students
from student import Student

if not login():
    print("Exiting Program...")
    exit()

students = []


def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, age, course, marks)
    students.append(student)
    save_students(students)

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

def update_student():
    update_id = int(input("enter student ID to Update"))

    for student in students:
        if student.student_id == update_id:

            print("\n Current details:")
            student.display()


            student.name = input("Enter New Name  ;")
            student.age = int(input("Enter new Age:"))
            student.course = input("Enter New Course")
            student.marks = float(input("Enter New Marks:"))

            print("\n ✅ Student Updated Successfully!")
            return

        print("\n❌ Student Not Found!")
        save_students(students)

def delete_student():
    delete_id = int(input("Enter Student Id to delete"))

    for  student in students:
          if student.student_id == delete_id :
              students.remove(student)
              students.remove(student)
              print("\n✅ Student Deleted Successfully!")
              return


    print("\n❌ Student Not Found!")

    

        




while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()
              

    elif choice == "5":
        delete_student()
        

    elif choice == "6":
        print("Thank you for using Student Management System.") 
        break