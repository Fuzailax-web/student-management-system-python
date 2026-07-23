from student import Student

# Get input from the user
student_id = int(input("Enter Student ID: "))
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
course = input("Enter Course: ")
marks = float(input("Enter Marks: "))

# Create Student object
student1 = Student(student_id, name, age, course, marks)

# Display details
print("\nStudent added successfully!")
student1.display()