import json
import csv
from student import Student

FILE_NAME = "students.json"


def save_students(student_list):
    data = []

    for student in student_list:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )
            students.append(student)

        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []

    
def export_to_csv():
    students = load_students()

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Student ID", "Name", "Age", "Course", "Marks", "Grade"])

        for student in students:
            writer.writerow([
                student.student_id,
                student.name,
                student.age,
                student.course,
                student.marks,
                student.calculate_grade()
            ])
          


     