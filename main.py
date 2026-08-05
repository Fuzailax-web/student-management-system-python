from auth import login
from database import save_students, load_students, export_to_csv
from student import Student
from logger import logger 


if not login():
    print("Exiting Program...")
    exit()

students = load_students()


def add_student():
    student_id = int(input("Enter Student ID: "))

    for student in students:
        if student.student_id == student_id:
            print("\n❌ Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, age, course, marks)
    students.append(student)

    save_students(students)
    logger.info(f"Student Added: {student.name} (ID: {student.student_id})")

    print("\n✅ Student Added Successfully!")

def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n========== Student List ==========")

    for student in students:
        student.display()

def search_student():
    print("\n========== Search Student ==========")
    print("1. Search by Student ID")
    print("2. Search by Student Name")

    search_choice = input("Enter your choice: ")

    if search_choice == "1":
        search_id = int(input("Enter Student ID to search: "))

        for student in students:
            if student.student_id == search_id:
                print("\n✅ Student Found!")
                student.display()
                return

        print("\n❌ Student Not Found!")

    elif search_choice == "2":
        search_name = input("Enter Student Name to search: ")

        for student in students:
            if student.name.lower() == search_name.lower():
                print("\n✅ Student Found!")
                student.display()
                return

        print("\n❌ Student Not Found!")

    else:
        print("\n❌ Invalid Choice!")


def student_statistics():
    all_students = load_students()

    if len(all_students) == 0:
        print("\nNo students found.")
        return

    highest_student = max(all_students, key=lambda student: student.marks)
    lowest_student = min(all_students, key=lambda student: student.marks)

    total_marks = sum(student.marks for student in all_students)
    average_marks = total_marks / len(all_students)

    pass_count = 0
    fail_count = 0

    for student in all_students:
        if student.marks >= 50:
            pass_count += 1
        else:
            fail_count += 1

    print("\n======== Student Statistics ========")
    print(f"Total Students : {len(all_students)}")
    print(f"Highest Marks  : {highest_student.marks}")
    print(f"Top Student    : {highest_student.name}")
    print(f"Lowest Marks   : {lowest_student.marks}")
    print(f"Lowest Student : {lowest_student.name}")
    print(f"Average Marks  : {average_marks:.2f}")
    print(f"Pass Students  : {pass_count}")
    print(f"Fail Students  : {fail_count}")



def update_student():
    update_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student.student_id == update_id:

            print("\nCurrent Details:")
            student.display()

            student.name = input("Enter New Name: ")
            student.age = int(input("Enter New Age: "))
            student.course = input("Enter New Course: ")
            student.marks = float(input("Enter New Marks: "))

            save_students(students)
            logger.info(f"Student Updated: {student.name} (ID: {student.student_id})")

            print("\n✅ Student Updated Successfully!")
            return

    print("\n❌ Student Not Found!")

def delete_student():
    delete_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student.student_id == delete_id:
            students.remove(student)
            save_students(students)
            logger.info(f"Student Deleted: {student.name} (ID: {student.student_id})")
            print("\n✅ Student Deleted Successfully!")
            return

    print("\n❌ Student Not Found!")


while True:

    def sort_students():
        print("\n======= Sort Students ========")
        print("1. Sort by Name (A-Z)")
        print("2. Sort by Marks (Highest First)")
        print("3. Back")

        sort_choice = input ("Enter your Choice:")


        if sort_choice == "1":
            sorted_students = sorted(students, key=lambda student: student.name.lower())

            print("\n============= Student Sorted by Name ============")

            for student in sorted_students:
                student.display()

        elif sort_choice == "2":
            sorted_students = sorted(
                students,
                key=lambda student: student.marks,
                reverse=True
            )

            print("\n=========== Sorted by Marks ============")

            for student in sorted_students:
                student.display()
        elif sort_choice == "3":
            return

        else:
            print("\n Invalid choice!")

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student (ID/Name)")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Export to CSV")
    print("8. Sort Students")
    print("9. Exit")

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
        student_statistics()

    elif choice == "7":
        export_to_csv()
        logger.info("Student data exported to students.csv")
        print("\n✅ Students exported successfully to students.csv.")

    elif choice == "8":
        sort_students()

    elif choice == "9":
        print("Thank you for using Student Management System.")
        break

    